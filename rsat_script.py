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
line_number_input = "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']//input[contains(@aria-label,'Line number')]"
count = Interactions.check_for_item_number_count(driver, By.XPATH, line_number_input)
row_number = Interactions.get_row_number_for_line_item(driver, By.XPATH, line_number_input,count)
"Skipping grid since it is deafault behavior of d365"
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
    #clicking inside grid: PurchLine_ItemId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])["+row_number+"]", "P0004")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])["+row_number+"]", "P0004")
"Skipping grid since previous was control was input"
"Skipping grid selection due input in the ancestor"
line_number_input = "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']//input[contains(@aria-label,'Line number')]"
count = Interactions.check_for_item_number_count(driver, By.XPATH, line_number_input)
row_number = Interactions.get_row_number_for_line_item(driver, By.XPATH, line_number_input,count)
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchReceivedNow')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Receive now')]") ):
    #clicking inside grid: PurchLine_PurchReceivedNow
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_PurchReceivedNow')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])["+row_number+"]", "1.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Receive now')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])["+row_number+"]", "1.00")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripNew']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripNew']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Add line']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Add line']")
line_number_input = "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']//input[contains(@aria-label,'Line number')]"
count = Interactions.check_for_item_number_count(driver, By.XPATH, line_number_input)
row_number = Interactions.get_row_number_for_line_item(driver, By.XPATH, line_number_input,count)
"Skipping grid since it is deafault behavior of d365"
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
    #clicking inside grid: PurchLine_ItemId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_ItemId')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])["+row_number+"]", "M0056")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Item number')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])["+row_number+"]", "M0056")
"Skipping grid since previous was control was input"
"Skipping grid selection due input in the ancestor"
line_number_input = "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']//input[contains(@aria-label,'Line number')]"
count = Interactions.check_for_item_number_count(driver, By.XPATH, line_number_input)
row_number = Interactions.get_row_number_for_line_item(driver, By.XPATH, line_number_input,count)
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_PurchReceivedNow')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Receive now')]") ):
    #clicking inside grid: PurchLine_PurchReceivedNow
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchLine_PurchReceivedNow')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_PurchReceivedNow')])["+row_number+"]", "2.00")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])["+row_number+"]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Receive now')])["+row_number+"]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Receive now')])["+row_number+"]", "2.00")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
time.sleep(5)
print("test case passed")
driver.quit()