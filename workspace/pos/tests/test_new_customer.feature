Feature: pos order placing with new customer

  Scenario Outline: placing order with new customer
    Given a username and password click submit button
    When on selection of product 
    Then enter the new customer phone number
    And click payment type
    And check order placed in magento
    