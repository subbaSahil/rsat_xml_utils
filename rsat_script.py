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
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedShowListButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedShowListButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Show list']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Show list']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: LedgerJournalName_JournalName
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalName_JournalName')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Name')]") ):
    #clicking inside grid: LedgerJournalName_JournalName
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalName_JournalName')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalName_JournalName')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalName_JournalName')])[1]", "aaa")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Name')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]", "aaa")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalName_JournalName')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalName_JournalName')]", "aaa")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Name')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Name')]", "aaa")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: LedgerJournalName_Name
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalName_Name')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Description')]") ):
    #clicking inside grid: LedgerJournalName_Name
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalName_Name')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalName_Name')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalName_Name')])[1]", "abcd")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Description')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Description')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Description')])[1]", "abcd")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalName_Name')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalName_Name')]", "abcd")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Description')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Description')]", "abcd")
    Interactions.press_enter(driver, By.XPATH, "//body")
# clicking dropdown for Tree
Interactions.wait_and_click(driver, By.XPATH, "//input[contains(@name,'VoucherNumber_NumberSequenceTable')]/parent::div/parent::div/following-sibling::div/div")
# Clicking button: Grid
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']")
# Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
time.sleep(5)
print("test case passed")
driver.quit()