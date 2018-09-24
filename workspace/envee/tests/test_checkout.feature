Feature: Assign the order and complete the order

  Scenario Outline: envee
    Given a username and password click submit button
    When on clicking purchase app 
    Then add product 
    And Receive the product by enter the vendor bill
    And validate by receiving the product 
    And verify the inventory updated in inventory app
    And sale the product in pos adayar