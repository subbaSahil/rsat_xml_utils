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

test_passed = True

try:
     Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
# Clicking navigation: Vendors
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Vendors']")
# Clicking navigation: Vendors past due
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Vendors past due']")
# Inputting into: QuickFilterControl
     if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "1001")
         Interactions.press_enter(driver, By.XPATH, locator)
     elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "1001")
         Interactions.press_enter(driver, By.XPATH, locator)
# Inputting into: QuickFilterControl
     if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "10")
         Interactions.press_enter(driver, By.XPATH, locator)
     elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "10")
         Interactions.press_enter(driver, By.XPATH, locator)
except Exception as e:
     test_passed = False
     print("Test case failed:"+ e)
finally:
     if test_passed:
          print("✅ Test case passed")
          Interactions.take_screenshot_on_pass(driver, "test_case_passed")
     else:
          print("❌ Test case failed")
     driver.quit()