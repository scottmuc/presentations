## Objectives

* Demonstrate the value in workstation automation

## Timeline

    Start +-------------------------------------+
    0m    + Introduction                        +
          +                                     +
    10m   +                                     +
          +                                     +
    20m   +                                     +
          +                                     +
    30m   +-------------------------------------+ End

## Introduction (5 minutes)

How long do we spend ensuring our tools work (not just locally but across machine
lifecycles and inside the team).

*Who* anyone that fears losing their cozy dev environment. How confident are you that
you could be up and running again when you get a new laptop?
*What* Makefiles or project bootstrap scripts are great but they only get you so far.
How do you get bootstrapped if your laptop is stolen? What about a new employee? How
do you share useful shell scripts or other utilities?

### The Toolchain

[sprout](https://github.com/pivotal-sprout) is a collection of [chef](https://www.chef.io/)
cookbooks. A gem called [soloist](https://github.com/mkocher/soloist) is the entry point to
the automation execution.

Alternatives exist:

* [boxen](https://boxen.github.com/) which runs on [puppet](https://puppetlabs.com/)
* [boxstarter](http://www.boxstarter.org/) is Windows focused
* [babushka](http://babushka.me/) is minimal compared to the other OSX options

### Examples

* https://github.com/grassdog/osx

### What Do I Do?

```
xcode-select --install
git clone https://github.com/scottmuc/workstation.git
cd workstation
sudo gem install bundler
bundle install
soloist
cat TODO.md
```

### Remix Culture

The music community has a concept of taking a piece of one song and a piece of
another. Workstation automation doesn't have to be prescriptive (except that
your machine should be recreated using automation).

### Features to Explore

* secret management
* app configuration
* backing up and restoring to some cloud drive provider

