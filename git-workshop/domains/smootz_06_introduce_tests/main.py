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
    head.commit("great")

    # Remaind of the commits
    head.commit("is")
    head.commit("git")

    for c in head.log():
        print(c.message)
    print()

    head.commit("think")
    head.commit("I")

    for c in head.log():
        print(c.message)


if __name__ == "__main__":
    main()
