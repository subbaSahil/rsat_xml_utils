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
# Clicking navigation: Journal setup
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Journal setup']")
time.sleep(1)
# Clicking navigation: Journal names
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Journal names']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: LedgerJournalName_JournalName
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalName_JournalName')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Name')]") ):
    #clicking inside grid: LedgerJournalName_JournalName
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalName_JournalName')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalName_JournalName')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalName_JournalName')])[1]", "test 10")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Name')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]", "test 10")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalName_JournalName')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalName_JournalName')]", "test 10")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Name')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Name')]", "test 10")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: LedgerJournalName_Name
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalName_Name')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Description')]") ):
    #clicking inside grid: LedgerJournalName_Name
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalName_Name')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalName_Name')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalName_Name')])[1]", "testing 1")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Description')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Description')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Description')])[1]", "testing 1")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalName_Name')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalName_Name')]", "testing 1")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Description')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Description')]", "testing 1")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Clicking combobox: JournalType_JournalType
if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='JournalType_JournalType']"):
     Interactions.wait_and_click(driver, By.XPATH, "//input[@name='JournalType_JournalType']")
     if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'JournalType_JournalType')]//li[@data-dyn-index='31']"):
         Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'JournalType_JournalType')]//li[@data-dyn-index='31']")
     else:Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'JournalType_JournalType')]",By.XPATH, "//ul[contains(@aria-labelledby, 'JournalType_JournalType')]//li[@data-dyn-index='1']")
# clicking dropdown for Tree
Interactions.wait_and_click(driver, By.XPATH, "//input[contains(@name,'VoucherNumber_NumberSequenceTable')]/parent::div/parent::div/following-sibling::div/div")
# Inputting into: VoucherNumber_NumberSequenceTable_NumberSequence
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'VoucherNumber_NumberSequenceTable_NumberSequence')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Voucher series')]") ):
    #clicking inside grid: VoucherNumber_NumberSequenceTable_NumberSequence
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'VoucherNumber_NumberSequenceTable_NumberSequence')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'VoucherNumber_NumberSequenceTable_NumberSequence')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'VoucherNumber_NumberSequenceTable_NumberSequence')])[1]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Voucher series')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Voucher series')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Voucher series')])[1]", "")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'VoucherNumber_NumberSequenceTable_NumberSequence')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'VoucherNumber_NumberSequenceTable_NumberSequence')]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Voucher series')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Voucher series')]", "")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
"Skipping grid selection due input in the ancestor"
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
time.sleep(5)
print("test case passed")
driver.quit()