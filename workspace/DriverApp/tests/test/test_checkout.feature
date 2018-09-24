Feature: Assign the order and complete the order

  Scenario Outline: assign one order and complete it
    Given driverapp user <username> and <password> click submit button
    When click store
    Then click online
    And enter orderid and search
    And assign the order
    And enter the barcode and assignorder
    And complete the order

    Examples:
      | username   | password |
      | 8754442380 | 123456   |