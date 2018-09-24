import pages
import time
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('test_checkout.feature', 'envee')
def test_login():
    """PlacingOrder_cod."""
    pass

@given('a username and password click submit button')
def a_username_username_and_password_click_submit_button(driver):
    """a username <username> and <password> click submit button."""
    loginpage=pages.Loginpage(driver)
    loginpage.enter_logindetails()

    manufacture=pages.Manufacturepage(driver)
    manufacture.humbergermenu()
    manufacture.manufacture_app()
    manufacture.create()
    manufacture.product()
    manufacture.quantitytoproduce()
    manufacture.save()
    manufacture.create_workspace()
    manufacture.workspace()
    manufacture.package()
    manufacture.startworking()
    manufacture.edit()
    manufacture.totaltield()
    manufacture.lot_servial()
    manufacture.barcode()
    manufacture.enter_weight()
    
    manufacture.save_product()
    manufacture.done()
    manufacture.clickmo()
    manufacture.click_workorder()
    manufacture.click_package2()
    manufacture.start_working()
    manufacture.edit()
    manufacture.barcode()
    manufacture.wight()
    manufacture.save1()
    manufacture.done()
    manufacture.manufacturing_order()
    manufacture.link_one()
    manufacture.mark_as_done()






    inventoryadjustment=pages.InventroyAdjustmentpage(driver)
    inventoryadjustment.inventory_adjustment()


@when('on clicking purchase app')
def purchase(driver):
    purchase_order=pages.Purchasepage(driver)
    purchase_order.humberger_menu()
    purchase_order.purchase_app()
    # purchase_order.change_vendor()
    
@then('add product')
def add(driver):
    purchase_order=pages.Purchasepage(driver)
    purchase_order.create()
    purchase_order.vendor_selection()
    purchase_order.company_selection()
    # purchase_order.add_item()
    purchase_order.add_product()
    # purchase_order.change_qunatity()
    purchase_order.save()
    purchase_order.confirmorder()
    purchase_order.get_po()
  

@then('Receive the product by enter the vendor bill')
def add2(driver):
    purchase_order=pages.Purchasepage(driver)
    purchase_order.received_product()
    purchase_order.vendor_bill()
    purchase_order.update_screenshot()
    purchase_order.click_attach()
    purchase_order.edit()
    purchase_order.barcode_plu()
    # purchase_order.weight()
    # purchase_order.enter_weight()
   
@then('validate by receiving the product')
def add3(driver):
    purchase_order=pages.Purchasepage(driver)
    purchase_order.validate()
    purchase_order.purchase_tab()
    purchase_order.purchase_order()
    purchase_order.click_po()


@then('verify the inventory updated in inventory app')
def add4(driver):
    inventorypage=pages.Inventorypage(driver)
    inventorypage.humbergermenu()
    inventorypage.inventory()
    inventorypage.report()
    inventorypage.inventorymenu()
    inventorypage.currentdate()
    inventorypage.close()
    inventorypage.location()
    inventorypage.whstock()
    inventorypage.quantity_verification()

@then('sale the product in pos adayar')
def pos_sale(driver):
    pospage=pages.Pointofsalepage(driver)
    pospage.humberger_menu()
    # pospage.pos_app()
    # pospage.new_session()
    # pospage.open_session()
    # pospage.continue_selling()
    # pospage.product_selection()
    # pospage.payment()
    # pospage.payment_selection()
    # pospage.number_pad()
    # pospage.validate()
    # pospage.close()
    # pospage.confirm()
    # pospage.close_adayar()
    # pospage.end_of_session()
    # pospage.validate_close()
    # pospage.order_menu()
    # pospage.order_option()