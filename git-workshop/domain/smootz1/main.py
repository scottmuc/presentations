import tempfile
import subprocess

# Non domain code, should be in a separate module, but included here for simplicity

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

        process.wait()

        stdout, stderr = process.communicate()
        output = stdout.strip()
        exitcode = process.returncode

        return CommandResult(output, stderr, exitcode)


class GitDriver:
    def __init__(self):
        self.dirpath = tempfile.mkdtemp()

    def init(self):
        cmd = CommandRunner()
        cmd.run(self.dirpath, 'git', 'init', '--initial-branch=main')
        # Add an initial commit so that the branch exists
        message = "initial-commit"
        cmd.run(self.dirpath, 'touch', message)
        cmd.run(self.dirpath, 'git', 'add', message)
        cmd.run(self.dirpath, 'git', 'commit', '-m', message)

    def list_branches(self):
        cmd = CommandRunner()
        # Get the branch names without the leading '* ' for the current branch)
        result = cmd.run(self.dirpath, 'git', 'branch', '--format=%(refname:short)')
        return result.output.splitlines()

# --- Domain ---

class Branch:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name


class BranchRepository:
    def find_by_name(self, name: str) -> Branch:
        raise NotImplementedError

    def find_all(self) -> list[Branch]:
        raise NotImplementedError


class GitBackedBranchRepository(BranchRepository):

    def __init__(self, driver: GitDriver) -> None:
        self.driver = driver

    def find_by_name(self, name: str) -> Branch:
        for branch in self.find_all():
            if branch.name == name:
                return branch
        raise ValueError(f"Branch {name} not found")


    def find_all(self) -> list[Branch]:
        self.driver.list_branches()
        branches = []
        for branch_name in self.driver.list_branches():
            branches.append(Branch(name=branch_name))
        return branches



def main() -> None:
    driver = GitDriver()
    driver.init()
    branch_repo = GitBackedBranchRepository(driver)
    main = branch_repo.find_by_name("main")
    print(main.name)



if __name__ == "__main__":
    main()
