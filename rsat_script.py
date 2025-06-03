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
# Clicking navigation: Purchase orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
time.sleep(1)
# Clicking navigation: All purchase orders
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
time.sleep(1)
# Clicking button: Grid
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
"Skipping grid since it is deafault behavior of d365"
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='LineStripPurchLine']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='LineStripPurchLine']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Purchase order line']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Purchase order line']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='buttonDeliverySchedule']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='buttonDeliverySchedule']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='Delivery schedule']/ancestor::button")):
     Interactions.wait_and_click(driver, By.XPATH, "//span[text()='Delivery schedule']/ancestor::button")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='NewCommandButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='NewCommandButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
dailog_box_line_count = Interactions.check_for_line_item_count(driver, By.XPATH, "//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label,'Line number')]")
max_line_number = Interactions.get_max_value_from_elements(driver, By.XPATH, "//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label,'Line number')]", dailog_box_line_count)
if Interactions.check_element_exist(driver, By.XPATH, "//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']"):
    target_xpath_1 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{max_line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@name,'PurchLine_PurchQty')]"
    target_xpath_2 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{max_line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@aria-label,'Quantity')]"
    if Interactions.check_element_exist(driver, By.XPATH, target_xpath_1):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_1, "2.00")
    elif Interactions.check_element_exist(driver, By.XPATH, target_xpath_2):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_2, "2.00")
    else:
        print("Element not found in either dynamic or fallback XPath for: PurchLine_PurchQty")
"Skipping grid since it is deafault behavior of d365"
if Interactions.check_element_exist(driver, By.XPATH, "//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']"):
    target_xpath_1 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{max_line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@name,'PurchLine_DeliveryDate')]"
    target_xpath_2 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{max_line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@aria-label,'Requested receipt date')]"
    if Interactions.check_element_exist(driver, By.XPATH, target_xpath_1):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_1, "01/31/2017")
    elif Interactions.check_element_exist(driver, By.XPATH, target_xpath_2):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_2, "01/31/2017")
    else:
        print("Element not found in either dynamic or fallback XPath for: PurchLine_DeliveryDate")
if Interactions.check_element_exist(driver, By.XPATH, "//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']"):
    target_xpath_1 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{max_line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@name,'PurchLine_ConfirmedDlv')]"
    target_xpath_2 = f"//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']//input[contains(@aria-label, 'Line number') and @value='{max_line_number}']/ancestor::div[@role='gridcell']/following-sibling::div//input[contains(@aria-label,'Confirmed receipt date')]"
    if Interactions.check_element_exist(driver, By.XPATH, target_xpath_1):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_1, "06/30/2025")
    elif Interactions.check_element_exist(driver, By.XPATH, target_xpath_2):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_2, "06/30/2025")
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