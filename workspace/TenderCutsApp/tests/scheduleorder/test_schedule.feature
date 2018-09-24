Feature: schedule order


  Background:
    Given a username <username> and password <password>
    And when a user click login button it redirect to location page
    And enter the location name
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click add button <quantity> from kolaurudai <product> product
    And check proceed option enable
    And click proceed button it redirect to cartsummary page
    And click checkout button it redirect to deliverysummary page
    And select time slot and delivery address <product>
    And when a user click continue button it redirect to payment page

  Scenario: schedule order card

    Given select a cash on delivery option
    When a user click place order button it redirect to continue shopping page
    Then verify the order placed in magento <ordertype> <paymenttype>

  Examples: Vertical
  | username   | 9710243651     |
  | password   | 123456         |
  | product    | marinades      |
  | ordertype  | schedule       |
  | quantity   |   2            |
  | paymenttype| cashondelivery |

  Scenario: schedule order cod

    Given a user card and enter cvv number
    When a user click place order button it redirect to bank page
    And a user click success button from razor payment
    Then verify the order placed in magento <ordertype> <paymenttype>

  Examples: Vertical
  | username   | 9710243651 |
  | password   | 123456     |
  | product    | marinades  |
  | ordertype  | schedule   |
  | quantity   |   2        |
  | paymenttype|  juspay    |
