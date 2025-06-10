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
# Clicking navigation: Main account categories
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Main account categories']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: LedgerAccountCategory_AccountCategory
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerAccountCategory_AccountCategory')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Main account category')]") ):
    #clicking inside grid: LedgerAccountCategory_AccountCategory
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerAccountCategory_AccountCategory')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerAccountCategory_AccountCategory')]")).perform()
          Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerAccountCategory_AccountCategory')])[1]", "win")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Main account category')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Main account category')]")).perform()
          Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Main account category')])[1]", "win")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerAccountCategory_AccountCategory')]")):
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerAccountCategory_AccountCategory')]", "win")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Main account category')]")):
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Main account category')]", "win")
Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: LedgerAccountCategory_Description
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerAccountCategory_Description')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Description')]") ):
    #clicking inside grid: LedgerAccountCategory_Description
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerAccountCategory_Description')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerAccountCategory_Description')]")).perform()
          Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerAccountCategory_Description')])[1]", "win")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Description')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Description')]")).perform()
          Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Description')])[1]", "win")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerAccountCategory_Description')]")):
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerAccountCategory_Description')]", "win")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Description')]")):
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Description')]", "win")
Interactions.press_enter(driver, By.XPATH, "//body")
# Clicking combobox: LedgerAccountCategory_AccountType
combox_box_to_click = None
if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='LedgerAccountCategory_AccountType']/following-sibling::div"):
     combox_box_to_click = "//input[@name='LedgerAccountCategory_AccountType']/following-sibling::div"
elif Interactions.check_element_exist(driver, By.XPATH, "//input[@aria-label='Main account type']/following-sibling::div"):
     combox_box_to_click = "//input[@aria-label='Main account type']/following-sibling::div"
elif Interactions.check_element_exist(driver, By.XPATH, "//input[@name='LedgerAccountCategory_AccountType']/parent::div/following-sibling::div/div"):
     combox_box_to_click = "//input[@name='LedgerAccountCategory_AccountType']/parent::div/following-sibling::div/div"
Interactions.wait_and_click(driver, By.XPATH, combox_box_to_click)
if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='3']"):
     Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='3']")
elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[3]"):
     Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[3]")
else:
     if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]"):
            cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='3']")
            if cliked_or_not == False:
                Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[3]")
     elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]"):
            cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@aria-labelledby, 'LedgerAccountCategory_AccountType')]//li[@data-dyn-index='3']")
            if cliked_or_not == False:
                Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'LedgerAccountCategory_AccountType')]",By.XPATH, "//ul[contains(@id,'LedgerAccountCategory_AccountType')]//li[3]")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LinkMainAccounts']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LinkMainAccounts']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Link main accounts']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Link main accounts']")
# Clicking checkbox: Linked
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Linked')]/following-sibling::div/span[1]")):
    if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//label[contains(text(),'Linked')]/following-sibling::div/span[1]", True) == False:
         Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Linked')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'Linked') and (@class='toggle-box' or @class='checkBox')]")):
    if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//span[contains(@id, 'Linked') and (@class='toggle-box' or @class='checkBox')]", True) == False:
         Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'Linked') and (@class='toggle-box' or @class='checkBox')]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@aria-label='Linked']//span")):
    if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//div[@aria-label='Linked']//span", True) == False:
         Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Linked']//span")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Yes']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Yes']")
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