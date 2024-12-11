import tempfile
import subprocess
import os
import re
from behave import *
from pathlib import Path
from utils import capture_output_from_commands


@given(u'I have a directory that is not a git repository')
def step_impl(context):
    context.dirpath = tempfile.mkdtemp()
    result = subprocess.run(['ls', '.git'], cwd=context.dirpath)
    assert result.returncode != 0


@when(u'I run git init in the directory')
def step_impl(context):
    # Figuring out how to prevent the line break after this would be useful
    result = subprocess.run(['git', 'init', '--initial-branch=main'],
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL,
                   cwd=context.dirpath)
    assert result.returncode == 0


@then(u'a .git directory exists')
def step_impl(context):
    result = subprocess.run(['ls', '.git'], cwd=context.dirpath)
    assert result.returncode == 0


@then(u'.git/HEAD contains the text "ref: refs/heads/main"')
def step_impl(context):
    head_content = capture_output_from_commands(['cat', '.git/HEAD'], context)
    assert head_content == "ref: refs/heads/main", f"Expected 'ref: refs/heads/main', but got '{head_content}'"


@then(u'.git/refs/heads/main doesn\'t exist')
def step_impl(context):
    result = subprocess.run(['ls', '.git/refs/heads/main'], cwd=context.dirpath)
    assert result.returncode != 0


@given(u'I have an empty repository')
def step_impl(context):
    context.execute_steps(u'''
        Given I have a directory that is not a git repository
        When I run git init in the directory
    ''')



@when(u'a series of commits are made with messages')
def step_impl(context):
    for row in context.table:
        message = row['message']
        subprocess.run(['touch', f'{message}'], cwd=context.dirpath)
        subprocess.run(['git', 'add', f'{message}'], cwd=context.dirpath)
        context.log_output = capture_output_from_commands(['git', 'commit', '-m', f'{message}'], context)


   
@then(u'running "git log --oneline" prints out')
def step_impl(context):
    log_output = capture_output_from_commands(['git', 'log', '--oneline'], context)
    commit_messages = log_output.split('\n')
    sha_pattern = r'[0-9a-f]{7}'

    for i, row in enumerate(context.table): 
        message = f"{sha_pattern} {row['message']}"
        assert re.match(message, commit_messages[i]), f"Expected commit message: {message}, but got: {commit_messages[i]}"
