import tempfile

from domain.directory.directory import Directory
from domain.command_runner.command_runner import CommandRunner


class DirectoryRepository:
    def __init__(self, cmd: CommandRunner):
        self.cmd = cmd

    def create_temp_directory(self) -> Directory:
        return Directory(tempfile.mkdtemp())

    def has_child_with_name(self, directory: Directory, name: str) -> bool:
        result = self.cmd.run(directory.path, "ls", name)
        return result.succeeded
