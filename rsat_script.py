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
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts receivable
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts receivable']")
time.sleep(1)
# Clicking navigation: Orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Orders']")
time.sleep(1)
# Clicking navigation: All sales orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All sales orders']")
time.sleep(1)
# ❌ Locator not found for: No Control Name (Type: )
# Clicking (default) on: Manage
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Manage']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='CheckCreditLimit']")):
     locator=Interactions.get_locator(driver, By.XPATH, "//button[@data-dyn-controlname='CheckCreditLimit']")
     Interactions.wait_and_click(driver, By.XPATH, locator)
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Check credit limit']")):
     locator=Interactions.get_locator(driver, By.XPATH, "//button[@aria-label='Check credit limit']")
     Interactions.wait_and_click(driver, By.XPATH, locator)
# Clicking (default) on: Manage
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Manage']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='PriceDiscActual']")):
     locator=Interactions.get_locator(driver, By.XPATH, "//button[@data-dyn-controlname='PriceDiscActual']")
     Interactions.wait_and_click(driver, By.XPATH, locator)
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Prices']")):
     locator=Interactions.get_locator(driver, By.XPATH, "//button[@aria-label='Prices']")
     Interactions.wait_and_click(driver, By.XPATH, locator)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='PriceSales']")):
     locator=Interactions.get_locator(driver, By.XPATH, "//button[@data-dyn-controlname='PriceSales']")
     Interactions.wait_and_click(driver, By.XPATH, locator)
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='View sales prices']")):
     locator=Interactions.get_locator(driver, By.XPATH, "//button[@aria-label='View sales prices']")
     Interactions.wait_and_click(driver, By.XPATH, locator)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Inputting into: ItemIdFilter
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'ItemIdFilter')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
    #clicking inside grid: ItemIdFilter
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'ItemIdFilter')])[1]")):
         locator=Interactions.get_locator(driver, By.XPATH, "(//input[contains(@name,'ItemIdFilter')])[1]")
         Interactions.wait_and_send_keys(driver, By.XPATH, locator, "A0002")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
         locator=Interactions.get_locator(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")
         Interactions.wait_and_send_keys(driver, By.XPATH, locator, "A0002")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'ItemIdFilter')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'ItemIdFilter')]")
         Interactions.wait_and_send_keys(driver, By.XPATH, locator, "A0002")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")
         Interactions.wait_and_send_keys(driver, By.XPATH, locator, "A0002")
# Clicking button: Grid
# Clicking (default) on: SystemDefinedOptions
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='SystemDefinedOptions']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Clicking (default) on: Manage
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='Manage']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='PdsRebateTable']")):
     locator=Interactions.get_locator(driver, By.XPATH, "//button[@data-dyn-controlname='PdsRebateTable']")
     Interactions.wait_and_click(driver, By.XPATH, locator)
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Rebate']")):
     locator=Interactions.get_locator(driver, By.XPATH, "//button[@aria-label='Rebate']")
     Interactions.wait_and_click(driver, By.XPATH, locator)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")):
     locator=Interactions.get_locator(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")
     Interactions.wait_and_click(driver, By.XPATH, locator)
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Yes']")):
     locator=Interactions.get_locator(driver, By.XPATH, "//button[@aria-label='Yes']")
     Interactions.wait_and_click(driver, By.XPATH, locator)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
time.sleep(5)
print("test case passed")
driver.quit()