Feature: check toast message unexist user login via otp
  verify by entering unexist user login via otp

  Scenario Outline: invalid login otp

    Given a username <username>
    When a user click send otp
    Then verify toast message <toastmessage>


    Examples:
      | username   | toastmessage        |
      | 1111111111 | User doesn't exists |


    
