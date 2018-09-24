Feature: pos order with barcde with existing customer

  Scenario Outline: placing order with barcode and reward points 
    Given a username and password click submit button
    When on selection of product with barcode 
    Then enter the existing customer phone number
    And apply reward points
    And click payment type
    And check order placed in magento
    