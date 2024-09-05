Feature: showing off behave

  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    Then behave will test it for us!

  Scenario: commit something
    Given there was a commit with a commit message that is "foo"
    When we run the log
    Then the log shows an entry with the message that is "foo"
