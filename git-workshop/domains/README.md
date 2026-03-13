# DDD'ing a Git Repository

## Entities

* Repository (or maybe this is redundant)
* Commit
* Branch
* Diff?
* Author

## Domain Services

* CommitService

## Repositories

* CommitRepository (what a git kinda is sort of)

## Pseudo Code Ideas

Repository repo = new Repository();
ChangeSet changeSet = new ChangeSet()

Author author = new Author("test", "test@example.com")
repo.commit(changeSet, author)

Commit[] log = repo.Log()
Branch[] branches = repo.Branches()
