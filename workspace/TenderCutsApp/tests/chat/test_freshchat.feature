Feature: fresh chat

  Scenario: fresh chat
    Given a username <username> and password <password>
    When a user click login button it redirect to location page
    Then when a user enter the location name
    And a user select location option it redirect to category page
    And a user click chat tab it redirect to chat page
    And enter a msg and click send msg option
    And click Narrow back arrow

  Examples:
  | username    | password |
  |  9710243651 |  123456  |