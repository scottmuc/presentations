from behave import then, when
from test_setup_helpers.command_runner import CommandRunner


@when(u'creating a branch named {branch_name}')
def step_impl(context, branch_name):
    cmd = CommandRunner()
    result = cmd.run(context.repo.dirpath, 'git', 'branch', branch_name)
    assert result.exitcode == 0


@then(u'branch {branch_1} and {branch_2} both point to the same commit')
def step_impl(context, branch_1, branch_2):
    cmd = CommandRunner()
    head_1 = cmd.run(context.repo.dirpath, 'cat', '.git/refs/heads/{branch_1}').output
    print("head_1", head_1)
    head_2 = cmd.run(context.repo.dirpath, 'cat', '.git/refs/heads/{branch_2}').output
    expected_head_1 = 'ref: refs/heads/{branch_1}'
    expected_head_2 = 'ref: refs/heads/{branch_2}'
    assert head_1 == f"ref: refs/heads/{branch_1}", f"Expected {head_1} to be {expected_head_1}"
    assert head_2 == f"ref: refs/heads/{branch_2}", f"Expected {head_2} to be {expected_head_2}"
