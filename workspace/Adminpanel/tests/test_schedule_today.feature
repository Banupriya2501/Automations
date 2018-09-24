Feature: pos order placing with new customer


  Scenario Outline: placing schedule today order 
    Given a username and password click submit button
    When user select the customer
    Then select the store
    And add product to cart
    And select delivery type and schedule today time slot
    And place the order
    