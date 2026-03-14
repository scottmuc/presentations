import tempfile
import subprocess

class CommandResult:
    def __init__(self, output, stderr, exitcode):
        self.output = output
        self.stderr = stderr
        self.exitcode = exitcode


class CommandRunner:
    def run(self, dirpath, command, *args) -> CommandResult:
        process = subprocess.Popen(
                [command, *args],
                cwd=dirpath,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
        )
        stdout, stderr = process.communicate()
        output = stdout.strip()
        exitcode = process.returncode

        return CommandResult(output, stderr, exitcode)


class TempGitDirectory:
    def __init__(self):
        self.dirpath = tempfile.mkdtemp()
        cmd = CommandRunner()
        cmd.run(self.dirpath, 'git', 'init', '--initial-branch=main')


class GitDriver:
    def __init__(self, path: str):
        self.dirpath = path


    def list_branches(self):
        cmd = CommandRunner()
        # Get the branch names without the leading '* ' for the current branch)
        result = cmd.run(self.dirpath, 'git', 'branch', '--format=%(refname:short)')
        return result.output.splitlines()


    def create_commit(self, message):
        cmd = CommandRunner()
        cmd.run(self.dirpath, 'touch', message)
        cmd.run(self.dirpath, 'git', 'add', message)
        cmd.run(self.dirpath, 'git', 'commit', '-m', message)
