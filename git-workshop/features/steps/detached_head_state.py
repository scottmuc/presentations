from behave import given, then, when
from test_helpers.command_runner import CommandRunner
from test_helpers.temp_git_repo import TempGitRepo


@given(u'a series of commits is made with messages: {messages}')
def step_impl(context, messages):
    context.repo = TempGitRepo()
    context.repo.init_with_commits(messages)


@when(u'I checkout the commit with the message \'git\' using its SHA')
def step_impl(context):
    cmd = CommandRunner()
    result = cmd.run(context.repo.dirpath, 'git', 'rev-parse', 'HEAD^^')
    context.sha = result.output
    context.repo.checkout_quiet(context.sha)
    assert result.exitcode == 0, f"Expected {result['exitcode']} to be 0"


@then(u'git is in a detached HEAD state')
def step_impl(context):
    head_content = context.repo.read_head()
    errmsg = f"Expected {head_content} to be equal to {context.sha}"
    assert head_content == context.sha, errmsg
    assert not head_content.startswith('ref: ')


@given(u'HEAD is in a detached state')
def step_impl(context):
    context.execute_steps(u'''
        Given I have a directory that is not a git repository
        When I run git init in the directory
        And a series of commits is made with messages: great, is, git, think, I
    ''')


@when(u'checking out the branch main')
def step_impl(context):
    cmd = CommandRunner()
    result = cmd.run(context.repo.dirpath, 'git', 'checkout', 'main')
    assert result.exitcode == 0


@then(u'HEAD points back to the branch main')
def step_impl(context):
    context.execute_steps(u'''
        Then .git/HEAD contains the text "ref: refs/heads/main"
    ''')


@then(u'HEAD still points to the branch main')
def step_impl(context):
    context.execute_steps(u'''
        Then .git/HEAD contains the text "ref: refs/heads/main"
    ''')
