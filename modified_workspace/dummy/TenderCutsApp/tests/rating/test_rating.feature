Feature: order rating

  Scenario: previous order rating

    Given a username <username> and password <password>
    When when a user click login button it redirect to location page
    Then enter the location name
    And when a user select location option it redirect to category page
    And click on rating star
    And click on taste button
    And click on quality button
    And enter the comments
    And click on submit button
    And click on Rate button

    Examples: Vertical
    | username    |  9710243651    |
    | password    |  123456        |
    