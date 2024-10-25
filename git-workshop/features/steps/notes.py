from behave import *
import tempfile
import subprocess
import os

@given(u'there was a commit with a commit message that is "foo"')
def step_impl(context):
    # we need a directory to nominate a repository
    dirpath = tempfile.mkdtemp()
    # shutil.rmtree(dirpath)

    # we need to initialize it with git init
    p = subprocess.Popen(['git', 'init'], cwd=dirpath)
    p.wait()

    # we need to git commit -m "foo"
    p = subprocess.Popen(['touch', 'foo'], cwd=dirpath)
    p.wait()

    p = subprocess.Popen(['git', 'add', './foo'], cwd=dirpath)
    p.wait()

    p = subprocess.Popen(['git', 'commit', '-m', 'foo'], cwd=dirpath)
    p.wait()

    print(dirpath)

    # we need to make dirpath accessible to the @when and @then steps
    context.dirpath = dirpath


@when(u'we run the log')
def step_impl(context):
    p = subprocess.Popen(['git', 'log', '--oneline', '--graph', '--all', '--decorate'], stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         cwd=context.dirpath, 
                         text=True) 
    
    # we need to obtain the output of the git log command
    stdout, stderr = p.communicate()
    context.log_output = stdout
    

@then(u'the log shows an entry with the message that is "foo"')
def step_impl(context):
    assert 'foo' in context.log_output


@then(u'the "git log --oneline" like')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the "git log --oneline" like')

@then(u'the "git log --oneline" prints out')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the "git log --oneline" prints out')
