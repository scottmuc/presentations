class Head:
    def __init__(self, ref: "Commit | Branch") -> None:
        self._ref = ref

    @property
    def ref(self) -> "Commit | Branch":
        return self._ref

    @property
    def is_detached(self) -> bool:
        return isinstance(self._ref, Commit)

    def checkout(self, ref: "Commit | Branch") -> None:
        self._ref = ref


    def ref_commit(self) -> "Commit | None":
        if self.is_detached:
            assert isinstance(self._ref, Commit)
            return self._ref
        else:
            assert isinstance(self._ref, Branch)
            return self._ref.ref


    def commit(self, message: str) -> None:
        if not self.is_detached:
            assert isinstance(self._ref, Branch)
            branch = self._ref
            parent = branch.ref
            new_commit = Commit(message=message, parent=parent)
            self._ref = Branch("main", new_commit)
        else:
            assert isinstance(self._ref, Commit)
            parent = self._ref
            self._ref = Commit(message=message, parent=parent)


    def log(self) -> list["Commit"]:
        current = self.ref_commit

        commits = []
        while current is not None:
            commits.append(current)
            assert isinstance(current, Commit)
            current = current.parent
        return commits


class Commit:
    def __init__(self, message: str, parent: "Commit | None") -> None:
        self._message = message
        self._parent = parent

    @property
    def message(self) -> str:
        return self._message

    @property
    def parent(self) -> "Commit | None":
        return self._parent


class Branch:
    def __init__(self, name: str, ref: "Commit | None") -> None:
        self._name = name
        self._ref = ref

    @property
    def name(self) -> str:
        return self._name

    @property
    def ref(self) -> "Commit | None":
        return self._ref

