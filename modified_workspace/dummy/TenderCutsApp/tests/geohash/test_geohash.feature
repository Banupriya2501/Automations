Feature: geohash failure

  Scenario: geohash fails
    Given a username <username> and password <password>
    When a user click login button it redirect to location page
    Then deny the location and verify the alert on map and add address
    And verify toast message <toastmessage>

  Examples:
  | username    | password | toastmessage  |
  | 9710243651  |  123456  | Address Added |