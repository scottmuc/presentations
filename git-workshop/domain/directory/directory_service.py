from domain.directory.directory import Directory
from domain.directory.directory_repository import DirectoryRepository


class DirectoryService:
    def __init__(self, directory_repository: DirectoryRepository):
        self.directory_repository = directory_repository

    def create_temp_directory(self) -> Directory:
        return self.directory_repository.create_temp_directory()
