Feature: app resume backgroud

  Scenario: app resume in category page
  
    Given a username <username> and password <password>
    When a user click login button it redirect to location page
    Then enter the location name
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click add button <quantity> from chickencurrycut <product> product
    And run app in background
    And change the staging advance inventory <productid> <qty> <forecastqty>
    And launch app
    And verify the popup displays

  Examples: Vertical
  | username    | 9710243651  |
  | password    | 123456      |
  | product     | chicken     |
  | quantity    | 1           |
  | productid   | 193         |
  | qty         | 0           |
  | forecastqty | 0           |

  Scenario: app resume in cart summary page and checkout
  
    Given a username <username> and password <password>
    When a user click login button it redirect to location page
    Then enter the location name
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click add button from chickencurrycut <product> product
    And check proceed option enable
    And click proceed button it redirect to cartsummary page
    And increase quantityo in cart page <quantity>
    And run app in background
    And change the staging advance inventory <productid> <qty> <forecastqty>
    And launch app
    And click checkout button it redirect to deliverysummary page
    And select time slot and delivery address <product>
    And when a user click continue button it redirect to payment page
    And select a cash on delivery option
    And when a user click place order button and it redirects to continueshopping page
    
  Examples: Vertical
  | username    | 9710243651  |
  | password    | 123456      |
  | product     | chicken     |
  | quantity    | 2           |
  | productid   | 193         |
  | qty         | 0.500       |
  | forecastqty | 0           |


  Scenario: app resume in cartsummary page
  
    Given a username <username> and password <password>
    When a user click login button it redirect to location page
    Then enter the location name
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click add button from chickencurrycut <product> product
    And check proceed option enable
    And click proceed button it redirect to cartsummary page
    And run app in background
    And change the staging advance inventory <productid> <qty> <forecastqty>
    And launch app
    And verify the popup displays
    
  Examples: Vertical
  | username    | 9710243651  |
  | password    | 123456      |
  | product     | chicken     |
  | productid   | 193         |
  | qty         | 0           |
  | forecastqty | 0           |

  Scenario: app resume in delivery page

    Given a username <username> and password <password>
    When a user click login button it redirect to location page
    Then enter the location name
    And when a user select location option it redirect to category page
    And click category product image chicken it redirect to tcuts product page
    And click add button <quantity> from chickencurrycut <product> product
    And check proceed option enable
    And click proceed button it redirect to cartsummary page
    And click checkout button it redirect to deliverysummary page
    And select time slot and delivery address <product>
    And run app in background
    And change the staging advance inventory <productid> <qty> <forecastqty>
    And launch app
    And when a user click continue button it redirect to payment page
    And select a cash on delivery option
    And when a user click place order button 
    And verify the popup displays
    
  Examples: Vertical
  | username    | 9710243651    |
  | password    | 123456        |
  | product     | chicken       |
  | quantity    | 2             |
  | productid   | 193           |
  | qty         | 0             |
  | forecastqty | 0             |