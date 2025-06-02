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
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripNew']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripNew']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Add line']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Add line']")
"Skipping grid since it is deafault behavior of d365"
# Inputting into: PurchLine_ItemId
line_item_container = "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']"
item_number_input = "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']//input[contains(@aria-label,'Item number')]"
count = Interactions.check_for_item_number_count(driver, By.XPATH, item_number_input)



if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
    #clicking inside grid: PurchLine_ItemId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_ItemId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]", "C0004")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "C0004")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]", "C0004")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "C0004")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
"Skipping grid selection due input in the ancestor"
# Inputting into: PurchLine_VariantId

print("test case passed")
driver.quit()