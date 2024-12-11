import tempfile
import subprocess
from behave import *
from git_repo import GitRepo

@given(u'a series of commits are made with messages')
def step_impl(context):
    # context.execute_steps(u'''
    #     Given I have a directory that is not a git repository
    #     When I run git init in the directory
    #     When a series of commits are made with messages
    #         | message |
    #         | great   |
    #         | is      |
    #         | git     |
    #         | think   |
    #         | I       |
    # ''')
    context.repo = GitRepo(dirpath=tempfile.mkdtemp())
    context.repo.init_with_commits(['great', 'is', 'git', 'think', 'I'])


@when(u'I checkout the commit with the message \'git\' using its SHA')
def step_impl(context):
    context.sha = context.repo.capture_output_from_commands(['git', 'rev-parse', 'HEAD^^'])
    context.repo.checkout_quiet(context.sha)


@then(u'git is in a detached HEAD state')
def step_impl(context):
    head_content = context.repo.get_head()
    assert head_content == context.sha
    assert not head_content.startswith('ref: ')
