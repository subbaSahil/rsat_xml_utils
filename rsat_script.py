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
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Sales and marketing
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Sales and marketing']")
time.sleep(1)
# Clicking navigation: Sales orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Sales orders']")
time.sleep(1)
# Clicking navigation: Open orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Open orders']")
time.sleep(1)
# Clicking navigation: Backorder lines
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Backorder lines']")
time.sleep(1)
# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Item number"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        break
if filter_manager_cloumn_last_opened == 'Item number' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Item number']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Item number']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Item number']")
filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of 'D0001' on the 'Item number' field using the 'is exactly' filter operator.")
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
# Inputting into: SalesLine_SalesId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'SalesLine_SalesId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Sales order')]") ):
    #clicking inside grid: SalesLine_SalesId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'SalesLine_SalesId')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'SalesLine_SalesId')])[1]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Sales order')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Sales order')])[1]", "")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SalesLine_SalesId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'SalesLine_SalesId')]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Sales order')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Sales order')]", "")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Clicking button: SalesLineGrid
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
time.sleep(5)
print("test case passed")
driver.quit()