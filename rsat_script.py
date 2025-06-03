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
# Clicking navigation: Structures
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Structures']")
time.sleep(1)
# Clicking navigation: Configure account structures
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Configure account structures']")
time.sleep(1)
# Inputting into: MainGridFilter
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'MainGridFilter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'MainGridFilter')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "Brasil")
    Interactions.press_enter(driver, By.XPATH, locator)
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "Brasil")
    Interactions.press_enter(driver, By.XPATH, locator)
# Clicking button: MainGrid
if Interactions.check_element_exist(driver, By.XPATH, f"//input[@value='Brasil']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']"):
     Interactions.wait_and_click(driver, By.XPATH, f"//input[@value='Brasil']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
else:
     Interactions.wait_and_click(driver, By.XPATH, f"//input[@value='Brasil']")
Interactions.press_enter(driver, By.XPATH, "//input[@value='Brasil']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='AddSegmentButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='AddSegmentButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Add segment']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Add segment']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='AddButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='AddButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Add segment']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Add segment']")
time.sleep(5)
print("test case passed")
driver.quit()