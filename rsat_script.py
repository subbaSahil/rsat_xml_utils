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
# Clicking navigation: Procurement and sourcing
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Procurement and sourcing']")
time.sleep(1)
# Clicking navigation: Purchase orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
time.sleep(1)
# Clicking navigation: All purchase orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
time.sleep(1)
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
filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of '00001364' on the 'Purchase order' field using the 'is exactly' filter operator.")
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
# Clicking button: Grid
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Edit']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Edit']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripNew']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripNew']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Add line']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Add line']")
"Skipping grid since it is deafault behavior of d365"
# Inputting into: PurchLine_ItemId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
    #clicking inside grid: PurchLine_ItemId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_ItemId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: InventoryDimensionsGrid_InventSiteId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Site')]") ):
    #clicking inside grid: InventoryDimensionsGrid_InventSiteId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')])[1]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Site')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]", "")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventSiteId')]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Site')]", "")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: InventoryDimensionsGrid_InventLocationId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]") ):
    #clicking inside grid: InventoryDimensionsGrid_InventLocationId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')])[1]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Warehouse')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]", "")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InventoryDimensionsGrid_InventLocationId')]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]", "")
    Interactions.press_enter(driver, By.XPATH, "//body")
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]") ):
    #clicking inside grid: PurchLine_PurchQtyGrid
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchQtyGrid')])[1]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_PurchQtyGrid')])[1]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchQtyGrid')])[1]", "10.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Quantity')])[1]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@aria-label,'Quantity')])[1]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Quantity')])[1]", "10.00")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_PurchQtyGrid')]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]", "10.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@aria-label,'Quantity')]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]", "10.00")
    Interactions.press_enter(driver, By.XPATH, "//body")
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchPriceGrid')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Unit price')]") ):
    #clicking inside grid: PurchLine_PurchPriceGrid
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchPriceGrid')])[1]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_PurchPriceGrid')])[1]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchPriceGrid')])[1]", "90.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Unit price')])[1]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@aria-label,'Unit price')])[1]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Unit price')])[1]", "90.00")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchPriceGrid')]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_PurchPriceGrid')]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchPriceGrid')]", "90.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Unit price')]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@aria-label,'Unit price')]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Unit price')]", "90.00")
    Interactions.press_enter(driver, By.XPATH, "//body")
Interactions.wait_and_click(driver, By.XPATH, "//li[contains(@data-dyn-controlname,'TabLineDelivery')]")
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DeliveryDate')]")):
    Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Requested receipt date')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'DeliveryDate')]", "05/29/2025")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Requested receipt date')]")):
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Requested receipt date')]", "05/29/2025")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'ConfirmedDlv')]")):
    Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Confirmed receipt date')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'ConfirmedDlv')]", "05/29/2025")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Confirmed receipt date')]")):
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Confirmed receipt date')]", "05/29/2025")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
time.sleep(5)
print("test case passed")
driver.quit()