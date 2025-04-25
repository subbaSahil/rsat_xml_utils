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

# Clicking navigation: Purchase orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
time.sleep(1)

# Clicking navigation: All purchase orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
time.sleep(1)

# Inputting into: GridFilter
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00001")
    Interactions.press_enter(driver, By.XPATH, locator)
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00001")
    Interactions.press_enter(driver, By.XPATH, locator)
# Clicking (default) on: Purchase
# Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='Purchase']")
# Clicking (default) on: PurchOrder
# Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='PurchOrder']")
# Inputting into: GridFilter
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00000")
    Interactions.press_enter(driver, By.XPATH, locator)
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00000")
    Interactions.press_enter(driver, By.XPATH, locator)
# Inputting into: GridFilter
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00000859")
    Interactions.press_enter(driver, By.XPATH, locator)
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "00000859")
    Interactions.press_enter(driver, By.XPATH, locator)
# Clicking (default) on: PurchOrder
# Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='PurchOrder']")
# Inputting into: GridFilter
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'GridFilter')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "000008")
    Interactions.press_enter(driver, By.XPATH, locator)
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "000008")
    Interactions.press_enter(driver, By.XPATH, locator)
# Clicking (default) on: PurchOrder
# Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='PurchOrder']")
time.sleep(5)
print("test case passed")
driver.quit()