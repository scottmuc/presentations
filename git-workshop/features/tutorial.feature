Feature: Git Workshop Faciliator Script

  Scenario: commit something
    Given there was a commit with a commit message that is "foo"
    When we run the log
    Then the log shows an entry with the message that is "foo"
