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
# Clicking navigation: Periodic tasks
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Periodic tasks']")
time.sleep(1)
# Clicking navigation: Periodic journals
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Periodic journals']")
time.sleep(1)
# Clicking button: GridOverview
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='JournalLines']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='JournalLines']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Lines']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Lines']")
"Skipping grid since it is deafault behavior of d365"
# Inputting into: LedgerJournalTrans_Voucher
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_Voucher')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Voucher')]") ):
    #clicking inside grid: LedgerJournalTrans_Voucher
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_Voucher')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_Voucher')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_Voucher')])[1]", "ok")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Voucher')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Voucher')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Voucher')])[1]", "ok")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_Voucher')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_Voucher')]", "ok")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Voucher')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Voucher')]", "ok")
    Interactions.press_enter(driver, By.XPATH, "//body")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: General ledger
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='General ledger']")
time.sleep(1)
# Clicking navigation: Periodic tasks
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Periodic tasks']")
time.sleep(1)
# Clicking navigation: Periodic journals
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Periodic journals']")
time.sleep(1)
# Clicking button: GridOverview
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='JournalLines']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='JournalLines']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Lines']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Lines']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Print_MenuButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Print_MenuButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Print']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Print']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='JounalDetails']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='JounalDetails']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Journal']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Journal']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
time.sleep(5)
print("test case passed")
driver.quit()