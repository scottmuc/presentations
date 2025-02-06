import tempfile

from test_helpers.command_runner import CommandRunner


class TempGitRepo:
    def __init__(self):
        self.dirpath = tempfile.mkdtemp()

    def init(self):
        cmd = CommandRunner()
        cmd.run(self.dirpath, 'git', 'init', '--initial-branch=main')

    def add_test_commit_with_message(self, message):
        cmd = CommandRunner()
        cmd.run(self.dirpath, 'touch', message)
        cmd.run(self.dirpath, 'git', 'add', message)
        cmd.run(self.dirpath, 'git', 'commit', '-m', message)
        
    def init_with_commits(self, messages):
        self.init()
        message_list = [msg. strip() for msg in messages.split(',')]
        for message in message_list:
            self.add_test_commit_with_message(message)

    def checkout_quiet(self, ref):
        cmd = CommandRunner()
        cmd.run(self.dirpath, 'git', 'checkout', '-q', ref)
    
    def read_head(self):
        cmd = CommandRunner()
        return cmd.run(self.dirpath, 'cat', '.git/HEAD').output
    
