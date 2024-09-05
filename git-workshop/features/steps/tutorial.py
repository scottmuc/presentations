from behave import *
import tempfile
import shutil
import subprocess

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False


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

    p = subprocess.Popen(['git', 'commit', '-am', 'foo'], cwd=dirpath)
    p.wait()

    print(dirpath)


@when(u'we run the log')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we run the log')


@then(u'the log shows an entry with the message that is "foo"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the log shows an entry with the message that is "foo"')
