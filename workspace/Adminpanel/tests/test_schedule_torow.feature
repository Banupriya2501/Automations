Feature: pos order with barcde with existing customer

  Scenario Outline: placing schedule torow order 
    Given a username and password click submit button
    When user select the customer
    Then select the store
    And add product to cart
    And select delivery type and schedule torow time slot
    And place the order
    