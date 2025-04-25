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

# Clicking (default) on: PurchOrder
Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='PurchOrder']")
# Clicking (default) on: PurchCopyJournalHeader
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='PurchCopyJournalHeader']")
# Clicking checkbox: CopyMarkup
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Copy charges')]/following-sibling::div/span[1]")):
    Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Copy charges')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'CopyMarkup') and (@class='toggle-box' or @class='checkBox')]")):
    Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'CopyMarkup') and (@class='toggle-box' or @class='checkBox')]")
# Clicking checkbox: CopyPrecisely
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Copy precisely')]/following-sibling::div/span[1]")):
    Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Copy precisely')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'CopyPrecisely') and (@class='toggle-box' or @class='checkBox')]")):
    Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'CopyPrecisely') and (@class='toggle-box' or @class='checkBox')]")
# Clicking checkbox: RecalculateAmount
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Recalculate price')]/following-sibling::div/span[1]")):
    Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Recalculate price')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'RecalculateAmount') and (@class='toggle-box' or @class='checkBox')]")):
    Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'RecalculateAmount') and (@class='toggle-box' or @class='checkBox')]")
# Clicking checkbox: CopyHeader
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Copy order header')]/following-sibling::div/span[1]")):
    Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Copy order header')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'CopyHeader') and (@class='toggle-box' or @class='checkBox')]")):
    Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'CopyHeader') and (@class='toggle-box' or @class='checkBox')]")
# Clicking checkbox: PurchOrderMarkAll
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Select all')]/following-sibling::div/span[1]")):
    Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Select all')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'PurchOrderMarkAll') and (@class='toggle-box' or @class='checkBox')]")):
    Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'PurchOrderMarkAll') and (@class='toggle-box' or @class='checkBox')]")
# Clicking checkbox: PackingSlipMarkAll
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Select all')]/following-sibling::div/span[1]")):
    Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Select all')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'PackingSlipMarkAll') and (@class='toggle-box' or @class='checkBox')]")):
    Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'PackingSlipMarkAll') and (@class='toggle-box' or @class='checkBox')]")
# Clicking button: OK
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
# Clicking (default) on: Purchase
Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='Purchase']")
# Clicking (default) on: PurchCreditNoteHeader
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='PurchCreditNoteHeader']")
# Clicking checkbox: InvoiceMarkAll
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Select all')]/following-sibling::div/span[1]")):
    Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Select all')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'InvoiceMarkAll') and (@class='toggle-box' or @class='checkBox')]")):
    Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'InvoiceMarkAll') and (@class='toggle-box' or @class='checkBox')]")
# Clicking button: OK
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
time.sleep(5)
print("test case passed")
driver.quit()