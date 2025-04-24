from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import login
import Interactions
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)

login.login(driver)

locator = ""

Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
time.sleep(1)

# Clicking navigation: Vendors
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Vendors']")
time.sleep(1)

# Clicking navigation: Vendors past due
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Vendors past due']")
time.sleep(1)

# Inputting into: SystemDefinedFilterManager
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SystemDefinedFilterManager')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'SystemDefinedFilterManager')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "")
# Inputting into: SystemDefinedFilterManager
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SystemDefinedFilterManager')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'SystemDefinedFilterManager')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "")
# Inputting into: SystemDefinedFilterManager
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SystemDefinedFilterManager')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'SystemDefinedFilterManager')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "")
# Inputting into: SystemDefinedFilterManager
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SystemDefinedFilterManager')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'SystemDefinedFilterManager')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "")
time.sleep(5)
print("test case passed")
driver.quit()