from infrastructure import GitDriver, TempGitDirectory
from domain import GitBackedBranchRepository

def main() -> None:
    # Setup

    # Creates a git initalized temporary directory
    temp_repo = TempGitDirectory()

    # All the driver needs is a path to a git repository
    driver = GitDriver(path=temp_repo.dirpath)

    # Add a single commit to the initialized repository so
    # that listing branchs works.
    driver.create_commit("foo")

    # Use the domain
    branch_repo = GitBackedBranchRepository(driver)
    main_branch = branch_repo.find_by_name("main")
    print(main_branch.name)

if __name__ == "__main__":
    main()
