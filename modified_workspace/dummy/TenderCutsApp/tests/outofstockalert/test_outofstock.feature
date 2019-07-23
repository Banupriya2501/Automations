Feature: out of stock alert 

  Background:
    Given a username <username> and password <password>
    And when a user click login button it redirect to location page
    And enter the location name
    And when a user select location option it redirect to category page
    

  Scenario: outofstock cartpage

    Given change the staging advance inventory <productid> <qty> <forecastqty>
    When click category product image chicken it redirect to tcuts product page
    Then click add button from chickencurrycut <product> product
    And check proceed option enable
    And click proceed button it redirect to cartsummary page
    And increase quantityo in cart page <quantity>
    And check out of stock alert displays

  Examples: Vertical
  | username    | 9710243651  |
  | password    | 123456      |
  | product     | chicken     |
  | quantity    | 3           |
  | productid   | 193         |
  | qty         | 1           |
  | forecastqty | 0           |


  Scenario: outofstock tcuts

    Given change the staging advance inventory <productid> <qty> <forecastqty>
    When click category product image chicken it redirect to tcuts product page
    Then click add button <quantity> from chickencurrycut <product> product
    And check out of stock alert displays

  Examples: Vertical
  | username    | 9710243651  |
  | password    | 123456      |
  | product     | chicken     |
  | quantity    | 3           |
  | productid   | 193         |
  | qty         | 1           |
  | forecastqty | 0           |
 
  Scenario: outofstock payment page

    Given click category product image chicken it redirect to tcutsproduct page
    When click add button <quantity> from chickencurrycut<product> product
    Then check proceed option enable
    And click proceed button it redirect to cartsummary page
    And click checkout button it redirect to deliverysummary page
    And select time slot and delivery address <product>
    And change the staging grams inventory <productid> <qty> <forecastqty>
    And when a user click continue button it redirect to payment page
    And select a cash on delivery option
    And when a user click place order button 
    And verify the popup displays
    And check it redirect to home page
    And add inventory <productid> <updateqty> <forecastqty>
    
  Examples: Vertical
  | username    | 9710243651  |
  | password    | 123456      |
  | product     | chicken     |
  | quantity    | 1           |
  | productid   | 193         |
  | qty         | 0           |
  | forecastqty | 0           |
  | updateqty   | 1           |

   Scenario: outofstock and place order

    Given click category product image chicken it redirect to tcutsproduct page
    When click add button <quantity> from chickencurrycut<product> product
    Then check proceed option enable
    And click proceed button it redirect to cartsummary page
    And click checkout button it redirect to deliverysummary page
    And select time slot and delivery address <product>
    And change the staging grams inventory <productid> <qty> <forecastqty>
    And when a user click continue button it redirect to payment page
    And select a cash on delivery option
    And when a user click place order button 
    And verify the popup displays  
    And when a user click place order button and it redirects to continueshopping page
    And verify the order placed in magento <ordertype> <paymenttype>
    And add inventory <productid> <updateqty> <forecastqty>
    
    
  Examples: Vertical
  | username    | 9710243651    |
  | password    | 123456        |
  | product     | chicken       |
  | quantity    | 2             |
  | ordertype   | express       |
  | paymenttype | cashondelivery|
  | productid   | 193           |
  | qty         | 0.500         |
  | forecastqty | 0             | 
  | updateqty   | 1             |