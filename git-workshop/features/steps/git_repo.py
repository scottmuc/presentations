import subprocess
import tempfile

class GitRepo:
    def __init__(self, dirpath=None, initial_branch="main"):
        if dirpath is None:
            self.dirpath = tempfile.mkdtemp()
        else:
            self.dirpath = dirpath
        self.initial_branch = initial_branch

    def init(self):
        subprocess.run(['git', 'init'], cwd=self.dirpath, check=True)

    def add_file_and_commit(self, filename, message):
        subprocess.run(['touch', filename], cwd=self.dirpath, check=True)
        subprocess.run(['git', 'add', filename], cwd=self.dirpath, check=True)
        subprocess.run(['git', 'commit', '-m', message], cwd=self.dirpath, check=True)
        
    def init_with_commits(self, messages):
        self.init()
        for message in messages:
            self.add_file_and_commit(message, message)

    def capture_output_from_commands(self, commands) -> str:
        p = subprocess.Popen(commands, cwd=self.dirpath, stdout=subprocess.PIPE, text=True)
        p.wait()
        stdout, stderr = p.communicate()
        log_output = stdout.strip()
        if p.returncode != 0:
            raise RuntimeError(f"Command failed: {commands}, stderr: {stderr}")
        return log_output

    def checkout_quiet(self, ref):
        subprocess.run(['git', 'checkout', '-q', ref], cwd=self.dirpath, check=True)
    
    def get_head(self):
        return self.capture_output_from_commands(['cat', '.git/HEAD'])
    