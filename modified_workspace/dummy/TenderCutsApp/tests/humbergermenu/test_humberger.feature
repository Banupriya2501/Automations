Feature: humberger menu
  

  Scenario: humberger menu

    Given a username <username> and password <password>
    When a user click login button it redirect to location page
    Then enter the location name
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click humberger menu
    And verify the menu present

  Examples:
  | username   | password | 
  | 9710243651 | 123456   | 

  Scenario: location change from humbermenu

    Given a username <username> and password <password>
    When a user click login button it redirect to location page
    Then enter the location name
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click humberger menu
    And click location from humber menu
    And enter the location <changelocation> name
    And verify it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click humberger menu
    And verify the location name

  Examples:
  | username   | password |  changelocation  |
  | 9710243651 | 123456   |  adayar         |