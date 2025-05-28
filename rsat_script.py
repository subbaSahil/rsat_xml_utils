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
# Clicking navigation: Product information management
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Product information management']")
time.sleep(1)
# Clicking navigation: Products
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Products']")
time.sleep(1)
# Clicking navigation: Released products
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Released products']")
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
filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of 'F00006' on the 'Item number' field using the 'begins with' filter operator.")
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
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='InventItemOrderSetupAction']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='InventItemOrderSetupAction']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Default order settings']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Default order settings']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Edit']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Edit']")
# Clicking combobox: ctrlDefaultOrderType
if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='ctrlDefaultOrderType']"):
     Interactions.wait_and_click(driver, By.XPATH, "//input[@name='ctrlDefaultOrderType']")
elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'ctrlDefaultOrderType')]//li[@data-dyn-index='1']"):
     Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'ctrlDefaultOrderType')]//li[@data-dyn-index='1']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Product information management
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Product information management']")
time.sleep(1)
# Clicking navigation: Products
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Products']")
time.sleep(1)
# Clicking navigation: All products and product masters
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All products and product masters']")
time.sleep(1)
# Clicking filter manager: SystemDefinedFilterManager
column_to_open = "Product number"
open_divs = driver.find_elements(By.XPATH, "//div/parent::div[contains(@class, 'dyn-headerCell')]")
filter_manager_cloumn_last_opened = ''
for i, div in enumerate(open_divs, start=1):
    class_attr = div.get_attribute('class')
    if 'hasOpenPopup' in class_attr:
        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]")
        break
if filter_manager_cloumn_last_opened == 'Product number' and filter_manager_cloumn_last_opened != '':
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Product number']")
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Product number']")
else:
    Interactions.wait_and_click(driver, By.XPATH, "//div[text()='Product number']")
filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of 'Test1234' on the 'Product number' field using the 'begins with' filter operator.")
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
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='EcoResProductRelease']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='EcoResProductRelease']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Release products']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Release products']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Next']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Next']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Next']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Next']")
# Clicking button: GridLegalEntities
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Next']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Next']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Next']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Next']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Finish']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Finish']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Finish']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Finish']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Product information management
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Product information management']")
time.sleep(1)
# Clicking navigation: Workspaces
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Workspaces']")
# Clicking navigation: Released product maintenance
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Released product maintenance']")
time.sleep(1)
Interactions.wait_and_click(driver, By.XPATH, "//li[contains(@data-dyn-controlname,'ReleasedProductsRecentlyCreated')]")
user_input = input('Enter the value for the hyperlink: ')
Interactions.wait_and_click(driver, By.XPATH, "//input[@title='"+user_input+"']")
Interactions.wait_and_click(driver, By.XPATH, "//div[text()='"+user_input+"']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Edit']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Edit']")
# Clicking button: InventModelGroupItem_ModelGroupId
# Clicking button: Grid
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='DimensionGroups']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='DimensionGroups']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Dimension groups']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Dimension groups']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
# Clicking button: PurchaseSetup_UnitId
# Clicking button: SalesSetup_UnitId
# Clicking button: CostPosting_ItemGroupId
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Validate']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Validate']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Validate']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Validate']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Product information management
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Product information management']")
time.sleep(1)
# Clicking navigation: Products
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Products']")
time.sleep(1)
# Clicking navigation: Released products
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Released products']")
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
filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of 'F00010' on the 'Item number' field using the 'begins with' filter operator.")
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
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='InventItemOrderSetupAction']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='InventItemOrderSetupAction']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Default order settings']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Default order settings']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: InventDim_InventSiteId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'InventDim_InventSiteId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Site')]") ):
    #clicking inside grid: InventDim_InventSiteId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'InventDim_InventSiteId')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'InventDim_InventSiteId')])[1]", "4")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]", "4")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventDim_InventSiteId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InventDim_InventSiteId')]", "4")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Site')]", "4")
    Interactions.press_enter(driver, By.XPATH, "//body")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
time.sleep(5)
print("test case passed")
driver.quit()