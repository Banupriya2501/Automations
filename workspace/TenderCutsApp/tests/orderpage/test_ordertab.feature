Feature: order details
  

  Scenario: order details

    Given a username <username> and password <password>
    When a user click login button it redirect to location page
    Then enter the location name
    And a user select location option
    And click order tab
    And verify visiblity of live order and past order
    And click view details button and verify status
    And click back button
    

  Examples:
  | username   | password |  
  | 9710243651 | 123456   |

