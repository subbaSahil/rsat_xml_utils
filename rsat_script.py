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

filter_manager_cloumn_last_opened = ""
column_to_open = ""
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")

# Clicking navigation: Accounts payable
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
time.sleep(1)

# Clicking navigation: Invoices
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Invoices']")
time.sleep(1)

# Clicking navigation: Pending vendor invoices
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Pending vendor invoices']")
time.sleep(1)

# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Invoice"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        print(f"filter_manager_cloumn_last_opened: {filter_manager_cloumn_last_opened}")
        break
if filter_manager_cloumn_last_opened == 'Invoice' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice']")
filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of '100' on the 'Invoice' field using the 'contains' filter operator.")
operator = filter_manager_data['operator']
new_val = filter_manager_data['value']
field_name = filter_manager_data['field_name']
drop_down_item = "//span[text()='"+operator+"']/ancestor::button[contains(@class,'button flyout-menuItem')]"
print(drop_down_item)
input_field = "//input[contains(@aria-label,'Filter field: "+field_name+",')]"
apply_button = "//input[contains(@aria-label,'Filter field: "+field_name+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-buttons']//span[text()='Apply']/ancestor::button"
dropDown_button = "//span[contains(@class,'button-label-dropDown')]/ancestor::button[contains(@class,'dynamicsButton')][ancestor::div[@class='filterFieldContainer']//input[contains(@aria-label,'Filter field: "+field_name+"')]]"
Interactions.wait_and_click(driver, By.XPATH, dropDown_button)
Interactions.wait_and_click(driver, By.XPATH, drop_down_item)
Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val)
Interactions.wait_and_click(driver, By.XPATH, apply_button)
# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Invoice"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        print(f"filter_manager_cloumn_last_opened: {filter_manager_cloumn_last_opened}")
        break
if filter_manager_cloumn_last_opened == 'Invoice' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice']")
print("//input[contains(@aria-label,'Filter field: "+column_to_open+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-sort']//span[text()='Sort Z to A']/ancestor::button")
Interactions.wait_and_click(driver, By.XPATH, "//input[contains(@aria-label,'Filter field: "+column_to_open+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-sort']//span[text()='Sort Z to A']/ancestor::button")
# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Company"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        print(f"filter_manager_cloumn_last_opened: {filter_manager_cloumn_last_opened}")
        break
if filter_manager_cloumn_last_opened == 'Company' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Company']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Company']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Company']")
print("//input[contains(@aria-label,'Filter field: "+column_to_open+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-sort']//span[text()='Sort Z to A']/ancestor::button")
Interactions.wait_and_click(driver, By.XPATH, "//input[contains(@aria-label,'Filter field: "+column_to_open+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-sort']//span[text()='Sort Z to A']/ancestor::button")
# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Name"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        print(f"filter_manager_cloumn_last_opened: {filter_manager_cloumn_last_opened}")
        break
if filter_manager_cloumn_last_opened == 'Name' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Name']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Name']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Name']")
filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of '1' on the 'Name' field using the 'does not contain' filter operator.")
operator = filter_manager_data['operator']
new_val = filter_manager_data['value']
field_name = filter_manager_data['field_name']
drop_down_item = "//span[text()='"+operator+"']/ancestor::button[contains(@class,'button flyout-menuItem')]"
print(drop_down_item)
input_field = "//input[contains(@aria-label,'Filter field: "+field_name+",')]"
apply_button = "//input[contains(@aria-label,'Filter field: "+field_name+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-buttons']//span[text()='Apply']/ancestor::button"
dropDown_button = "//span[contains(@class,'button-label-dropDown')]/ancestor::button[contains(@class,'dynamicsButton')][ancestor::div[@class='filterFieldContainer']//input[contains(@aria-label,'Filter field: "+field_name+"')]]"
Interactions.wait_and_click(driver, By.XPATH, dropDown_button)
Interactions.wait_and_click(driver, By.XPATH, drop_down_item)
Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val)
Interactions.wait_and_click(driver, By.XPATH, apply_button)
# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Invoice received date"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        print(f"filter_manager_cloumn_last_opened: {filter_manager_cloumn_last_opened}")
        break
if filter_manager_cloumn_last_opened == 'Invoice received date' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice received date']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice received date']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice received date']")
# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Invoice date"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        print(f"filter_manager_cloumn_last_opened: {filter_manager_cloumn_last_opened}")
        break
if filter_manager_cloumn_last_opened == 'Invoice date' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice date']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice date']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice date']")
time.sleep(5)
print("test case passed")
driver.quit()