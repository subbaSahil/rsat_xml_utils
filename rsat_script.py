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

# Clicking navigation: Accounts payable
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
time.sleep(1)

# Clicking navigation: Vendors
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Vendors']")
time.sleep(1)

# Clicking navigation: Vendor groups
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Vendor groups']")
time.sleep(1)

# Clicking navigation: Purchase orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
time.sleep(1)

# Clicking navigation: All purchase orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
time.sleep(1)

# Clicking navigation: Invoices
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Invoices']")
time.sleep(1)

# Clicking navigation: Pending vendor invoices
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Pending vendor invoices']")
time.sleep(1)

# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# ❌ Locator not found for: No Control Name (Type: )
# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Vendor group"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        break
if filter_manager_cloumn_last_opened == 'Vendor group' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Vendor group']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Vendor group']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Vendor group']")
filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of '123' on the 'Vendor group' field using the 'begins with' filter operator.")
operator = filter_manager_data['operator']
new_val = filter_manager_data['value']
field_name = filter_manager_data['field_name']
drop_down_item = "//input[contains(@aria-label,'Filter field: "+field_name+",')]/ancestor::div[@class='columnHeader-popup sysPopup']/ancestor::body/child::div[@class='sysPopup flyoutButton-flyOut layout-root-scope']//button//span[text()='"+operator+"']"
input_field = "//input[contains(@aria-label,'Filter field: "+field_name+",')]"
apply_button = "//input[contains(@aria-label,'Filter field: "+field_name+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-buttons']//span[text()='Apply']/ancestor::button"
dropDown_button = "//span[contains(@class,'button-label-dropDown')]/ancestor::button[contains(@class,'dynamicsButton')][ancestor::div[@class='filterFieldContainer']//input[contains(@aria-label,'Filter field: "+field_name+"')]]"
Interactions.wait_and_click(driver, By.XPATH, dropDown_button)
Interactions.wait_and_click(driver, By.XPATH, drop_down_item)
if(Interactions.check_element_exist(driver, By.XPATH, "//div[contains(@class,'popupShadow popupView preview')]")):
    actions = ActionChains(driver)
    other_element = driver.find_element(By.XPATH, "//div[text()='" + field_name + "']")
    actions.move_to_element(other_element).perform()
if operator == 'is one of' or operator == 'matches':
    new_val = Interactions.extract_multiple_values(new_val)
    for new_val_value in new_val:
        Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val_value)
        Interactions.wait_and_click(driver, By.XPATH, apply_button)
elif operator == 'between':
    new_val = Interactions.extract_dates(new_val)
    from_date_locator = "(//input[contains(@aria-label,'Filter field: " + field_name + ",')])[1]"
    to_date_locator = "(//input[contains(@aria-label,'Filter field: " + field_name + ",')])[2]"
    Interactions.wait_and_send_keys(driver, By.XPATH, from_date_locator, new_val[0])
    Interactions.wait_and_send_keys(driver, By.XPATH, to_date_locator, new_val[1])
else:
    Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val)
Interactions.wait_and_click(driver, By.XPATH, apply_button)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# ❌ Locator not found for: No Control Name (Type: )
# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Purchase order"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        break
if filter_manager_cloumn_last_opened == 'Purchase order' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Purchase order']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Purchase order']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Purchase order']")
filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of '00000042' on the 'Purchase order' field using the 'does not contain' filter operator.")
operator = filter_manager_data['operator']
new_val = filter_manager_data['value']
field_name = filter_manager_data['field_name']
drop_down_item = "//input[contains(@aria-label,'Filter field: "+field_name+",')]/ancestor::div[@class='columnHeader-popup sysPopup']/ancestor::body/child::div[@class='sysPopup flyoutButton-flyOut layout-root-scope']//button//span[text()='"+operator+"']"
input_field = "//input[contains(@aria-label,'Filter field: "+field_name+",')]"
apply_button = "//input[contains(@aria-label,'Filter field: "+field_name+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-buttons']//span[text()='Apply']/ancestor::button"
dropDown_button = "//span[contains(@class,'button-label-dropDown')]/ancestor::button[contains(@class,'dynamicsButton')][ancestor::div[@class='filterFieldContainer']//input[contains(@aria-label,'Filter field: "+field_name+"')]]"
Interactions.wait_and_click(driver, By.XPATH, dropDown_button)
Interactions.wait_and_click(driver, By.XPATH, drop_down_item)
if(Interactions.check_element_exist(driver, By.XPATH, "//div[contains(@class,'popupShadow popupView preview')]")):
    actions = ActionChains(driver)
    other_element = driver.find_element(By.XPATH, "//div[text()='" + field_name + "']")
    actions.move_to_element(other_element).perform()
if operator == 'is one of' or operator == 'matches':
    new_val = Interactions.extract_multiple_values(new_val)
    for new_val_value in new_val:
        Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val_value)
        Interactions.wait_and_click(driver, By.XPATH, apply_button)
elif operator == 'between':
    new_val = Interactions.extract_dates(new_val)
    from_date_locator = "(//input[contains(@aria-label,'Filter field: " + field_name + ",')])[1]"
    to_date_locator = "(//input[contains(@aria-label,'Filter field: " + field_name + ",')])[2]"
    Interactions.wait_and_send_keys(driver, By.XPATH, from_date_locator, new_val[0])
    Interactions.wait_and_send_keys(driver, By.XPATH, to_date_locator, new_val[1])
else:
    Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val)
Interactions.wait_and_click(driver, By.XPATH, apply_button)
# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Vendor account"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        break
if filter_manager_cloumn_last_opened == 'Vendor account' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Vendor account']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Vendor account']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Vendor account']")
Interactions.wait_and_click(driver, By.XPATH, "//input[contains(@aria-label,'Filter field: "+column_to_open+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-sort']//span[text()='Sort Z to A']/ancestor::button")
# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Invoice account"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        break
if filter_manager_cloumn_last_opened == 'Invoice account' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice account']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice account']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Invoice account']")
filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of '1002' on the 'Invoice account' field using the 'does not contain' filter operator.")
operator = filter_manager_data['operator']
new_val = filter_manager_data['value']
field_name = filter_manager_data['field_name']
drop_down_item = "//input[contains(@aria-label,'Filter field: "+field_name+",')]/ancestor::div[@class='columnHeader-popup sysPopup']/ancestor::body/child::div[@class='sysPopup flyoutButton-flyOut layout-root-scope']//button//span[text()='"+operator+"']"
input_field = "//input[contains(@aria-label,'Filter field: "+field_name+",')]"
apply_button = "//input[contains(@aria-label,'Filter field: "+field_name+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-buttons']//span[text()='Apply']/ancestor::button"
dropDown_button = "//span[contains(@class,'button-label-dropDown')]/ancestor::button[contains(@class,'dynamicsButton')][ancestor::div[@class='filterFieldContainer']//input[contains(@aria-label,'Filter field: "+field_name+"')]]"
Interactions.wait_and_click(driver, By.XPATH, dropDown_button)
Interactions.wait_and_click(driver, By.XPATH, drop_down_item)
if(Interactions.check_element_exist(driver, By.XPATH, "//div[contains(@class,'popupShadow popupView preview')]")):
    actions = ActionChains(driver)
    other_element = driver.find_element(By.XPATH, "//div[text()='" + field_name + "']")
    actions.move_to_element(other_element).perform()
if operator == 'is one of' or operator == 'matches':
    new_val = Interactions.extract_multiple_values(new_val)
    for new_val_value in new_val:
        Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val_value)
        Interactions.wait_and_click(driver, By.XPATH, apply_button)
elif operator == 'between':
    new_val = Interactions.extract_dates(new_val)
    from_date_locator = "(//input[contains(@aria-label,'Filter field: " + field_name + ",')])[1]"
    to_date_locator = "(//input[contains(@aria-label,'Filter field: " + field_name + ",')])[2]"
    Interactions.wait_and_send_keys(driver, By.XPATH, from_date_locator, new_val[0])
    Interactions.wait_and_send_keys(driver, By.XPATH, to_date_locator, new_val[1])
else:
    Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val)
Interactions.wait_and_click(driver, By.XPATH, apply_button)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# ❌ Locator not found for: No Control Name (Type: )
# Inputting into: QuickFilterControl
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'QuickFilterControl')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "")
    Interactions.press_enter(driver, By.XPATH, locator)
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "")
    Interactions.press_enter(driver, By.XPATH, locator)
# Inputting into: CompanyFilter
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'CompanyFilter')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'CompanyFilter')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Company')]")):
    locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Company')]")
    Interactions.wait_and_send_keys(driver, By.XPATH, locator, "")
# Clicking button: OK
Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Name"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        break
if filter_manager_cloumn_last_opened == 'Name' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Name']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Name']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Name']")
Interactions.wait_and_click(driver, By.XPATH, "//input[contains(@aria-label,'Filter field: "+column_to_open+", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-sort']//span[text()='Sort Z to A']/ancestor::button")
time.sleep(5)
print("test case passed")
driver.quit()