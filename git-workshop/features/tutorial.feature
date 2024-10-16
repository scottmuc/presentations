Feature: Git Workshop Faciliator Script

  # https://github.com/scottmuc/presentations/tree/main/git#empty-repository
  Scenario: Initializing a new repository
    Given I have a directory that is not a git repository
    When I run git init in the directory
    Then a .git directory exists
    And .git/HEAD contains the text "ref: refs/heads/main"
    And .git/refs contains a directory named heads

  # Scenario: commit something
  #   Given there was a commit with a commit message that is "foo"
  #   When we run the log
  #   Then the log shows an entry with the message that is "foo"

  # Scenario: Revealing git log is reverse traversal of the graph
  #   Given I have an empty repository
  #   When a series of commits are made with messages
  #     | great   |
  #     | is      |
  #     | git     |
  #     | think   |
  #     | I       |
  #   Then the "git log --oneline" prints out
  #     | sha          | message |
  #     | ^[0-9a-f]{7} | I       |
  #     | ^[0-9a-f]{7} | think   |
  #     | ^[0-9a-f]{7} | git     |
  #     | ^[0-9a-f]{7} | is      |
  #     | ^[0-9a-f]{7} | great   |
