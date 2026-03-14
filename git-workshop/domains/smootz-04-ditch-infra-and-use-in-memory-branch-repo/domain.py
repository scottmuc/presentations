class Branch:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name


class BranchRepository:
    def find_by_name(self, name: str) -> Branch:
        raise NotImplementedError

    def find_all(self) -> list[Branch]:
        raise NotImplementedError

    def save(self, branch: Branch) -> None:
        raise NotImplementedError


class InMemoryBranchRepository(BranchRepository):

    def __init__(self) -> None:
        self.branches = []

    def find_by_name(self, name: str) -> Branch:
        for branch in self.find_all():
            if branch.name == name:
                return branch
        raise ValueError(f"Branch {name} not found")


    def find_all(self) -> list[Branch]:
        return self.branches


    def save(self, branch: Branch) -> None:
        self.branches.append(branch)
