from behave import given, then, when
from command_runner import CommandRunner
from git_repo import TempGitRepo


@given(u'a series of commits is made with messages {messages}')
def step_impl(context, messages):
    context.repo = TempGitRepo()
    context.cmd = CommandRunner()
    context.repo.init_with_commits(messages)


@when(u'I checkout the commit with the message \'git\' using its SHA')
def step_impl(context):
    context.sha = context.cmd.capture_output_from_command(context.repo.dirpath, 'git', 'rev-parse', 'HEAD^^')
    context.repo.checkout_quiet(context.sha)
    assert context.cmd.returncode == 0, f"Expected {context.cmd.returncode} to be 0"


@then(u'git is in a detached HEAD state')
def step_impl(context):
    head_content = context.repo.read_head()
    assert head_content == context.sha, f"Expected {head_content} to be equal to {context.sha}"
    assert not head_content.startswith('ref: ')


@given(u'HEAD is in a detached state')
def step_impl(context):
    context.execute_steps(u'''
        Given I have a directory that is not a git repository
        When I run git init in the directory
        And a series of commits is made with messages
    ''')


@when(u'creating a branch from the commit HEAD is pointing to')
def step_impl(context):
    raise NotImplementedError(u'STEP: When creating a branch from the commit HEAD is pointing to')


@then(u'HEAD is reattached to the branch')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then HEAD is reattached to the branch')
