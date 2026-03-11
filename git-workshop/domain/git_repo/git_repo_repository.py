from domain.directory.directory import Directory
from domain.command_runner.command_runner import CommandRunner


class GitRepoRepository:
    def __init__(self, cmd: CommandRunner):
        self.cmd = cmd

    def is_initialized(self, directory: Directory) -> bool:
        result = self.cmd.run(directory.path, "ls", ".git")
        return result.succeeded

    def initialize(self, directory: Directory):
        self.cmd.run(directory.path, "git", "init", "--initial-branch=main")
