Feature: erp tendercuts

  Scenario Outline: admin flow to receive inventory from thoraipakkam
    Given a username<username> and password<password> click submit button
    When click sales menu and click sales <projectionsheet> projection
    Then update <indentsheet> indent <indentdate>
    And select auto indent po and receive the product
    And login to thoraipakkam store and receive the product<storedate><scannedbill>
    And check the inventory from adminstrator<username><password>

    Examples: Vertical
    |username           | varun@tendercuts.in                                      |
    |password           |  admin                                                   |
    |projectionsheet    | /home/banupriya/workspace/erp_tendercuts/sheet/projection.xlsx|
    |indentsheet        | /home/banupriya/workspace/erp_tendercuts/sheet/indent.xlsx  |
    |scannedbill        | /home/banupriya/workspace/erp_tendercuts/sheet/scanpackage.png  |
    |indentdate         | 10/13/2018                                               |
    |storedate          | 13 Oct                                                   |