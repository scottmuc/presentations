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

    def commit(self, message: str) -> None:
        parent = self._ref
        self._ref = Commit(message=message, parent=parent)

    def log(self) -> list[Commit]:
        current = self._ref
        commits = []
        while current is not None:
            commits.append(current)
            current = current.parent
        return commits
