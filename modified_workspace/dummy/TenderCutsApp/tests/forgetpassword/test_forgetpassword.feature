Feature: check toast message for forgetpassword
  verify by entering invalid phone number and check alert

  Scenario: forgetpassword alert
    Given username
    When a user click forgetpassword link and enter username<username>
    Then verify toast message <toastmessage>

  Examples:
  | username   | toastmessage        |
  | 1111111111 | User doesn't exists |