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
# Clicking navigation: Accounts payable
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
time.sleep(1)
# Clicking navigation: Broker and royalties
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Broker and royalties']")
time.sleep(1)
# Clicking navigation: Broker claims
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Broker claims']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SSRS_OpenBrokerInvoices']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SSRS_OpenBrokerInvoices']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Broker report']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Broker report']")
# Open dropdown for Broker
Interactions.wait_and_click(driver, By.XPATH, "//input[@name='Fld1_1']/following-sibling::div//*[contains(@class, 'lookupButton')]")
time.sleep(1)
user_input = input("Press data to select: ")
Interactions.scroll_and_click(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
user_input = input("Press data to select: ")
Interactions.scroll_and_click(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
user_input = input("Press data to select: ")
Interactions.scroll_and_click(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Select']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Select']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='CommandButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
time.sleep(5)
print("test case passed")
driver.quit()