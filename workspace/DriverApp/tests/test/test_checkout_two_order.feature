Feature: Assign the order and complete the order

  Scenario Outline: assign two order and complete it
    Given a username <username> and <password> click submit button
    When click store
    Then click online
    And enter orderid and search
    And donebutton
    And assign order and complete the order

    Examples:
      | username   | password |
      | 8754442380 | 123456   | 