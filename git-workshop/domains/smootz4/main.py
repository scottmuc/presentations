from domain import InMemoryBranchRepository, Branch

def main() -> None:
    branch_repo = InMemoryBranchRepository()
    branch_repo.save(Branch(name="main"))
    main_branch = branch_repo.find_by_name("main")
    print(main_branch.name)

if __name__ == "__main__":
    main()
