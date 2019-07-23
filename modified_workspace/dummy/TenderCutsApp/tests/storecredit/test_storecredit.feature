Feature: store credit

  Background:
    Given a username <username> and password <password>
    And when a user click login button it redirect to location page
    And enter the location name
    And update the storecredit from magento
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click add button <quantity> from chickencurrycut <product> product
    And check proceed option enable
    And click proceed button it redirect to cartsummary page
    And click checkout button it redirect to deliverysummary page
    And select time slot and delivery address <product>
    And when a user click continue button it redirect to payment page
    And check store credit applied 

  Scenario: store credit with card
    Given a user card and enter cvv number
    When a user click place order button it redirect to bank page
    And a user click success button from razor payment
    Then verify the order placed in magento <ordertype><paymenttype>

  Examples:
  | username   | password | product |   ordertype |  quantity | paymenttype | 
  | 9710243651 | 123456   | chicken |    express  |     1     |  juspay     |

  Scenario: store credit with cod
    Given select a cash on delivery option
    When a user click place order button it redirect to continue shopping page
    Then verify the order placed in magento <ordertype><paymenttype>

  Examples:
  | username   | password | product |  ordertype  |   quantity  | paymenttype     |
  | 9710243651 | 123456   | chicken |    express  |     1       | cashondelivery  |


  Scenario: auto select cod
    Given check cash on delivery option auto selected
    When a user click place order button it redirect to continue shopping page
    Then verify the order placed in magento <ordertype><paymenttype>

  Examples:
  | username   | password  | product |  ordertype  |   quantity  | paymenttype     |
  | 9710243651 | 123456    | chicken |    express  |     1       | cashondelivery  |
