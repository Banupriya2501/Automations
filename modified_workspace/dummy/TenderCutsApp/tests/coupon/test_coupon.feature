Feature: coupon code

  Scenario Outline: add and remove coupon

    Given a username <username> and password <password>
    When when a user click login button it redirect to location page
    Then enter the location name
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click add button <quantity> from chickencurrycut <product> product
    And check proceed option enable
    And click proceed button it redirect to cartsummary page
    And click on coupon tab
    And enter coupon code <coupon>
    And click checkout button it redirect to deliverysummary page
    And select time slot and delivery address <product>
    And when a user click continue button it redirect to payment page
    And click on paytm icon
    And click on back button in Paytm page
    And click on back button in Payment page
    And click on back button in Delivery Summary
    And click on Remove Button
    And click checkout button it redirect to deliverysummary page
    And when a user click continue button it redirect to payment page
    And select a cash on delivery option
    And a user click place order button it redirect to continue shopping page
    And verify the order placed in magento <ordertype> <paymenttype>

    Examples: Vertical
    | username    |  9710243651    |
    | password    |  123456        |
    | product     | chicken        |
    | quantity    |    1           |
    | coupon      | OLA75 		   |
    | ordertype	  | express		   |
    | paymenttype | cashondelivary |