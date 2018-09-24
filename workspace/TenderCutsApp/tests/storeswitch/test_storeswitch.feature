Feature: placing express order

  Scenario: store switch from location
    Given a username <username> and password <password>
    When a user click login button it redirect to location page
    Then enter the location name
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click add button <quantity> from chickencurrycut <product> product
    And check proceed option enable
    And click proceed button it redirect to cartsummary page
    And click checkout button it redirect to deliverysummary page
    And select time slot and select out side delivery address <product>
    And check store switch alert 
    And verify it redirect to home page 
    And verify the humbermenu location  

  Examples:
  | username   | password | product |  quantity  |
  | 9710243651 | 123456   | chicken |    1       |