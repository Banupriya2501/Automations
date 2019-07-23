Feature: intercompanypo receiving

  Scenario Outline: intercompany po
    Given a username<usernameRetail> and password<password> click submit button
    When click sales menu and click sales <projectionsheet> projection
    Then update <indentsheet> indent <indentdate>
    And select the po and change the vendor
    And login to purchase manager<usernamepurchase><password>
    And create po for external vendor and receive the product<scannedbill>
    And check the po and so and put in packs
    And from retail manager receive the box<scannedbill>
    And verify the inventory<productname1><productname2>

    Examples: Vertical
    |usernameRetail          | kumaran@tendercuts.in |
    |usernamepurchase        | purchase@tendercuts.in|
    |password                | test                  |
    |projectionsheet|/home/banupriya/workspace/erp_tendercuts/sheet/splitprojection.xlsx|
    |indentsheet    |/home/banupriya/workspace/erp_tendercuts/sheet/splitindent.xlsx|
    |scannedbill    |/home/banupriya/workspace/erp_tendercuts/sheet/scanpackage.png |
    |indentdate         | 10/12/2018 |
    |productname1       | RM_SF_KALAVAN |
    |productname2       | RM_SF_SEER    |