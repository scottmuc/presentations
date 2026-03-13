from infrastructure import GitDriver
from domain import GitBackedBranchRepository

def main() -> None:
    driver = GitDriver()
    driver.init()
    branch_repo = GitBackedBranchRepository(driver)
    main_branch = branch_repo.find_by_name("main")
    print(main_branch.name)

if __name__ == "__main__":
    main()
