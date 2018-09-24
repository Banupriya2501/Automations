Feature: pos order existing customer

  Scenario Outline: placing order with existing customer
    Given a username and password click submit button
    When on selection of product 
    Then enter the existing customer phone number
    And click payment type
    And check order placed in magento
    