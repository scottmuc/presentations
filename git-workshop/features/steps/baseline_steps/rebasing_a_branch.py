
from behave import then
from test_helpers.command_runner import CommandRunner


@then(u'a rebase of banana onto main is completed')
def step_impl(context):
    cmd = CommandRunner()
    result = cmd.run(
        context.repo.dirpath, 'git', 'rebase', 'main', 'banana'
        )
    assert result.exitcode == 0
