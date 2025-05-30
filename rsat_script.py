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
# Closing the page
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Inventory management
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Inventory management']")
time.sleep(1)
# Clicking navigation: Inquiries and reports
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Inquiries and reports']")
time.sleep(1)
# Clicking navigation: On-hand list
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='On-hand list']")
time.sleep(1)
#Applying filter:
Interactions.wait_and_click(driver, By.XPATH, "//div[@title='Item number']/following-sibling::div/button")
Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-role='FilterPane']/ancestor::div[@id='mainContainer']/following-sibling::div/div/button/div/span[text()='contains']")
Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//div[@title='Item number']/parent::div/parent::div/following-sibling::div//input","GA0002")
Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Apply']//ancestor::button")
#Applying filter:
Interactions.wait_and_click(driver, By.XPATH, "//div[@title='Site']/following-sibling::div/button")
Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-role='FilterPane']/ancestor::div[@id='mainContainer']/following-sibling::div/div/button/div/span[text()='contains']")
Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//div[@title='Site']/parent::div/parent::div/following-sibling::div//input","2")
Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Apply']//ancestor::button")
#Applying filter:
Interactions.wait_and_click(driver, By.XPATH, "//div[@title='Warehouse']/following-sibling::div/button")
Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-role='FilterPane']/ancestor::div[@id='mainContainer']/following-sibling::div/div/button/div/span[text()='is not']")
Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//div[@title='Warehouse']/parent::div/parent::div/following-sibling::div//input","11-UND")
Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Apply']//ancestor::button")
#Applying filter:
Interactions.wait_and_click(driver, By.XPATH, "//div[@title='Serial number']/following-sibling::div/button")
Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-role='FilterPane']/ancestor::div[@id='mainContainer']/following-sibling::div/div/button/div/span[text()='contains']")
Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//div[@title='Serial number']/parent::div/parent::div/following-sibling::div//input","000002")
Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Apply']//ancestor::button")
#Applying filter:
Interactions.wait_and_click(driver, By.XPATH, "//div[@title='Search name']/following-sibling::div/button")
Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-role='FilterPane']/ancestor::div[@id='mainContainer']/following-sibling::div/div/button/div/span[text()='does not contain']")
Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//div[@title='Search name']/parent::div/parent::div/following-sibling::div//input","abc")
Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Apply']//ancestor::button")
time.sleep(5)
print("test case passed")
driver.quit()