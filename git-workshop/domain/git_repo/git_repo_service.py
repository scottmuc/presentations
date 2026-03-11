from domain.directory.directory import Directory
from domain.git_repo.git_repo_repository import GitRepoRepository


class GitRepoService:
    def __init__(self, git_repo_repository: GitRepoRepository):
        self.git_repo_repository = git_repo_repository

    def is_initialized(self, directory: Directory) -> bool:
        return self.git_repo_repository.is_initialized(directory)

    def initialize(self, directory: Directory):
        self.git_repo_repository.initialize(directory)
