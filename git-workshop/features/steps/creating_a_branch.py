from behave import then, when
from test_helpers.command_runner import CommandRunner


@when(u'creating a branch named {branch_name}')
def step_impl(context, branch_name):
    cmd = CommandRunner()
    result = cmd.run(context.repo.dirpath, 'git', 'branch', branch_name)
    assert result.exitcode == 0


@then(u'branch {branch_1} and {branch_2} both point to the same commit')
def step_impl(context, branch_1, branch_2):
    cmd = CommandRunner()
    head_1 = cmd.run(context.repo.dirpath, 'cat', f".git/refs/heads/{branch_1}").output
    head_2 = cmd.run(context.repo.dirpath, 'cat', f".git/refs/heads/{branch_2}").output
    assert head_1 == head_2
