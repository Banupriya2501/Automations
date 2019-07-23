Feature: Signup
  signup new user and verify it redirect to otp verification page

  Scenario: signup
    Given a signup link
    When enter the details <name> ,<email>, <phone>, <password> and <conformpassword>
    Then click signup button
    And verify it redirect to OTP page

  Examples:
  | name    | email           | phone      | password | conformpassword  |
  | npriya  | 1w86@gmail.com  | 9999688882 | 123456   | 123456           |