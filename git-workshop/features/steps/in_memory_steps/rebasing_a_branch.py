
from behave import then


@then(u'a rebase of banana onto main is completed')
def step_impl(context):
    raise NotImplementedError("Step not implemented")
    # cmd = CommandRunner()
    # result = cmd.run(
    #     context.repo.dirpath, 'git', 'rebase', 'main', 'banana'
    #     )
    # assert result.exitcode == 0
