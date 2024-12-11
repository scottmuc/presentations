from behave import *
import subprocess
from utils import capture_output_from_commands

@given(u'a series of commits are made with messages')
def step_impl(context):
    context.execute_steps(u'''
        Given I have a directory that is not a git repository
        When I run git init in the directory
        When a series of commits are made with messages
            | message |
            | great   |
            | is      |
            | git     |
            | think   |
            | I       |
    ''')


@when(u'I checkout the SHA for the commit with the message \'git\'')
def step_impl(context):
    context.sha = capture_output_from_commands(['git', 'rev-parse', 'HEAD^^'], context)
    result = subprocess.run(['git', 'checkout', context.sha], cwd=context.dirpath, check=True)
    assert result.returncode == 0


@then(u'HEAD is pointing to a SHA and not a ref')
def step_impl(context):
    head_content = capture_output_from_commands(['cat', '.git/HEAD'], context)
    assert head_content == context.sha
    assert not head_content.startswith('ref: ')
