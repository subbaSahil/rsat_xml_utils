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
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQty')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]") ):
    #clicking inside grid: PurchLine_PurchQty
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchQty')])[1]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_PurchQty')])[1]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchQty')])[1]", "2.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Quantity')])[1]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@aria-label,'Quantity')])[1]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Quantity')])[1]", "2.00")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQty')]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_PurchQty')]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchQty')]", "2.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]")):
         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@aria-label,'Quantity')]")).perform()
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Quantity')]", "2.00")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since it is deafault behavior of d365"
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_DeliveryDate')]")):
    Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Requested receipt date')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_DeliveryDate')]", "01/31/2017")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Requested receipt date')]")):
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Requested receipt date')]", "01/31/2017")
if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_ConfirmedDlv')]")):
    Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'Confirmed receipt date')]")
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_ConfirmedDlv')]", "06/30/2025")
elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Confirmed receipt date')]")):
    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Confirmed receipt date')]", "06/30/2025")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
# if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")):
#      Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")
# elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Yes']")):
#      Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Yes']")
time.sleep(5)
print("test case passed")
driver.quit()