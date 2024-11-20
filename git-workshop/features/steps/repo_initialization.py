from behave import *
from pathlib import Path
import tempfile
import subprocess
import os
import re

@then(u'a .git directory exists')
def step_impl(context):
    result = subprocess.run(['ls', '.git'], cwd=context.dirpath)
    assert result.returncode == 0


@then(u'.git/HEAD contains the text "ref: refs/heads/main"')
def step_impl(context):
    git_head_path = os.path.join(context.dirpath, '.git', 'HEAD')
    contents = Path(git_head_path).read_text().strip()
    assert contents == "ref: refs/heads/main", f"Expected 'ref: refs/heads/main', but got '{contents}'"


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
        p = subprocess.Popen(['touch', f'{message}'], cwd=context.dirpath)
        p.wait()

        p = subprocess.Popen(['git', 'add', f'{message}'], cwd=context.dirpath)
        p.wait()
        p = subprocess.Popen(['git', 'commit', '-m', f'{message}'], cwd=context.dirpath, stdout=subprocess.PIPE, text=True)
        p.wait()

        stdout, stderr = p.communicate()
        context.log_output = stdout
        
    
    
@then(u'running "git log --oneline" prints out')
def step_impl(context):
    p = subprocess.Popen(['git', 'log', '--oneline'], cwd=context.dirpath, stdout=subprocess.PIPE, text=True)
    p.wait()
    stdout, stderr = p.communicate()
    log_output = stdout.strip()
    commit_messages = log_output.split('\n')
    sha_pattern = r'[0-9a-f]{7}'

    for i,row in enumerate(context.table): 
        message = f"{sha_pattern} {row['message']}"
        assert re.match(message, commit_messages[i]), f"Expected commit message: {message}, but got: {commit_messages[i]}"
