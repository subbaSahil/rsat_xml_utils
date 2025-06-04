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
filter_manager_data = Interactions.extract_value_and_operator_from_description("Enter a filter value of '00001365' on the 'Purchase order' field using the 'is exactly' filter operator.")
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
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripNew']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripNew']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Add line']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Add line']")
count = Interactions.check_for_line_item_count(driver, By.XPATH, "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']//input[contains(@aria-label,'Line number')]")
row_number = Interactions.get_row_number_for_line_item(driver, By.XPATH, "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']",count)
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
    #clicking inside grid: PurchLine_ItemId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])["+row_number+"]", "0001")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])["+row_number+"]", "0001")
"Skipping grid since previous was control was input"
"Skipping grid since it is deafault behavior of d365"
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQtyGrid')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]") ):
    #clicking inside grid: PurchLine_PurchQtyGrid
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchQtyGrid')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_PurchQtyGrid')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchQtyGrid')])["+row_number+"]", "2.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Quantity')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Quantity')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Quantity')])["+row_number+"]", "2.00")
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchPriceGrid')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Unit price')]") ):
    #clicking inside grid: PurchLine_PurchPriceGrid
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchPriceGrid')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_PurchPriceGrid')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchPriceGrid')])["+row_number+"]", "10.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Unit price')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Unit price')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Unit price')])["+row_number+"]", "10.00")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='LineStripPurchLine']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='LineStripPurchLine']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Purchase order line']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Purchase order line']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='buttonDeliverySchedule']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='buttonDeliverySchedule']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Delivery schedule']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Delivery schedule']/ancestor::button")
line_number = input('Enter the line number: ')
if Interactions.check_element_exist(driver, By.XPATH, "//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']"):
    target_xpath_1 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@name,'PurchLine_PurchQty')]"
    target_xpath_2 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@aria-label,'Quantity')]"
    if Interactions.check_element_exist(driver, By.XPATH, target_xpath_1):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_1, "1.00")
    elif Interactions.check_element_exist(driver, By.XPATH, target_xpath_2):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_2, "1.00")
    else:
        print("Element not found in either dynamic or fallback XPath for: PurchLine_PurchQty")
"Skipping grid since it is deafault behavior of d365"
line_number = input('Enter the line number: ')
if Interactions.check_element_exist(driver, By.XPATH, "//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']"):
    target_xpath_1 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@name,'PurchLine_ConfirmedDlv')]"
    target_xpath_2 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@aria-label,'Confirmed receipt date')]"
    if Interactions.check_element_exist(driver, By.XPATH, target_xpath_1):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_1, "06/04/2025")
    elif Interactions.check_element_exist(driver, By.XPATH, target_xpath_2):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_2, "06/04/2025")
    else:
        print("Element not found in either dynamic or fallback XPath for: PurchLine_ConfirmedDlv")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='NewCommandButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='NewCommandButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
dailog_box_line_count = Interactions.check_for_line_item_count(driver, By.XPATH, "//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label,'Line number')]")
line_number = Interactions.get_max_value_from_elements(driver, By.XPATH, "//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label,'Line number')]", dailog_box_line_count)
if Interactions.check_element_exist(driver, By.XPATH, "//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']"):
    target_xpath_1 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@name,'PurchLine_PurchQty')]"
    target_xpath_2 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@aria-label,'Quantity')]"
    if Interactions.check_element_exist(driver, By.XPATH, target_xpath_1):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_1, "2.00")
    elif Interactions.check_element_exist(driver, By.XPATH, target_xpath_2):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_2, "2.00")
    else:
        print("Element not found in either dynamic or fallback XPath for: PurchLine_PurchQty")
"Skipping grid since it is deafault behavior of d365"
if Interactions.check_element_exist(driver, By.XPATH, "//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']"):
    target_xpath_1 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@name,'PurchLine_ConfirmedDlv')]"
    target_xpath_2 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@aria-label,'Confirmed receipt date')]"
    if Interactions.check_element_exist(driver, By.XPATH, target_xpath_1):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_1, "06/04/2025")
    elif Interactions.check_element_exist(driver, By.XPATH, target_xpath_2):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_2, "06/04/2025")
    else:
        print("Element not found in either dynamic or fallback XPath for: PurchLine_ConfirmedDlv")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Yes']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Yes']")
time.sleep(5)
print("test case passed")
driver.quit()