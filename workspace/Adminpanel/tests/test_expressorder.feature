Feature: pos order existing customer

  Scenario Outline: placing express order 
    Given a username and password click submit button
    When user select the customer
    Then select the store
    And add product to cart
    And select delivery type and express time slot
    And place the order