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
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
time.sleep(1)

# Clicking navigation: Vendors
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Vendors']")
time.sleep(1)

# Clicking navigation: All vendors
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All vendors']")
time.sleep(1)

# Clicking button: SystemDefinedNewButton
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
# Inputting into: Identification_AccountNum
Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Identification_AccountNum')]", "")
Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Identification_AccountNum')]", Keys.RETURN)
# Inputting into: Org_NameAlias
Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Org_NameAlias')]", "")
Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Org_NameAlias')]", Keys.RETURN)
# Inputting into: Posting_VendGroup
Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Posting_VendGroup')]", "")
Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Posting_VendGroup')]", Keys.RETURN)
time.sleep(5)
driver.quit()