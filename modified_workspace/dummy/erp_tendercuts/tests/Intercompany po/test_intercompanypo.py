import pages
import time
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('test_intercompanypo.feature', 'intercompany po')
def test_intercompanyporeceiving():
    """PlacingOrder_cod."""
    pass

@pytest.fixture()
def cache():
    return {}

@given('a username<usernameRetail> and password<password> click submit button')
def a_username_username_and_password_click_submit_button(driver,usernameRetail,password):
    """a username <username> and <password> click submit button."""
    loginpage=pages.Loginpage(driver)
    loginpage.enter_logindetails(usernameRetail,password)

@when('click sales menu and click sales <projectionsheet> projection')
def sales_projection(driver,projectionsheet):
    menu=pages.Menupage(driver)
    time.sleep(1)
    menu.humberger_menu()
    menu.purchase_menu()
    purchasepage=pages.Purchasepage(driver)
    purchasepage.sub_menu_autoindent()
    purchasepage.projection()
    purchasepage.import_projection()
    purchasepage.loadfile(projectionsheet)
    purchasepage.test_import()
    purchasepage.import_file()

@then('update <indentsheet> indent <indentdate>')
def indent(driver,cache,indentsheet,indentdate):
    purchasepage=pages.Purchasepage(driver)
    purchasepage.sub_menu_autoindent()
    purchasepage.indent()
    purchasepage.import_projection()
    purchasepage.loadfile_indent(indentsheet)
    purchasepage.test_import()
    purchasepage.import_file()
    purchasepage.projection_to_done()
    purchasepage.indent_date()
    time.sleep(0.2)
    purchasepage.action()
    purchasepage.generate_indent()
    po_number=purchasepage.getponumber(indentdate)
    cache['po_number'] = po_number


@then('select the po and change the vendor')
def autoindent(cache,driver):
    purchasepage=pages.Purchasepage(driver)
    purchasepage.sub_menu_autoindent()
    purchasepage.auto_indent()
    purchasepage.pending_record()
    po_number = cache['po_number']
    purchasepage.check_box(po_number)
    purchasepage.change_vendor()
    purchasepage.action()
    purchasepage.conform_order()
    time.sleep(1)
    so_number=purchasepage.get_so()
    cache['so_number'] = so_number

@then('login to purchase manager<usernamepurchase><password>')
def purchase_manager(driver,usernamepurchase,password):
    purchasemanager=pages.Purchasemanager(driver)
    purchasemanager.login_purchasemanager(usernamepurchase,password)
    menu=pages.Menupage(driver)
    menu.humberger_menu()
    menu.purchase_menu()
    time.sleep(0.5)
    purchasepage=pages.Purchasepage(driver)
    purchasepage.sub_menu_purchase()
    purchasepage.sub_menu_purchaseorder()

@then('create po for external vendor and receive the product<scannedbill>')
def external_vendor(driver,scannedbill):
    purchasemanager=pages.Purchasemanager(driver)
    purchasemanager.create()
    purchasemanager.vendor()
    purchasemanager.add_product()
    purchasemanager.save()
    time.sleep(0.5)
    purchasemanager.confirmorder()
    time.sleep(1.5)
    vendor_po=purchasemanager.get_po()
    purchasemanager.received_product()
    purchasemanager.vendor_bill()
    purchasemanager.update_screenshot(scannedbill)
    purchasemanager.click_attach()
    # purchasemanager.receive_Products()
    time.sleep(1.5)
    purchasemanager.edit()
    time.sleep(0.5)

    purchasemanager.done_quantity()
    time.sleep(0.5)

    purchasemanager.save()
    time.sleep(0.5)
    purchasemanager.validate()
    
@then('check the po and so and put in packs')
def packs(cache,driver):
    salespage=pages.Salespage(driver)
    so_number=cache['so_number']
    menu=pages.Menupage(driver)
    menu.humberger_menu()
    menu.sales_menu()
    salespage.click_so(so_number) 
    salespage.confirm_sale()
    time.sleep(1.5)
    salespage.delivery()
    time.sleep(0.5)
    salespage.edit()
    time.sleep(0.5)
    salespage.plu_code()
    time.sleep(1)
    salespage.put_in_pack()
    time.sleep(0.5)
    salespage.box_number()
    time.sleep(0.5)
    salespage.confirm()
    time.sleep(0.5)
    salespage.save()
    time.sleep(0.5)
    salespage.validate()
    time.sleep(15)
    salespage.switch_purchase_store_login()

@then('from retail manager receive the box<scannedbill>')
def retail_manager(cache,driver,scannedbill,usernameRetail,password):
    loginpage=pages.Loginpage(driver)
    loginpage.enter_logindetails(usernameRetail,password)
    menu=pages.Menupage(driver)
    menu.humberger_menu()
    menu.purchase_menu()
    purchasepage=pages.Purchasepage(driver)
    purchasepage.sub_menu_purchase()
    purchasepage.sub_menu_purchaseorder()
    time.sleep(1)
    purchasepage.filter_remove()
    po_number = cache['po_number']
    time.sleep(0.5)
    purchasepage.check_box(po_number)
    purchasepage.receive_product()
    purchasepage.vendor_bill(scannedbill)
    purchasepage.receive_product_bill()
    purchasepage.scan_package()
    purchasepage.barcode()
    purchasepage.confirm()
    time.sleep(10)

@then('verify the inventory<productname1><productname2>')
def inventory(driver,productname1,productname2):
    menu=pages.Menupage(driver)
    time.sleep(5)
    menu.humberger_menu()
    menu.inventory_menu()
    inventory_verify=pages.Inventorypage(driver)
    inventory_verify.reporting()
    inventory_verify.inventory()
    inventory_verify.current_inventory()
    time.sleep(0.8)
    inventory_verify.filter()
    inventory_verify.click_filter()
    inventory_verify.filter_advance(productname1)
    inventory_verify.click_product(productname1)
    inventory_verify.quantity()
    time.sleep(0.5)
    inventory_verify.reporting()
    inventory_verify.inventory()
    inventory_verify.current_inventory()
    time.sleep(0.8)
    inventory_verify.group_by()
    inventory_verify.filter()
    inventory_verify.click_filter()
    inventory_verify.filter_advance(productname2)
    inventory_verify.click_product(productname2)
    inventory_verify.quantity()
