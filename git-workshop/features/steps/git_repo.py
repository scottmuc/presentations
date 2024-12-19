import tempfile

from command_runner import CommandRunner

class TempGitRepo:
    def __init__(self, dirpath=None, initial_branch="main"):
        if dirpath is None:
            self.dirpath = tempfile.mkdtemp()
        else:
            self.dirpath = dirpath
        self.initial_branch = initial_branch
        self.command_runner = CommandRunner()

    def init(self):
        self.command_runner.run(self.dirpath, ['git', 'init'])

    def add_test_commit_with_message(self, message):
        self.command_runner.run(self.dirpath, ['touch', message])
        self.command_runner.run(self.dirpath, ['git', 'add', message])
        self.command_runner.run(self.dirpath, ['git', 'commit', '-m', message])
        
    def init_with_commits(self, messages):
        self.init()
        for message in messages:
            self.add_test_commit_with_message(message)

    def checkout_quiet(self, ref):
        self.command_runner.run(self.dirpath, ['git', 'checkout', '-q', ref])
    
    def read_head(self):
            return self.command_runner.capture_output_from_commands(self.dirpath, ['cat', '.git/HEAD'])
    