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
* After this no one should want to install a db server on their laptop

## Timeline

    Start +-------------------------------------+
    0m    + Introduction and Demo               +
          +                                     +
    10m   + What is Vagrant                     +
          + Anatomy of the Chef Run             +
    20m   +                                     +
          +                                     +
    30m   + Workshop                            +
          +                                     +
    40m   +                                     +
          + Q&A                                 +
    50m   +                                     +
          + Feedback                            +
    60m   +-------------------------------------+ End

### Introduction and Demo (0min)

This workshop is about automating infrastructure with Vagrant and Chef. We'll specifically target Postgresql as it is a
common external dependency.

Start a new rails project that will use Postgresql:

    rails new demo_app -d postgresql
    cd demo_app
    # update config/database.yml
    rake db:create && rails s

Browse to http://localhost:3000/ and we should see an error connecting to the database. Let's make this work.

Navigate to the vagrant-postgresql repository and execute

    script/database up

Pass around USB sticks so that everyone has VirtualBox and Vagrant installed. Want to reach a point where everyone is
ready to run `script/database up`. While everyone is running that go into the mechanics of Vagrant.

### What is Vagrant (5min)

Vagrant is like IAAS (infrastructure as a service) for your local machine. With amazon you can create new machines
starting from base AMIs (amazon machine images). With Vagrant you can create new machines using base boxes. Everyone
should try and import the base box that was on the USB stick.

    vagrant basebox add precise64 <path to the precise64.box from USB stick>

Try the following command:

    vagrant init precise64 && vagrant up

This created a locally running Ubuntu 12.04 server. Now destroy it with the following command:

    vagrant destroy -f

There's your re-usable infrastructure.

The problem is... this box doesn't do much, so let's make it do something interesting.

### Anatomy of the Chef Run (15min)


### Workshop (15min)

Everyone should have a running database server. Everyone is encouraged to play around with the server

