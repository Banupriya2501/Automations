Feature: managing address
  my account managing address

  Background:
    Given a username <username> and password <password>
    And when a user click login button it redirect to location page
    And enter the location name
    And when a user select location option it redirect to category page
    And click my accountpage tab

  Scenario: managing address

    Given when user click managing address option
    When default address option visible then click defaulf addres and verify toast message
    Then when delete option visible then click delete button
    Then verify toast message <toastmessage>

  Examples:
  | username    | password | toastmessage    |
  |  9710243651 |  123456  | Address Deleted |


  Scenario: managing profile

    Given when user click managing profile option
    When edit option visible then enter new name
    Then verify toast message <toastmessage>
    And when edit option visible for email then edit email address
    Then verify toast message <toastmessage>

  Examples:
  | username    | password | toastmessage                  |
  |  9710243651 |  123456  | Profile Updated Successfully. |


  Scenario: change password

    Given when user click managing profile option
    When edit option visible for password click the option
    Then enter new password and conform password <passwordd>
    And click change password button
    Then verify toast message <toastmessage>

  Examples:
  | username    | password | passwordd  | toastmessage                    |
  |  9710243651 |  123456  | 123456     | Password changed Successfully.  |


  Scenario: Refer a friend
    Given a refer a friend link
    When on cliking link it redirect to invite friend and earn page
    Then verify whats app link displays

  Examples:
  | username    | password | 
  |  9710243651 |  123456  | 

  Scenario: manage payment
    Given a managepayment link
    Then verify it displays card detail and delete button

  Examples:
  | username    | password |
  |  9710243651 |  123456  |

  Scenario: Edit and cancel address
    Given when user click managing address option
    When default address option visible then click defaulf addres and verify toast message
    Then when edit option visible then click edit button
    Then enter the details flatno<flatno>
    Then click save button
    Then click on backward navigation
    Then click on cancel button
    Then check address row
  
  Examples:
  | username    | password | flatno |
  | 9710243651  |  123456  | 1223   |

  Scenario: Edit and save address
    Given when user click managing address option
    When default address option visible then click defaulf addres and verify toast message
    Then when edit option visible then click edit button
    Then enter the details flatno<flatno>
    Then click save button
    Then click save address button
    Then verify toast msg <toastmsg>

  Examples:
  | username   | password | flatno | toastmsg       |
  | 9710243651 | 123456   | 33     | Address Edited |