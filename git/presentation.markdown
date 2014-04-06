---
title: The Human Git Graph
---
# The Human Git Graph
---
    git init
    cat .git/HEAD
---
    git init
    git commit -m 'great'
---
    git init
    git commit -m 'great'
    git commit -m 'is'
---
    git init
    git commit -m 'great'
    git commit -m 'is'
    git commit -m 'git'
---
    git init
    git commit -m 'great'
    git commit -m 'is'
    git commit -m 'git'
    git commit -m 'think'
---
    git init
    git commit -m 'great'
    git commit -m 'is'
    git commit -m 'git'
    git commit -m 'think'
    git commit -m 'I'
---
    git init
    git commit -m 'great'
    git commit -m 'is'
    git commit -m 'git'
    git commit -m 'think'
    git commit -m 'I'
    git checkout B3CC
---
    git init
    git commit -m 'great'
    git commit -m 'is'
    git commit -m 'git'
    git commit -m 'think'
    git commit -m 'I'
    git checkout B3CC
    git checkout master
---
    git init
    git commit -m 'great'
    git commit -m 'is'
    git commit -m 'git'
    git commit -m 'think'
    git commit -m 'I'
    git checkout B3CC
    git checkout master
    git branch branch-1
---
    git init
    git commit -m 'great'
    git commit -m 'is'
    git commit -m 'git'
    git commit -m 'think'
    git commit -m 'I'
    git checkout B3CC
    git checkout master
    git branch branch-1
    git checkout branch-1
---
    git init
    git commit -m 'great'
    git commit -m 'is'
    git commit -m 'git'
    git commit -m 'think'
    git commit -m 'I'
    git checkout B3CC
    git checkout master
    git branch branch-1
    git checkout branch-1
    git checkout master
    git reset EF12
---
    git init
    git commit -m 'great'
    git commit -m 'is'
    git commit -m 'git'
    git commit -m 'think'
    git commit -m 'I'
    git checkout B3CC
    git checkout master
    git branch branch-1
    git checkout branch-1
    git checkout master
    git reset EF12
    git commit -m 'do not'
---
    git init
    git commit -m 'great'
    git commit -m 'is'
    git commit -m 'git'
    git commit -m 'think'
    git commit -m 'I'
    git checkout B3CC
    git checkout master
    git branch branch-1
    git checkout branch-1
    git checkout master
    git reset EF12
    git commit -m 'do not'
    git rebase master branch-1
