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
      When the branch main is checked out
      Then HEAD points back to the branch main


  Scenario: Creating a branch
      Given a series of commits is made with messages: great, is, git, think, I
        When a branch branch_2 is created
        Then branch main and branch branch_2 both point to the same commit
        And HEAD still points to the branch main


  Scenario: Reset a branch
      Given a series of commits is made with messages: great, is, git, think, I
        When resetting to HEAD^^
        Then branch main points to the commit with message think
        And HEAD still points to the branch main


  # Scenario: Rebase a branch 
  #   Given a series of commits is made with messages: great, is, git, think, I
  #   When a branch banana is created
  #   And the branch banana is checked out
  #   And a reset to HEAD^ is done
  #   And a series of commits is made with messages: do not
  #   And running "git log --oneline" prints out
  #   | sha          | message  |
  #   | ^[0-9a-f]{7} | do not   |
  #   | ^[0-9a-f]{7} | think    |
  #   | ^[0-9a-f]{7} | git      |
  #   | ^[0-9a-f]{7} | is       |
  #   | ^[0-9a-f]{7} | great    |
  #   And a rebase of "banana" onto "main" is completed
  #   Then running "git log --oneline" prints out
  #   | sha          | message  |
  #   | ^[0-9a-f]{7} | I        |
  #   | ^[0-9a-f]{7} | do not   |
  #   | ^[0-9a-f]{7} | think    |
  #   | ^[0-9a-f]{7} | git      |
  #   | ^[0-9a-f]{7} | is       |
  #   | ^[0-9a-f]{7} | great    |
  #   And HEAD will still be on banana