from behave import given, then, when
from command_runner import CommandRunner
from git_repo import TempGitRepo


@given(u'a series of commits is made with messages')
def step_impl(context):
    context.repo = TempGitRepo()
    context.cmd = CommandRunner()
    context.repo.init_with_commits(['great', 'is', 'git', 'think', 'I'])


@when(u'I checkout the commit with the message \'git\' using its SHA')
def step_impl(context):
    context.sha = context.cmd.capture_output_from_command(context.repo.dirpath, 'git', 'rev-parse', 'HEAD^^')
    context.repo.checkout_quiet(context.sha)


@then(u'git is in a detached HEAD state')
def step_impl(context):
    head_content = context.repo.read_head()
    assert head_content == context.sha
    assert not head_content.startswith('ref: ')
