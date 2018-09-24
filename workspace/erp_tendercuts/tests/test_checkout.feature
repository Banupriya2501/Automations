Feature: erp tendercuts

  Scenario Outline: erp
    Given a username<username> and password<password> click submit button
    When click sales menu and click sales <projectionsheet> projection
    Then update <indentsheet> indent <indentdate>
    And select auto indent po and receive the product
    And login to thoraipakkam store and receive the product<storedate>
    And check the inventory from adminstrator<username><password>

    Examples: Vertical
    |username           | varun@tendercuts.in                                      |
    |password           |  admin                                                   |
    |projectionsheet    | /home/banupriya/Documents/Projectionsheet/projection.xlsx|
    |indentsheet        | /home/banupriya/Documents/Projectionsheet/indent.xlsx    |
    |indentdate         | 09/25/2018                                               |
    |storedate          | 25 Sep                                                   |