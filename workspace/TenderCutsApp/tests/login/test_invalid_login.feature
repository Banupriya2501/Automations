Feature: check toast message
  verify by entering valid username and invalid password

  Scenario Outline: invalid password alert

    Given a username <username> and password <password>
    When a user click login button
    Then verify toast message <toastmessage>


    Examples:
      | username   | password | toastmessage           |
      | 9710243651 | 123478   | Invalid Phone/Password |


    
