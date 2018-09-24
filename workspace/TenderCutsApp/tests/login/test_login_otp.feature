Feature: check redirection to otp verification page
  verify by entering unexist user login via otp

  Scenario Outline: valid login otp

    Given a username <username>
    When a user click send otp
    Then verify it redirect to OTP page


    Examples:
      | username   |
      | 9710243651 | 
