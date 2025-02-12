from behave import then, when
from test_helpers.command_runner import CommandRunner


@when(u'resetting the branch main to HEAD^^')
def step_impl(context):
    cmd = CommandRunner()
    result = cmd.run(context.repo.dirpath, 'git', 'reset', '--hard', 'HEAD^^')
    assert result.exitcode == 0
    


@then(u'branch main points to the commit with message think')
def step_impl(context):
    cmd = CommandRunner()
    result_branch = cmd.run(context.repo.dirpath, 'cat', '.git/refs/heads/main')
    sha = result_branch.output
    result_head = cmd.run(context.repo.dirpath, 'git', 'rev-parse', 'HEAD')
    head = result_head.output
    assert head == sha, f"Expected {head} to equal {sha}"