Feature: add card

  Scenario Outline: payment with added card

    Given a username <username> and password <password>
    When when a user click login button it redirect to location page
    Then enter the location name
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click add button <quantity> from chickencurrycut <product> product
    And check proceed option enable
    And click proceed button it redirect to cartsummary page
    And click checkout button it redirect to deliverysummary page
    And select time slot and delivery address <product>
    And when a user click continue button it redirect to payment page
    And a new added card
    And enter card numnber <card>
    And enter mm,yy <mmyy>
    And select a card and enter cvv number
    And click on Add New Card
    And click on back button in Payment page
    And click on back button in Delivery Summary
    And click on back button in Cart Summary
    And click proceed button it redirect to cartsummary page
    And click checkout button it redirect to deliverysummary page
    And when a user click continue button it redirect to payment page
    And a user click place order button it redirect to bank page
    And a user click success button from razor payment
    And verify the order placed in magento <ordertype> <paymenttype>
    And click on continue shopping
        
    Examples: Vertical
    | username    |  9710243651         |
    | password    |  123456             |
    | product     | chicken             |
    | quantity    |    1                |
    | card        | 4242424242424242 |
    | mmyy        | 12/23               |
    | ordertype   | express             |
    | paymenttype | juspay              |

    
    

  
