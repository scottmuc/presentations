# Human Graph

The human graph exercises has people representing the different components in
a git graph. People will have to play: commits, branches, and HEAD.

> Git is built on a graph. Almost every Git command manipulates this graph. To
> understand Git deeply, focus on the properties of this graph, not workflows
> or commands.

The above quote is by [Mary Rose Cook](http://maryrosecook.com/blog/post/git-from-the-inside-out)

## Prerequisites

Knowing the basic mechanics of working with git. May not know the 'why' around
the mechanics, but you know enough to get in trouble.

The class should know some basics on what a commit is. This exercises abstracts
out what entails a commit and how they are created. They should do the "All the
worlds a stage" exercise before this one.

## Materials

* whiteboard to write commands (eg. reflog)
* large index cards
  * 6-10 white commit cards
  * 2-3  red branch cards
  * 1    blue HEAD card
* rope so it's easier to visualize the connections in the graph

## Objectives

* recall of the basic structures in a git graph
* ability to predict the changes in a graph after some basic commands:
  * git reset
  * git checkout
  * git commit
  * git branch
  * git rebase

## Exercise

Introduce the presentation stating that knowing how to make a commit is not
the objective of the session.

Commit messages:
  - [great, is, git, think, I, do not]

### Empty Repository

Represent an empty initialized repository by having 1 person represent the
HEAD. They should be spinning because it is pointing to branch master but it
technically doesn't exist yet.

Explain how this state represents a brand new repository. HEAD is pointing to a
branch master, and that branch doesn't exist. Git does a lot of things
impliciitly like telling HEAD that it's pointing to master

    git init
    cat .git/HEAD
    ref: refs/heads/master
    # note that .git/refs/heads/master does not exist

### First Commit

Make the first commit. A person will represent the initial commit which
which will then trigger the creation of the master branch, and HEAD will
stop spinning and point to the branch.

We're still not in a normal state because we have another exceptional condition
where the first commit does not have a parent. Explain the concept of the root
node.

    git commit -m 'great'
    # the contents of .git/HEAD are the same
    # .git/refs/heads/master now exists and the contents of the file
    # is the SHA of the first commit

### Adding More Commits

Adding a 2nd commit. The new commit will have to point to the commit that
master is pointing to. Once that's complete, master needs to update itself and
point to the new commit. 

    git commit -m 'is'
    # .git/refs/heads/master now contains the SHA of the new commit
    # The latest commit will have a parent SHA that is the SHA
    # of the first commit

Ask how does the latest commit know their parent?

Add a couple more commits (5 total) 

    git commit -m 'git'
    git commit -m 'think'
    git commit -m 'I'

Call git log to hear the commit messages in reverse order.

    git log

They should say out loud "I think git is great".

Ask what they think the branch is doing, what's its job?
Ask what HEAD has been doing this whole time.

### Detached HEAD State

Checkout the SHA for the commit with the message 'git'.

    git checkout B3CC

What happened to HEAD, and what happened to the MASTER branch?

Explain why this is called a detached HEAD state.

    cat .git/HEAD
    # This will print the SHA that HEAD is pointing to. If HEAD
    # is pointing to a SHA and not a ref, then you're workspace
    # is in a detached HEAD state.

Do a `git log` and they should say "git is great". Point out that this is
because git log starts at HEAD not at MASTER

### Checkout To Safety

Checkout the MASTER branch. This should make HEAD point back to the
master branch.

    git checkout master
    cat .git/HEAD
    ref: refs/heads/master

Explain how checking out a branch re-attaches HEAD.

### Creating A Branch

Create a branch called branch-1. Now another person is a branch and is
pointing to the same commit that master is pointing to.

    git branch branch-1
    # cat .git/refs/heads/master and .git/refs/heads/branch-1
    # are the same commit SHA!

Then checkout this new branch

    git checkout branch-1
    cat .git/HEAD
    ref: refs/heads/branch-1

### Let's Reset


Get back onto master and reset it to EF12. This should make master point to the commit with
the message 'think'.

    git checkout master
    git reset EF12

The participants should see the subtle difference between a checkout and a
reset. The commands are similar but they operate on different objects. They
should also notice how `branch-1` is left unaffected.

### I Feel A Divergence In The Graph

Make a new commit with the message 'do not'.

    git commit -m 'do not'

Now there should be a divergence in the graph. A `git log` should result in
"do not think git is great".

Ask why the message 'I' was not spoken

Now their minds should be blown a little bit. This gets into the power of git
and knowing the graph.

### All Your Rebase Are Belong To Us

Lastly, perform `git rebase master branch-1`. This should replay the 'I'
commit on top of the 'do not' commit. The tricky part about this one is that the
original 'I' commit does not change. Someone else joins the graph and points to
'do not' with their own message of 'I'. Also, branch-1 moves to the replayed
commit and HEAD now points to branch-1. `git log` should say "I do not think git
is great".

    git rebase master branch-1

Note that HEAD will always point to the branch that is being rebased.

Lesson should be that the graph is immutable. The only things that can change
values are branches and HEAD.

### Garbage Man Cometh

Maybe emulate git garbage collection and destroy the unreferenced commit
that got lost due to the rebase.

    git -c gc.reflogExpireUnreachable=0 -c gc.pruneExpire=now gc

### Burning The Reflog

Ask about the journal of commands


