# Testing PowerShell with Pester


## Objectives

* Should leave with some sense that PowerShell is a useful tool
* Know Pester is a tool to test PowerShell code
* Can name some scenarios where testing scripts are important

## Timeline

    Start +-------------------------------------+
    0m    + Introduction and What is Powershell +
          + Pipelines                           +
    10m   + Windows Administration              +
          + Why Pester and PowerYaml            +
    20m   + Demo                                +
          +                                     +
    30m   +                                     +
          + Lesson about OSS                    +
    40m   + Q/A                                 +
    45m   +-------------------------------------+ End

### Introduction

Explain how PowerShell is making the big time with Windows system adminstrators. Call
out Ancestry as a company who followings Continuous Delivery practices uses PowerShell
to automate everything (and Chef).

The community is a bit fragmented. There are some that write code to the letter of the law
according to Microsoft. Poor methods of sharing code is also a problem.

* Get-Content
* Get-ChildItem
* Test-Path
* Resolve-Path
* ForEach-Object

### Pipelines

Pipelines might be familiar to those that have used Unix like operating systems. PowerShell takes
it a bit further with the ability to pipeline objects, not streams.

### Windows Administration

PowerShell can built in support for nearly all the Microsoft technologies:

* Active Directory
* IIS
* Sql Server
* Azure
* etc...

If you're a Windows Admin you're not using PowerShell, then you're making your
life a lot harder.

### Pester and the Story of PowerYaml

This presentation isn't about PowerShell...

It all started with PowerYaml.

### Live Demo

* Test Structure

