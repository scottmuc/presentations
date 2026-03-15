from behave import then, when
from test_helpers.command_runner import CommandRunner


@when(u'a branch {branch_name} is created')
def step_impl(context, branch_name):
    cmd = CommandRunner()
    result = cmd.run(context.repo.dirpath, 'git', 'branch', branch_name)
    assert result.exitcode == 0


@then(u"branch {branch_1} and branch {branch_2} "
      "both point to the same commit")
def step_impl(context, branch_1, branch_2):
    cmd = CommandRunner()
    repo_dir = context.repo.dirpath
    head_1 = cmd.run(repo_dir, 'cat', f".git/refs/heads/{branch_1}").output
    head_2 = cmd.run(repo_dir, 'cat', f".git/refs/heads/{branch_2}").output
    assert head_1 == head_2
