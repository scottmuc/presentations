from behave import given, then, when
from smootz_06_introduce_tests.domain import Head, Branch, Commit


@given(u'I have a directory that is not a git repository')
def step_impl(context):
    main_branch = Branch(name="main", ref=None)
    context.head = Head(ref=main_branch)
    assert context.head and main_branch is not None


@when(u'I run git init in the directory')
def step_impl(context):
    pass


@then(u'a .git directory exists')
def step_impl(context):
    pass


@then(u'.git/HEAD contains the text "ref: refs/heads/main"')
def step_impl(context):
    assert context.head.ref.name == "main"


@then(u'.git/refs/heads/main doesn\'t exist')
def step_impl(context):
    assert context.head.ref.ref is None


@given(u'I have an empty repository')
def step_impl(context):
    context.execute_steps(u'''
        Given I have a directory that is not a git repository
        When I run git init in the directory
    ''')


@when(u'a series of commits is made with messages: {messages}')
def step_impl(context, messages):
    raise NotImplementedError("Step not implemented")
    # message_list = [msg. strip() for msg in messages.split(',')]
    # for message in message_list:
    #     context.repo.add_test_commit_with_message(message)


@then(u'running "git log --oneline" prints out')
def step_impl(context):
    raise NotImplementedError("Step not implemented")
    # cmd = CommandRunner()
    # log_output = cmd.run(context.repo.dirpath,
    #                      'git', 'log', '--oneline').output
    # commit_messages = log_output.split('\n')
    # sha_pattern = r'[0-9a-f]{7}'
    #
    # for i, row in enumerate(context.table):
    #     message = f"{sha_pattern} {row['message']}"
    #     errmsg = f'''
    #         Expected commit message: {message}
    #         But got: {commit_messages[i]}'''
    #     assert re.match(message, commit_messages[i]), errmsg


@then(u'the contents of .git/refs/heads/main contains a SHA')
def step_impl(context):
    raise NotImplementedError("Step not implemented")
    # cmd = CommandRunnerjj()
    # result = cmd.run(context.repo.dirpath, 'cat', ".git/refs/heads/main")
    # debugging = cmd.run(context.repo.dirpath, 'ls', "-laR")
    # assert result.output != '', debugging.output


@then(u'the parent commit of HEAD does not exist')
def step_impl(context):
    raise NotImplementedError("Step not implemented")
    # cmd = CommandRunner()
    # contains_parent = 'parent' in result.output
    # errmsg = f"Expected no parent in the following output: {result.output}"
    # assert contains_parent is False, errmsg
