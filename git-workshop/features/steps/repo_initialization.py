import tempfile
import subprocess
import os
import re
from behave import *
from git_repo import GitRepo


@given(u'I have a directory that is not a git repository')
def step_impl(context):
    context.repo = GitRepo(dirpath=tempfile.mkdtemp())
    result = subprocess.run(['ls', '.git'], cwd=context.repo.dirpath)
    assert result.returncode != 0


@when(u'I run git init in the directory')
def step_impl(context):
    context.repo.init()


@then(u'a .git directory exists')
def step_impl(context):
    result = subprocess.run(['ls', '.git'], cwd=context.repo.dirpath)
    assert result.returncode == 0


@then(u'.git/HEAD contains the text "ref: refs/heads/main"')
def step_impl(context):
    head_content = context.repo.get_head()
    assert head_content == "ref: refs/heads/main", f"Expected 'ref: refs/heads/main', but got '{head_content}'"


@then(u'.git/refs/heads/main doesn\'t exist')
def step_impl(context):
    result = subprocess.run(['ls', '.git/refs/heads/main'], cwd=context.repo.dirpath)
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
        context.repo.add_file_and_commit(message, message)

   
@then(u'running "git log --oneline" prints out')
def step_impl(context):
    log_output = context.repo.capture_output_from_commands(['git', 'log', '--oneline'])
    commit_messages = log_output.split('\n')
    sha_pattern = r'[0-9a-f]{7}'

    for i, row in enumerate(context.table):
        message = f"{sha_pattern} {row['message']}"
        assert re.match(message, commit_messages[i]), f"Expected commit message: {message}, but got: {commit_messages[i]}"
