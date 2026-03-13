from infrastructure import GitDriver

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
        branches = []
        for branch_name in self.driver.list_branches():
            branches.append(Branch(name=branch_name))
        return branches
