Feature: Git Workshop Faciliator Script

  # https://github.com/scottmuc/presentations/tree/main/git#empty-repository
  Scenario: Initializing a new repository
    Given I have a directory that is not a git repository
      When I run git init in the directory
      Then a .git directory exists
      And .git/HEAD contains the text "ref: refs/heads/main"
      And .git/refs/heads/main doesn't exist


  Scenario: The first commit
    Given I have an empty repository
      When a series of commits is made with messages: great
      Then the contents of .git/refs/heads/main contains a SHA
      And the parent commit of HEAD does not exist


  Scenario: Revealing git log is reverse traversal of the graph
    Given I have an empty repository
      When a series of commits is made with messages: great, is, git, think, I
      Then running "git log --oneline" prints out
        | sha          | message |
        | ^[0-9a-f]{7} | I       |
        | ^[0-9a-f]{7} | think   |
        | ^[0-9a-f]{7} | git     |
        | ^[0-9a-f]{7} | is      |
        | ^[0-9a-f]{7} | great   |


  Scenario: Examining git log in a detached HEAD state
    Given a series of commits is made with messages: great, is, git, think, I
      When I checkout the commit with the message 'git' using its SHA
      Then git is in a detached HEAD state
      And running "git log --oneline" prints out
        | sha          | message |
        | ^[0-9a-f]{7} | git     |
        | ^[0-9a-f]{7} | is      |
        | ^[0-9a-f]{7} | great   |


  Scenario: Re-attach a commit to a branch from a detached HEAD state
    Given HEAD is in a detached state
      When checking out the branch main
      Then HEAD points back to the branch main


 Scenario: Creating a branch
    Given a series of commits is made with messages: great, is, git, think, I
      When creating a branch named branch_2
      Then branch main and branch_2 both point to the same commit
      And HEAD still points to the branch main


 Scenario: Reset a branch
    Given a series of commits is made with messages: great, is, git, think, I
      When resetting the branch main to HEAD^^
      Then branch main points to the commit with message think
      And HEAD still points to the branch main
