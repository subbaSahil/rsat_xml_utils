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

locator = ""

filter_manager_cloumn_last_opened = ""
filter_manager_dropdown_item_index = 1

column_to_open = ""
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

# Clicking (default) on: WHS
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='WHS']")
# Clicking (default) on: MenuItemButton
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='MenuItemButton']")
# Inputting into: SupplyDemandLPWFilter
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SupplyDemandLPWFilter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'SupplyDemandLPWFilter')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Supply and demand filter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Supply and demand filter')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "")
# Inputting into: InventSiteIdFilter
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventSiteIdFilter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'InventSiteIdFilter')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "2")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "2")
# Inputting into: InventLocationIdFilter
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventLocationIdFilter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'InventLocationIdFilter')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "11")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "11")
# ❌ Locator not found for: GridInventLocation (Type: grid)
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'ShipDateFilter')]")):
    Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Ship date')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'ShipDateFilter')]", "05/13/2025")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Ship date')]")):
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Ship date')]", "05/13/2025")
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'ReceiptDateFilter')]")):
    Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Receipt date')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'ReceiptDateFilter')]", "05/20/2025")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Receipt date')]")):
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Receipt date')]", "05/20/2025")
# Clicking (default) on: InventLines
Interactions.wait_and_click(driver, By.XPATH, "//li[contains(@data-dyn-controlname,'InventLines')]")
# Clicking (default) on: SalesLines
Interactions.wait_and_click(driver, By.XPATH, "//li[contains(@data-dyn-controlname,'SalesLines')]")
# Clicking (default) on: UnassignedShipments
Interactions.wait_and_click(driver, By.XPATH, "//li[contains(@data-dyn-controlname,'UnassignedShipments')]")
# Inputting into: LoadLPWFilter
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LoadLPWFilter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'LoadLPWFilter')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Load filter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Load filter')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "")
# ❌ Locator not found for: LoadGrid (Type: grid)
# Clicking (default) on: Actions
Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Actions']")
# Clicking (default) on: change
Interactions.wait_and_click(driver, By.XPATH, "//button[@name='change']")
# Inputting into: WHSUserId
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'WHSUserId')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'WHSUserId')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "25")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'User ID')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'User ID')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "25")
# ❌ Locator not found for: WHSWorkPriority (Type: integer)
# Clicking button: OK
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
# Inputting into: FinalLocationId
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'FinalLocationId')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'FinalLocationId')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "BAYDOOR")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Final shipping location')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Final shipping location')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "BAYDOOR")
# Clicking button: OK
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
# Clicking button: SystemDefinedSaveButton
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
# Clicking (default) on: SupplyDemandActionPane
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='SupplyDemandActionPane']")
# Clicking (default) on: AddToNewLoad
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='AddToNewLoad']")
# Inputting into: Fld1_1
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Fld1_1')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'Fld1_1')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "20' Container")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Load template ID')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Load template ID')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "20' Container")
# Clicking button: OkButton
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")
# Clicking (default) on: FiltersActionPane
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='FiltersActionPane']")
# Clicking (default) on: ButtonSetDefault
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='ButtonSetDefault']")
# Clicking (default) on: ShipReceive
Interactions.wait_and_click(driver, By.XPATH, "//button[@name='ShipReceive']")
# Clicking (default) on: btnReverseShipConfirm
Interactions.wait_and_click(driver, By.XPATH, "//button[@name='btnReverseShipConfirm']")
# ❌ Locator not found for: LoadGrid (Type: grid)
# Clicking (default) on: ShipReceive
Interactions.wait_and_click(driver, By.XPATH, "//button[@name='ShipReceive']")
# Clicking (default) on: WHSPackStructureCrossDockCreate
Interactions.wait_and_click(driver, By.XPATH, "//button[@name='WHSPackStructureCrossDockCreate']")
# Inputting into: Fld4_1
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Fld4_1')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'Fld4_1')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "AIFBatch")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Batch group')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Batch group')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "AIFBatch")
# Clicking checkbox: Fld2_1
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Batch processing')]/following-sibling::div/span[1]")):
    Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Batch processing')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'Fld2_1') and (@class='toggle-box' or @class='checkBox')]")):
    Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'Fld2_1') and (@class='toggle-box' or @class='checkBox')]")
# Clicking checkbox: Fld6_1
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Critical Job')]/following-sibling::div/span[1]")):
    Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Critical Job')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'Fld6_1') and (@class='toggle-box' or @class='checkBox')]")):
    Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'Fld6_1') and (@class='toggle-box' or @class='checkBox')]")
# Clicking checkbox: Fld5_1
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Private')]/following-sibling::div/span[1]")):
    Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Private')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'Fld5_1') and (@class='toggle-box' or @class='checkBox')]")):
    Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'Fld5_1') and (@class='toggle-box' or @class='checkBox')]")
# Clicking button: CommandButton
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButton']")
time.sleep(5)
print("test case passed")
driver.quit()