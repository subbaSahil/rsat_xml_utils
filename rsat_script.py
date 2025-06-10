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
# Clicking navigation: Ledger setup
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Ledger setup']")
time.sleep(1)
# Clicking navigation: General ledger parameters
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='General ledger parameters']")
time.sleep(1)
Interactions.wait_and_click(driver, By.XPATH, "//li[contains(@data-dyn-controlname,'DimensionsTab')]")
# Clicking (default) on: UpdateDelimiter
Interactions.wait_and_click(driver, By.XPATH, "//span[text() = 'Change delimiter']/ancestor::a")
# Interactions.press_enter(driver, By.XPATH, "//span[text() = 'Change delimiter']/ancestor::a")
# Clicking combobox: Fld1_1
combox_box_to_click = None
if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='Fld1_1']/following-sibling::div"):
     combox_box_to_click = "//input[@name='Fld1_1']/following-sibling::div"
elif Interactions.check_element_exist(driver, By.XPATH, "//input[@aria-label='Dimension segment delimiter']/following-sibling::div"):
     combox_box_to_click = "//input[@aria-label='Dimension segment delimiter']/following-sibling::div"
elif Interactions.check_element_exist(driver, By.XPATH, "//input[@name='Fld1_1']/parent::div/following-sibling::div/div"):
     combox_box_to_click = "//input[@name='Fld1_1']/parent::div/following-sibling::div/div"
Interactions.wait_and_click(driver, By.XPATH, combox_box_to_click)
if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'Fld1_1')]//li[@data-dyn-index='3']"):
     Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'Fld1_1')]//li[@data-dyn-index='3']")
elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id,'Fld1_1')]//li[3]"):
     Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@id,'Fld1_1')]//li[3]")
else:
     if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'Fld1_1')]"):
            cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'Fld1_1')]",By.XPATH, "//ul[contains(@aria-labelledby, 'Fld1_1')]//li[@data-dyn-index='3']")
            if cliked_or_not == False:
                Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'Fld1_1')]",By.XPATH, "//ul[contains(@id,'Fld1_1')]//li[3]")
     elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id, 'Fld1_1')]"):
            cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'Fld1_1')]",By.XPATH, "//ul[contains(@aria-labelledby, 'Fld1_1')]//li[@data-dyn-index='3']")
            if cliked_or_not == False:
                Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'Fld1_1')]",By.XPATH, "//ul[contains(@id,'Fld1_1')]//li[3]")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='UpdateButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='UpdateButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Modify']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Modify']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Yes']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Yes']")
time.sleep(5)
print("test case passed")
driver.quit()