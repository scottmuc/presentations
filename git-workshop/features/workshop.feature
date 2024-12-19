Feature: Git Workshop Faciliator Script

  # https://github.com/scottmuc/presentations/tree/main/git#empty-repository
  Scenario: Initializing a new repository
    Given I have a directory that is not a git repository
    When I run git init in the directory
    Then a .git directory exists
    And .git/HEAD contains the text "ref: refs/heads/main"
    And .git/refs/heads/main doesn't exist

  # Scenario: commit something
  #   Given there was a commit with a commit message that is "foo"
  #   When we run the log
  #   Then the log shows an entry with the message that is "foo"

  Scenario: Revealing git log is reverse traversal of the graph
    Given I have an empty repository
    When a series of commits is made with messages
      | message |
      | great   |
      | is      |
      | git     |
      | think   |
      | I       |
    Then running "git log --oneline" prints out
      | sha          | message |
      | ^[0-9a-f]{7} | I       |
      | ^[0-9a-f]{7} | think   |
      | ^[0-9a-f]{7} | git     |
      | ^[0-9a-f]{7} | is      |
      | ^[0-9a-f]{7} | great   |

  Scenario: Examining git log in a detached HEAD state
   Given a series of commits is made with messages
      | message |
      | great   |
      | is      |
      | git     |
      | think   |
      | I       |
    When I checkout the commit with the message 'git' using its SHA
    Then git is in a detached HEAD state


  # Scenario: Re-attach a commit to a branch from a detached HEAD state
  #   Given HEAD is in a detached state
  #   When creating a branch from the commit HEAD is pointing to
  #   Then HEAD is reattached to the branch