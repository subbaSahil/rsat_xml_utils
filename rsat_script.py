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
# Clicking navigation: Dimensions
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Dimensions']")
time.sleep(1)
# Clicking navigation: Financial dimension sets
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Financial dimension sets']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: DetailAutoIdentification_Name
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'DetailAutoIdentification_Name')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Financial dimension set')]") ):
    #clicking inside grid: DetailAutoIdentification_Name
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'DetailAutoIdentification_Name')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'DetailAutoIdentification_Name')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DetailAutoIdentification_Name')])[1]", "Product")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Financial dimension set')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Financial dimension set')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Financial dimension set')])[1]", "Product")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DetailAutoIdentification_Name')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'DetailAutoIdentification_Name')]", "Product")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Financial dimension set')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Financial dimension set')]", "Product")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: DetailAutoIdentification_Description
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'DetailAutoIdentification_Description')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Name')]") ):
    #clicking inside grid: DetailAutoIdentification_Description
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'DetailAutoIdentification_Description')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'DetailAutoIdentification_Description')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DetailAutoIdentification_Description')])[1]", "Product")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Name')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]", "Product")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DetailAutoIdentification_Description')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'DetailAutoIdentification_Description')]", "Product")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Name')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Name')]", "Product")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Clicking button: GroupComposition_Panel_ViewAvailable
user_input = input("Press data to select: ")
Interactions.scroll_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='GroupComposition_Panel_ViewAvailable//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='GroupComposition_Panel_Add']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='GroupComposition_Panel_Add']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Add']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Add']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
time.sleep(5)
print("test case passed")
driver.quit()