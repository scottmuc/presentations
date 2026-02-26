from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from typing import Optional


# --- Entity ---

@dataclass
class Thing:
    name: str
    id: UUID = field(default_factory=uuid4)

    def rename(self, new_name: str) -> None:
        if not new_name:
            raise ValueError("Name cannot be empty")
        self.name = new_name


# --- Repository Interface ---

class ThingRepository(ABC):

    @abstractmethod
    def find_by_id(self, thing_id: UUID) -> Optional[Thing]:
        ...

    @abstractmethod
    def find_all(self) -> list[Thing]:
        ...

    @abstractmethod
    def save(self, thing: Thing) -> None:
        ...

    @abstractmethod
    def delete(self, thing_id: UUID) -> None:
        ...


# --- Infrastructure ---

class InMemoryThingRepository(ThingRepository):

    def __init__(self) -> None:
        self._store: dict[UUID, Thing] = {}

    def find_by_id(self, thing_id: UUID) -> Optional[Thing]:
        return self._store.get(thing_id)

    def find_all(self) -> list[Thing]:
        return list(self._store.values())

    def save(self, thing: Thing) -> None:
        self._store[thing.id] = thing

    def delete(self, thing_id: UUID) -> None:
        self._store.pop(thing_id, None)


# --- Service ---

class ThingService:

    def __init__(self, repository: ThingRepository) -> None:
        self._repository = repository

    def get(self, thing_id: UUID) -> Optional[Thing]:
        return self._repository.find_by_id(thing_id)

    def create(self, name: str) -> Thing:
        thing = Thing(name=name)
        self._repository.save(thing)
        return thing

    def rename(self, thing_id: UUID, new_name: str) -> Thing:
        thing = self._repository.find_by_id(thing_id)
        if thing is None:
            raise ValueError(f"Thing {thing_id} not found")
        thing.rename(new_name)
        self._repository.save(thing)
        return thing

    def delete(self, thing_id: UUID) -> None:
        self._repository.delete(thing_id)


# --- Main ---

def main() -> None:
    repo = InMemoryThingRepository()
    service = ThingService(repo)

    t1 = service.create("foo")
    t2 = service.create("bar")
    t3 = service.create("baz")
    print(f"Created: {repo.find_all()}")

    fetched = service.get(t1.id)
    print(f"Fetched by ID: {fetched}")

    service.rename(t2.id, "bar-renamed")
    print(f"After rename: {repo.find_all()}")

    service.delete(t3.id)
    print(f"After delete: {repo.find_all()}")

    missing = service.get(t3.id)
    print(f"Deleted thing lookup: {missing}")

    try:
        service.rename(t1.id, "")
    except ValueError as e:
        print(f"Expected error: {e}")


if __name__ == "__main__":
    main()
