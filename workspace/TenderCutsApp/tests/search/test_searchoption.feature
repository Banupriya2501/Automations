Feature: placing order from search option

  Scenario: place order via search option
    Given a username <username> and password <password>
    When a user click login button it redirect to location page
    Then enter the location name
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click the search option and enter product name
    And check proceed option enable
    And click proceed button it redirect to cartsummary page
    And click checkout button it redirect to deliverysummary page
    And select time slot and delivery address <product>
    And when a user click continue button it redirect to payment page
    And select a cash on delivery option
    And a user click place order button it redirect to continue shopping page
    And verify the order placed in magento <ordertype> <paymenttype>

  Examples:
  | username    | password | product   |  ordertype  | paymenttype   |
  |  9710243651 | 123456   | chicken  |   express    |cashondelivery |   
