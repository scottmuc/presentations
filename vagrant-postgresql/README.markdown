# Vagrant Postgresql

Have you had to install a database server onto your laptop? Did you find it painful? What happened when you moved to
another project and didn't discover until late that you had been running the wrong version?

With the power of virtualization and automated configuration management, there's no need to ever run these kinds of
third party external dependencies on your machine. You never deploy to a Mac, so why do you run your database server on
one?

This workshop will start with showing you how you can stand up your own "production like" Postgresql database server
locally in a VM in just a few minutes. After some brief explanation, you'll be running the scripts on your machine too!

Time permitting, we can work together to make a different type of database instance.

## Objectives

* Describe what Vagrant does
* Can describe what a cookbook does
* Can setup database

## Timeline

    Start +-------------------------------------+
    0m    + Introduction and Demo               +
          +                                     +
    10m   + What is Vagrant                     +
          +                                     +
    20m   +                                     +
          +                                     +
    30m   +                                     +
          +                                     +
    40m   +                                     +
          +                                     +
    50m   +                                     +
          +                                     +
    60m   +-------------------------------------+ End

### Introduction (0min)

Introduce the topic by showing magical example. It should take just a few minutes to stand up a database server. Locally
create a rails project that talks to this database.

Pass around USB sticks so that everyone has VirtualBox and Vagrant installed. Want to reach a point where everyone is
ready to run `script/database up`. While everyone is running that go into the mechanics of Vagrant.

### What is Vagrant (10min)

Draw how AWS webservices are IAAS.
