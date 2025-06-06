from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
user_input = None

save_line_items_without_errors = False

Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Inventory management
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Inventory management']")
time.sleep(1)
# Clicking navigation: Inbound orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Inbound orders']")
time.sleep(1)
# Clicking navigation: Transfer order
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Transfer order']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: LineViewHeader_InventLocationIdFrom
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LineViewHeader_InventLocationIdFrom')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'From warehouse')]") ):
    #clicking inside grid: LineViewHeader_InventLocationIdFrom
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LineViewHeader_InventLocationIdFrom')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LineViewHeader_InventLocationIdFrom')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LineViewHeader_InventLocationIdFrom')])[1]", "11")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'From warehouse')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'From warehouse')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'From warehouse')])[1]", "11")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LineViewHeader_InventLocationIdFrom')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LineViewHeader_InventLocationIdFrom')]", "11")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'From warehouse')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'From warehouse')]", "11")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
# Inputting into: LineViewHeader_InventLocationIdTo
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LineViewHeader_InventLocationIdTo')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'To warehouse')]") ):
    #clicking inside grid: LineViewHeader_InventLocationIdTo
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LineViewHeader_InventLocationIdTo')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LineViewHeader_InventLocationIdTo')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LineViewHeader_InventLocationIdTo')])[1]", "21")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'To warehouse')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'To warehouse')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'To warehouse')])[1]", "21")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LineViewHeader_InventLocationIdTo')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LineViewHeader_InventLocationIdTo')]", "21")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'To warehouse')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'To warehouse')]", "21")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
"Skipping grid selection due input in the ancestor"
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='CopyOfAddButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='CopyOfAddButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Add']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Add']")
"Skipping grid since it is deafault behavior of d365"
# Inputting into: InventTransferLine_ItemId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'InventTransferLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
    #clicking inside grid: InventTransferLine_ItemId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'InventTransferLine_ItemId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'InventTransferLine_ItemId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'InventTransferLine_ItemId')])[1]", "1000")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "1000")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventTransferLine_ItemId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InventTransferLine_ItemId')]", "1000")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "1000")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
"Skipping grid selection due input in the ancestor"
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Inventory']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Inventory']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Inventory']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Inventory']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='InventOnhand']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='InventOnhand']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='On-hand']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='On-hand']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='DialogCloseCommandButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='DialogCloseCommandButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Close']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Close']")
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'InventTransferLine_QtyTransfer')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Transfer quantity')]") ):
    #clicking inside grid: InventTransferLine_QtyTransfer
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'InventTransferLine_QtyTransfer')])[1]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'InventTransferLine_QtyTransfer')])[1]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'InventTransferLine_QtyTransfer')])[1]", "10.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Transfer quantity')])[1]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@aria-label,'Transfer quantity')])[1]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Transfer quantity')])[1]", "10.00")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventTransferLine_QtyTransfer')]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'InventTransferLine_QtyTransfer')]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InventTransferLine_QtyTransfer')]", "10.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Transfer quantity')]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@aria-label,'Transfer quantity')]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Transfer quantity')]", "10.00")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Clicking (default) on: ShipmentTab
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='ShipmentTab']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='ButtonInventTransferPick']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='ButtonInventTransferPick']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Generate picking list']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Generate picking list']")
"Skipping grid since it is deafault behavior of d365"
# Clicking combobox: InventTransferParmTable_pickUpdateQty
combox_box_to_click = None
if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='InventTransferParmTable_pickUpdateQty']/following-sibling::div"):
     combox_box_to_click = "//input[@name='InventTransferParmTable_pickUpdateQty']/following-sibling::div"
elif Interactions.check_element_exist(driver, By.XPATH, "//input[@aria-label='Update']/following-sibling::div"):
     combox_box_to_click = "//input[@aria-label='Update']/following-sibling::div"
Interactions.wait_and_click(driver, By.XPATH, combox_box_to_click)
if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_pickUpdateQty')]//li[@data-dyn-index='3']"):
     Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_pickUpdateQty')]//li[@data-dyn-index='3']")
elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id,'InventTransferParmTable_pickUpdateQty')]//li[3]"):
     Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@id,'InventTransferParmTable_pickUpdateQty')]//li[3]")
else:
     if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_pickUpdateQty')]"):
            cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_pickUpdateQty')]",By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_pickUpdateQty')]//li[@data-dyn-index='3']")
            if cliked_or_not == False:
                Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_pickUpdateQty')]",By.XPATH, "//ul[contains(@id,'InventTransferParmTable_pickUpdateQty')]//li[3]")
     elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id, 'InventTransferParmTable_pickUpdateQty')]"):
            cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'InventTransferParmTable_pickUpdateQty')]",By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_pickUpdateQty')]//li[@data-dyn-index='3']")
            if cliked_or_not == False:
                Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'InventTransferParmTable_pickUpdateQty')]",By.XPATH, "//ul[contains(@id,'InventTransferParmTable_pickUpdateQty')]//li[3]")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='buttonInventPickingListRegistrate']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='buttonInventPickingListRegistrate']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Picking list registration']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Picking list registration']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Functions']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Functions']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Functions']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Functions']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='WMSPickingRouteStart']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='WMSPickingRouteStart']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Start picking route']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Start picking route']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='UpdatesMenuButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='UpdatesMenuButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Updates']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Updates']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='PickAllButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='PickAllButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Update all']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Update all']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Clicking (default) on: ReceiveTab
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='ReceiveTab']")
# Clicking (default) on: ShipmentTab
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='ShipmentTab']")
# Refreshing the page
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedRefreshButton']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='ButtonInventTransferShip']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='ButtonInventTransferShip']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Ship transfer order']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Ship transfer order']")
"Skipping grid since it is deafault behavior of d365"
# Clicking combobox: InventTransferParmTable_ShipUpdateQty
combox_box_to_click = None
if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='InventTransferParmTable_ShipUpdateQty']/following-sibling::div"):
     combox_box_to_click = "//input[@name='InventTransferParmTable_ShipUpdateQty']/following-sibling::div"
elif Interactions.check_element_exist(driver, By.XPATH, "//input[@aria-label='Update']/following-sibling::div"):
     combox_box_to_click = "//input[@aria-label='Update']/following-sibling::div"
Interactions.wait_and_click(driver, By.XPATH, combox_box_to_click)
if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ShipUpdateQty')]//li[@data-dyn-index='4']"):
     Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ShipUpdateQty')]//li[@data-dyn-index='4']")
elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id,'InventTransferParmTable_ShipUpdateQty')]//li[4]"):
     Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@id,'InventTransferParmTable_ShipUpdateQty')]//li[4]")
else:
     if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ShipUpdateQty')]"):
            cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ShipUpdateQty')]",By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ShipUpdateQty')]//li[@data-dyn-index='4']")
            if cliked_or_not == False:
                Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ShipUpdateQty')]",By.XPATH, "//ul[contains(@id,'InventTransferParmTable_ShipUpdateQty')]//li[4]")
     elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id, 'InventTransferParmTable_ShipUpdateQty')]"):
            cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'InventTransferParmTable_ShipUpdateQty')]",By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ShipUpdateQty')]//li[@data-dyn-index='4']")
            if cliked_or_not == False:
                Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'InventTransferParmTable_ShipUpdateQty')]",By.XPATH, "//ul[contains(@id,'InventTransferParmTable_ShipUpdateQty')]//li[4]")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
# Clicking (default) on: ReceiveTab
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='ReceiveTab']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='ButtonInventTransferReceive']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='ButtonInventTransferReceive']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Receive']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Receive']")
"Skipping grid since it is deafault behavior of d365"
# Clicking combobox: InventTransferParmTable_ReceiveUpdateQty
combox_box_to_click = None
if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='InventTransferParmTable_ReceiveUpdateQty']/following-sibling::div"):
     combox_box_to_click = "//input[@name='InventTransferParmTable_ReceiveUpdateQty']/following-sibling::div"
elif Interactions.check_element_exist(driver, By.XPATH, "//input[@aria-label='Update']/following-sibling::div"):
     combox_box_to_click = "//input[@aria-label='Update']/following-sibling::div"
Interactions.wait_and_click(driver, By.XPATH, combox_box_to_click)
if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ReceiveUpdateQty')]//li[@data-dyn-index='2']"):
     Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ReceiveUpdateQty')]//li[@data-dyn-index='2']")
elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id,'InventTransferParmTable_ReceiveUpdateQty')]//li[2]"):
     Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@id,'InventTransferParmTable_ReceiveUpdateQty')]//li[2]")
else:
     if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ReceiveUpdateQty')]"):
            cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ReceiveUpdateQty')]",By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ReceiveUpdateQty')]//li[@data-dyn-index='2']")
            if cliked_or_not == False:
                Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ReceiveUpdateQty')]",By.XPATH, "//ul[contains(@id,'InventTransferParmTable_ReceiveUpdateQty')]//li[2]")
     elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id, 'InventTransferParmTable_ReceiveUpdateQty')]"):
            cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'InventTransferParmTable_ReceiveUpdateQty')]",By.XPATH, "//ul[contains(@aria-labelledby, 'InventTransferParmTable_ReceiveUpdateQty')]//li[@data-dyn-index='2']")
            if cliked_or_not == False:
                Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'InventTransferParmTable_ReceiveUpdateQty')]",By.XPATH, "//ul[contains(@id,'InventTransferParmTable_ReceiveUpdateQty')]//li[2]")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
# Refreshing the page
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedRefreshButton']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Inventory']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Inventory']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Inventory']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Inventory']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='InventOnhand']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='InventOnhand']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='On-hand']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='On-hand']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='DialogCloseCommandButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='DialogCloseCommandButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Close']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Close']")
time.sleep(5)
print("test case passed")
driver.quit()