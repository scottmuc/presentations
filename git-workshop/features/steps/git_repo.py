import tempfile

from command_runner import CommandRunner


class TempGitRepo:
    def __init__(self, initial_branch="main"):
        self.dirpath = tempfile.mkdtemp()
        self.initial_branch = initial_branch
        self.cmd = CommandRunner()

    def init(self):
        self.cmd.capture_output_from_command(self.dirpath, 'git', 'init')

    def add_test_commit_with_message(self, message):
        self.cmd.capture_output_from_command(self.dirpath, 'touch', message)
        self.cmd.capture_output_from_command(self.dirpath, 'git', 'add', message)
        self.cmd.capture_output_from_command(self.dirpath, 'git', 'commit', '-m', message)
        
    def init_with_commits(self, messages):
        self.init()
        message_list = [msg. strip() for msg in messages.split(',')]
        for message in message_list:
            self.add_test_commit_with_message(message)

    def checkout_quiet(self, ref):
        self.cmd.capture_output_from_command(self.dirpath, 'git', 'checkout', '-q', ref)
    
    def read_head(self):
            return self.cmd.capture_output_from_command(self.dirpath, 'cat', '.git/HEAD')
    