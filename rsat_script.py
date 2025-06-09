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
# Clicking navigation: General ledger
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='General ledger']")
time.sleep(1)
# Clicking navigation: Chart of accounts
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Chart of accounts']")
time.sleep(1)
# Clicking navigation: Accounts
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts']")
time.sleep(1)
# Clicking navigation: Main accounts
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Main accounts']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='TreeNext']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='TreeNext']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Next']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Next']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='TreeNext']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='TreeNext']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Next']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Next']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='TreeNext']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='TreeNext']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Next']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Next']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='TreeNext']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='TreeNext']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Next']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Next']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='TreeNext']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='TreeNext']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Next']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Next']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='TreeNext']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='TreeNext']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Next']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Next']")
# Clicking on last path: 601300, Advertising Expense
Interactions.wait_and_click(driver, By.XPATH, "//li[@aria-label='601300, Advertising Expense']/div/button[@type='button']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='AddLegalEntityOverride']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='AddLegalEntityOverride']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Add']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Add']")
# Inputting into: DataAreaIdQuickFilter
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DataAreaIdQuickFilter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'DataAreaIdQuickFilter')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "DEMF")
    Interactions.press_enter(driver, By.XPATH, locator)
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "DEMF")
    Interactions.press_enter(driver, By.XPATH, locator)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SelectCompanyInfoBtn']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SelectCompanyInfoBtn']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Add']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Add']")
"Skipping grid since it is deafault behavior of d365"
# Clicking checkbox: MainAccountLegalEntity_AutoAllocate
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Allocation')]/following-sibling::div/span[1]")):
    if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//label[contains(text(),'Allocation')]/following-sibling::div/span[1]", True) == False:
         Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Allocation')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'MainAccountLegalEntity_AutoAllocate') and (@class='toggle-box' or @class='checkBox')]")):
    if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//span[contains(@id, 'MainAccountLegalEntity_AutoAllocate') and (@class='toggle-box' or @class='checkBox')]", True) == False:
         Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'MainAccountLegalEntity_AutoAllocate') and (@class='toggle-box' or @class='checkBox')]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@aria-label='Allocation']//span")):
    if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//div[@aria-label='Allocation']//span", True) == False:
         Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Allocation']//span")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SetupAllocations']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SetupAllocations']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Allocation terms']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Allocation terms']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerAllocation_ValueDetails')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Percent')]") ):
    #clicking inside grid: LedgerAllocation_ValueDetails
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerAllocation_ValueDetails')])[1]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'LedgerAllocation_ValueDetails')])[1]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerAllocation_ValueDetails')])[1]", "20.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Percent')])[1]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@aria-label,'Percent')])[1]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Percent')])[1]", "20.00")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerAllocation_ValueDetails')]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerAllocation_ValueDetails')]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerAllocation_ValueDetails')]", "20.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Percent')]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@aria-label,'Percent')]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Percent')]", "20.00")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: DimensionEntryControlFrom_DECValue_BusinessUnit
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'DimensionEntryControlFrom_DECValue_BusinessUnit')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'BusinessUnit value')]") ):
    #clicking inside grid: DimensionEntryControlFrom_DECValue_BusinessUnit
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'DimensionEntryControlFrom_DECValue_BusinessUnit')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'DimensionEntryControlFrom_DECValue_BusinessUnit')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DimensionEntryControlFrom_DECValue_BusinessUnit')])[1]", "001")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'BusinessUnit value')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'BusinessUnit value')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'BusinessUnit value')])[1]", "001")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DimensionEntryControlFrom_DECValue_BusinessUnit')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'DimensionEntryControlFrom_DECValue_BusinessUnit')]", "001")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'BusinessUnit value')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'BusinessUnit value')]", "001")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
time.sleep(5)
print("test case passed")
driver.quit()