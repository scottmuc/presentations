from behave import *
import tempfile
import subprocess

@given(u'a series of commits are made with messages')
def step_impl(context):
    context.execute_steps(u'''
        Given I have a directory that is not a git repository
        When I run git init in the directory
        When a series of commits are made with messages
            | message |
            | great   |
            | is      |
            | git     |
            | think   |
            | I       |
    ''')
    

@when(u'I checkout the SHA for the commit with the message \'git\'')
def step_impl(context):
    context.dirpath = tempfile.mkdtemp()
    p = subprocess.Popen(['git', 'rev-parse', 'HEAD^^'], cwd=context.dirpath, stdout=subprocess.PIPE, text=True)
    p.wait()
    context.sha, _ = p.communicate()

    p = subprocess.run(['git', 'checkout', context.sha], cwd=context.dirpath)


@then(u'HEAD is pointing to a SHA')
def step_impl(context):
    p = subprocess.Popen(['cat', '.git/HEAD '], cwd=context.dirpath, stdout=subprocess.PIPE, text=True)
    p.wait()
    stdout, _ = p.communicate()
    assert stdout == context.sha


@then(u'HEAD is not pointing to a ref')
def step_impl(context):
    p = subprocess.Popen(['cat', '.git/HEAD '], cwd=context.dirpath, stdout=subprocess.PIPE, text=True)
    p.wait()
    stdout, _ = p.communicate()
    assert not stdout.startswith('ref: ')