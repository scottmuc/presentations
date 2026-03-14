from domain import Branch, Head

def main() -> None:
    # Simulate git init
    main_branch = Branch(name="main", ref=None)
    head = Head(ref=main_branch)

    if not head.is_detached:
        branch = head.ref
        assert isinstance(branch, Branch)
        print(f"HEAD -> {branch.name}\n")

    # First commit exploration
    main_branch.commit("great")

    # Remaind of the commits
    main_branch.commit("is")
    main_branch.commit("git")

    for c in main_branch.log():
        print(c.message)
    print()

    main_branch.commit("think")
    main_branch.commit("I")

    for c in main_branch.log():
        print(c.message)




if __name__ == "__main__":
    main()
