import pages
import time
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('test_admin_thoraipakkam.feature', 'admin flow to receive inventory from thoraipakkam')
def test_admin_flow():
    """Upload projection and receive from thoraipakkam and check inventory"""
    pass

@pytest.fixture()
def cache():
    return {}

@given('a username<username> and password<password> click submit button')
def a_username_username_and_password_click_submit_button(driver,username,password):
    """a username <username> and <password> click submit button."""
    loginpage=pages.Loginpage(driver)
    loginpage.enter_logindetails(username,password)

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


@then('select auto indent po and receive the product')
def autoindent(cache,driver):
    purchasepage=pages.Purchasepage(driver)
    purchasepage.sub_menu_autoindent()
    purchasepage.auto_indent()
    purchasepage.pending_record()
    po_number = cache['po_number']
    purchasepage.check_box(po_number)
    purchasepage.action()
    purchasepage.conform_order()

@then('login to thoraipakkam store and receive the product<storedate><scannedbill>')
def thoraipakkam(cache,driver,storedate,scannedbill):
    thoraipakkam_store=pages.Thoraipakkampage(driver)
    thoraipakkam_store.switch_to_thoraipakkam()
    thoraipakkam_store.purchase_order(storedate)
    po_number = cache['po_number']
    thoraipakkam_store.click_po(po_number)
    thoraipakkam_store.receive_product()
    thoraipakkam_store.vendor_bill(scannedbill)
    thoraipakkam_store.receive_product_bill()
    time.sleep(0.5)
    thoraipakkam_store.edit()
    time.sleep(0.5)
    thoraipakkam_store.zero()
    time.sleep(0.5)
    thoraipakkam_store.save()
    time.sleep(0.5)
    thoraipakkam_store.validate()

@then('check the inventory from adminstrator<username><password>')
def inventory_check(driver,username,password):
    inventory_verify=pages.Inventorypage(driver)
    inventory_verify.switch_to_adminstrator()
    loginpage=pages.Loginpage(driver)
    loginpage.enter_logindetails(username,password)
    menu=pages.Menupage(driver)
    time.sleep(1)
    menu.humberger_menu()
    menu.inventory_menu()
    inventory_verify.reporting()
    inventory_verify.inventory()
    inventory_verify.current_inventory()
    time.sleep(0.8)
    inventory_verify.filter()
    inventory_verify.click_filter()
    inventory_verify.click_filter_advance()
    inventory_verify.select_product()
    inventory_verify.quantity()

