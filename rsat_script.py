from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import login
import Interactions
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)

login.login(driver)
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
time.sleep(1)

# Clicking navigation: Purchase orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
time.sleep(1)

# Clicking navigation: All purchase orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
time.sleep(1)

# Clicking button: SystemDefinedNewButton
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
# Inputting into: PurchTable_OrderAccount
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]")):
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]", "1001")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]")):
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]", "1001")
# Clicking button: OK
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
# Clicking (default) on: Receive
Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='Receive']")
# Clicking (default) on: LineSpec
Interactions.wait_and_click(driver, By.XPATH, "//*[contains(@data-dyn-controlname, 'LineSpec')]")
# Inputting into: PurchLine_ItemId
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]")):
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]", "")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "")
# Inputting into: InventoryDimensionsGrid_InventSiteId
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')]")):
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')]", "2")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")):
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Site')]", "2")
# Inputting into: InventoryDimensionsGrid_InventLocationId
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]")):
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]", "21")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")):
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]", "21")
# Clicking (default) on: GridInventLocation
Interactions.wait_and_click(driver, By.XPATH, "//*[contains(@data-dyn-controlname, 'GridInventLocation')]")
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]")):
    Interactions.clearInputField(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]", "100.00")
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]", "100.00")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]")):
    Interactions.clearInputField(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]", "100.00")
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]", "100.00")
# Clicking button: SystemDefinedSaveButton
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
# Clicking (default) on: Purchase
Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='Purchase']")
# Clicking (default) on: buttonConfirm
Interactions.wait_and_click(driver, By.XPATH, "//*[contains(@data-dyn-controlname, 'buttonConfirm')]")
# Clicking (default) on: LineSpec
Interactions.wait_and_click(driver, By.XPATH, "//*[contains(@data-dyn-controlname, 'LineSpec')]")
# Clicking (default) on: Receive
Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='Receive']")
# Clicking (default) on: buttonUpdatePackingSlip
Interactions.wait_and_click(driver, By.XPATH, "//*[contains(@data-dyn-controlname, 'buttonUpdatePackingSlip')]")
# Clicking (default) on: gridParmTable
Interactions.wait_and_click(driver, By.XPATH, "//*[contains(@data-dyn-controlname, 'gridParmTable')]")
# Inputting into: PurchParmTable_Num
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]")):
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]", "PR-0002")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Product receipt')]")):
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Product receipt')]", "PR-0002")
# Clicking button: OK
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
# Clicking (default) on: buttonJournalPackingSlip
Interactions.wait_and_click(driver, By.XPATH, "//*[contains(@data-dyn-controlname, 'buttonJournalPackingSlip')]")
# Clicking (default) on: Invoice
Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='Invoice']")
# Clicking (default) on: buttonUpdateInvoice
Interactions.wait_and_click(driver, By.XPATH, "//*[contains(@data-dyn-controlname, 'buttonUpdateInvoice')]")
# Inputting into: PurchParmTable_Num
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]")):
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchParmTable_Num')]", "INV-0002")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Number')]")):
    Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Number')]", "INV-0002")
# Clicking button: SystemDefinedSaveButton
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
# Clicking (default) on: UpdateMatchStatus
Interactions.wait_and_click(driver, By.XPATH, "//*[contains(@data-dyn-controlname, 'UpdateMatchStatus')]")
# Clicking (default) on: OK
Interactions.wait_and_click(driver, By.XPATH, "//*[contains(@data-dyn-controlname, 'OK')]")
time.sleep(5)
print("test case passed")
driver.quit()