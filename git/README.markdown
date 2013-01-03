# Human Graph

The human graph exercises has people representing the different components in
a git graph. People will have to play: commits, branches, and HEAD.

## Prerequisites

The class should know some basics on what a commit is. This exercises abstracts
out what entails a commit and how they are created. They should do the "All the
worlds a stage" exercise before this one.

## Objectives

* recall of the basic structures in a git graph
* ability to predict the changes in a graph after some basic commands:
** git reset
** git checkout
** git commit
** git branch
** git rebase

## Exercise

Commit messages:
  - [great, is, git, think, I, do not]

1. Represent an empty initialized repository by having 1 person represent the
master branch. They should be spinning because no commits exist. Add 1 more
person that represents HEAD and have them point to the master branch.

Explain how this state represents a brand new repository. HEAD is pointing to a
branch, and that branch is pointing to nothing. Git does a lot of things
impliciitly like creating the first branch 'master'.

git init

2. Make the first commit. A person will represent the initial commit which will
make the master branch stop spinning and point to this new commit. Invoke git
log by having the commit speak out loud their message.

We're still not in a normal state because we have another exceptional condition
where the first commit does not have a parent. Explain the concept of the root
node. Also explain how from this point forward, you can't have a branch that
doesn't point to a commit

git commit -m 'great'

3. Adding a 2nd commit. The new commit will have to point to the commit that
master is pointing to. Once that's complete, master needs to update itself and
point to the new commit. Add a couple more commits (5 total) and call git log
to hear the commit messages in reverse order.

They should say out loud "I think git is great"
Ask participants what they think the branch is doing, what's its job?
Ask participants what HEAD has been doing this whole time.

git commit -m 'is'
git commit -m 'git'
git commit -m 'think'
git commit -m 'I'

4. Perform a `git checkout 'git'`. This should make HEAD point to the commit
with the message 'git'.

Explain why this is called a detached HEAD state.
Do a `git log` and they should say "git is great"
Point out the fact that the branch didn't move.

git checkout HEAD^^

5. Perform a `git checkout master`. This should make HEAD point back to the
master branch. When a `git log` is executed they should say "I think git is
great".

Explain how checking out a branch re-attaches HEAD.

git checkout master

6. Perform a `git checkout -b other_branch`. Now another person is a branch and is
pointing to the same commit that master is pointing new.

Go over the difference between that command and `git branch other_branch`.

git checkout -b other_branch

7. Perform a `git reset HEAD^` or `git reset think`. This should make
other_branch point to the commit 'think'.

The participants should see the subtle difference between a checkout and a
reset. The commands are similar but they operate on different objects. They
should also notice how the master branch is left unaffected.

git reset HEAD^

8. Make a new commit with the message 'do not'. Now there should be a divergence
in the graph. A `git log` should result in "do not think git is great". Notice
how the 'I' is left out because it cannot be traversed to by HEAD.

Now their minds should be blown a little bit. This gets into the power of git
and knowing the graph.

git commit -m 'do not'

9. Lastly, perform `git rebase other_branch master`. This should replay the 'I'
commit on top of the 'do not' commit. The tricky part about this one is that the
original 'I' commit does not change. Someone else joins the graph and points to
'do not' with their own message of 'I'. Also, master moves to the replayed
commit and HEAD now points to master. `git log` should say "I do not think git
is great".

This one is a bit confusing as to what's going on. It's unclear to me why the
HEAD switches branches. Lesson should be that the graph is immutable. The only
things that can change value are branches and HEAD.

git rebase other_branch master (I like to read this out as rebase master onto
other_branch)

10. Maybe emulate git garbage collection and destroy the unreferenced commit
that got lost due to the rebase.


