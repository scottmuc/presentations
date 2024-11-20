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
    p = subprocess.Popen(['git', 'log', '--oneline'], cwd=context.dirpath, stdout=subprocess.PIPE, text=True)
    p.wait()
    stdout, _ = p.communicate()

    # How to get the sha? :)
    sha = 'some_sha_here'

    p = subprocess.Popen(['git', 'checkout', sha], cwd=context.dirpath)
    p.wait()


@then(u'HEAD is pointing to a SHA')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then HEAD is pointing to a SHA')


@then(u'HEAD is not pointing to a ref')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then HEAD is not pointing to a ref')