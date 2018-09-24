Feature: payment failure
  
Background:
    Given a username <username> and password <password> 
    And when a user click login button it redirect to location page
    And enter the location name
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click add button <quantity> from chickencurrycut <product> product
    And check proceed option enable
    And click proceed button it redirect to cartsummary page
    And click checkout button it redirect to deliverysummary page
    And select time slot and delivery address <product>
    And when a user click continue button it redirect to payment page
    And select a card and enter cvv number
    And when a user click place order button it redirect to bank page
    And click failure button from razor payment
    
Scenario: payment failure and place with card

    Given when a user click retryoption and click placeorder
    When a user click success button from razor payment
    Then verify the order placed in magento <ordertype> <paymenttype>

    Examples:
      | username   | password | product |  ordertype  |  quantity | paymenttype |
      | 9710243651 | 123456   | chicken |    express  |     1     |  juspay     |

Scenario: payment failure and place with cod

    Given when a click Retry cod option enable and click cod
    Then verify the order placed in magento <ordertype> <paymenttype>

    Examples:
      | username   | password  | product |  ordertype  |  quantity | paymenttype         |
      | 9710243651 | 123456    | chicken |    express  |     1     |  cashondelivery     |
