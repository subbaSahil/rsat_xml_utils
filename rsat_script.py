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
# Clicking navigation: Sales and marketing
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Sales and marketing']")
time.sleep(1)
# Clicking navigation: Sales returns
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Sales returns']")
time.sleep(1)
# Clicking navigation: All return orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All return orders']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: SalesTable_CustAccount
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'SalesTable_CustAccount')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]") ):
    #clicking inside grid: SalesTable_CustAccount
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'SalesTable_CustAccount')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'SalesTable_CustAccount')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'SalesTable_CustAccount')])[1]", "US-001")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Customer account')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Customer account')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Customer account')])[1]", "US-001")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SalesTable_CustAccount')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'SalesTable_CustAccount')]", "US-001")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]", "US-001")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
# Inputting into: SalesTable_ReturnReasonCodeId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'SalesTable_ReturnReasonCodeId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Return reason code')]") ):
    #clicking inside grid: SalesTable_ReturnReasonCodeId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'SalesTable_ReturnReasonCodeId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'SalesTable_ReturnReasonCodeId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'SalesTable_ReturnReasonCodeId')])[1]", "15")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Return reason code')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Return reason code')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Return reason code')])[1]", "15")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SalesTable_ReturnReasonCodeId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'SalesTable_ReturnReasonCodeId')]", "15")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Return reason code')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Return reason code')]", "15")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
# Inputting into: SalesTable_InventSiteId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'SalesTable_InventSiteId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Site')]") ):
    #clicking inside grid: SalesTable_InventSiteId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'SalesTable_InventSiteId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'SalesTable_InventSiteId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'SalesTable_InventSiteId')])[1]", "1")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Site')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]", "1")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SalesTable_InventSiteId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'SalesTable_InventSiteId')]", "1")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Site')]", "1")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: SalesTable_InventLocationId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'SalesTable_InventLocationId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]") ):
    #clicking inside grid: SalesTable_InventLocationId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'SalesTable_InventLocationId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'SalesTable_InventLocationId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'SalesTable_InventLocationId')])[1]", "11")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Warehouse')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]", "11")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SalesTable_InventLocationId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'SalesTable_InventLocationId')]", "11")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]", "11")
    Interactions.press_enter(driver, By.XPATH, "//body")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
# Inputting into: SalesLine_ItemIdGrid
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'SalesLine_ItemIdGrid')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
    #clicking inside grid: SalesLine_ItemIdGrid
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'SalesLine_ItemIdGrid')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'SalesLine_ItemIdGrid')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'SalesLine_ItemIdGrid')])[1]", "1000")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "1000")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SalesLine_ItemIdGrid')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'SalesLine_ItemIdGrid')]", "1000")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "1000")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Return_CostPrice')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Return cost price')]") ):
    #clicking inside grid: Return_CostPrice
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Return_CostPrice')])[1]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'Return_CostPrice')])[1]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Return_CostPrice')])[1]", "100.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Return cost price')])[1]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@aria-label,'Return cost price')])[1]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Return cost price')])[1]", "100.00")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Return_CostPrice')]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Return_CostPrice')]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Return_CostPrice')]", "100.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Return cost price')]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@aria-label,'Return cost price')]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Return cost price')]", "100.00")
    Interactions.press_enter(driver, By.XPATH, "//body")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
user_input = input('Enter the value for the hyperlink: ')
if Interactions.check_element_exist(driver, By.XPATH, "//div[contains(@data-dyn-savedtooltip,'"+user_input+"')]/preceding-sibling::label[text()='Sales order']"):
     Interactions.wait_and_click(driver, By.XPATH,  "//div[contains(@data-dyn-savedtooltip,'"+user_input+"')]/preceding-sibling::label[text()='Sales order']")
     Interactions.press_enter(driver, By.XPATH, "//div[contains(@data-dyn-savedtooltip,'"+user_input+"')]/preceding-sibling::label[text()='Sales order']")
elif Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@title,'"+user_input+"')]/preceding-sibling::label[text()='Sales order']"):
     Interactions.wait_and_click(driver, By.XPATH,  "//input[contains(@title,'"+user_input+"')]/preceding-sibling::label[text()='Sales order']")
     Interactions.press_enter(driver, By.XPATH, "//input[contains(@title,'"+user_input+"')]/preceding-sibling::label[text()='Sales order']")
Interactions.wait_and_click(driver, By.XPATH, "//li[contains(@data-dyn-controlname,'TabFinancialDimensionLine')]")
# Inputting into: DimensionEntryControlLine_DECValue_Department
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'DimensionEntryControlLine_DECValue_Department')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Department value')]") ):
    #clicking inside grid: DimensionEntryControlLine_DECValue_Department
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'DimensionEntryControlLine_DECValue_Department')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'DimensionEntryControlLine_DECValue_Department')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DimensionEntryControlLine_DECValue_Department')])[1]", "023")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Department value')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Department value')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Department value')])[1]", "023")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DimensionEntryControlLine_DECValue_Department')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'DimensionEntryControlLine_DECValue_Department')]", "023")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Department value')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Department value')]", "023")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Update']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Update']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Update line']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Update line']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='InventTransRegister']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='InventTransRegister']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Registration']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Registration']/ancestor::button")
# Inputting into: Fld3_1
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Fld3_1')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Disposition code')]") ):
    #clicking inside grid: Fld3_1
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Fld3_1')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Fld3_1')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Fld3_1')])[1]", "11")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Disposition code')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Disposition code')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Disposition code')])[1]", "11")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Fld3_1')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Fld3_1')]", "11")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Disposition code')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Disposition code')]", "11")
    Interactions.press_enter(driver, By.XPATH, "//body")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='AddRegistrationLinesButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='AddRegistrationLinesButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Add registration line']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Add registration line']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='ctrlUpdateButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='ctrlUpdateButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Confirm registration']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Confirm registration']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='buttonUpdatePackingSlip']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='buttonUpdatePackingSlip']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Post packing slip']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Post packing slip']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Ok']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Ok']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
user_input = input('Enter the value for the hyperlink: ')
if Interactions.check_element_exist(driver, By.XPATH, "//div[contains(@data-dyn-savedtooltip,'"+user_input+"')]/preceding-sibling::label[text()='Sales order']"):
     Interactions.wait_and_click(driver, By.XPATH,  "//div[contains(@data-dyn-savedtooltip,'"+user_input+"')]/preceding-sibling::label[text()='Sales order']")
     Interactions.press_enter(driver, By.XPATH, "//div[contains(@data-dyn-savedtooltip,'"+user_input+"')]/preceding-sibling::label[text()='Sales order']")
elif Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@title,'"+user_input+"')]/preceding-sibling::label[text()='Sales order']"):
     Interactions.wait_and_click(driver, By.XPATH,  "//input[contains(@title,'"+user_input+"')]/preceding-sibling::label[text()='Sales order']")
     Interactions.press_enter(driver, By.XPATH, "//input[contains(@title,'"+user_input+"')]/preceding-sibling::label[text()='Sales order']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='buttonUpdateInvoice']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='buttonUpdateInvoice']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Invoice']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Invoice']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Ok']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Ok']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='buttonJournalInvoice']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='buttonJournalInvoice']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Invoice']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Invoice']")
time.sleep(5)
print("test case passed")
driver.quit()