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
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripDelete']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LineStripDelete']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Remove']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Remove']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
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
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
    #clicking inside grid: PurchLine_ItemId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchLine_ItemId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchLine_ItemId')])[1]", "0002")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "0002")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchLine_ItemId')]", "0002")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "0002")
    Interactions.press_enter(driver, By.XPATH, "//body")
"Skipping grid since previous was control was input"
"Skipping grid selection due input in the ancestor"
# clicking dropdown for Tree
Interactions.wait_and_click(driver, By.XPATH, "//input[@role='combobox']/parent::div/parent::div/following-sibling::div")
#Expanding paths: CORP PROCUREMENT CATEGORIES (OFFICE EQUIPMENT AND ACCESSORIES AND SUPPLIES)
if not (Interactions.checkInputExpanded(driver, By.XPATH, "//li[@aria-label='CORP PROCUREMENT CATEGORIES (OFFICE EQUIPMENT AND ACCESSORIES AND SUPPLIES)']")):
     Interactions.wait_and_click(driver, By.XPATH, "//li[@aria-label='CORP PROCUREMENT CATEGORIES (OFFICE EQUIPMENT AND ACCESSORIES AND SUPPLIES)']/div/button[@type='button']")
#Expanding paths: WORKPLACE SERVICES (WORKPLACE SERVICES)
if not (Interactions.checkInputExpanded(driver, By.XPATH, "//li[@aria-label='WORKPLACE SERVICES (WORKPLACE SERVICES)']")):
     Interactions.wait_and_click(driver, By.XPATH, "//li[@aria-label='WORKPLACE SERVICES (WORKPLACE SERVICES)']/div/button[@type='button']")
# Clicking on last path: Cleaning (Cleaning)
Interactions.wait_and_click(driver, By.XPATH, "//li[@aria-label='Cleaning (Cleaning)']/div/button[@type='button']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
"Skipping grid since it is deafault behavior of d365"
time.sleep(5)
print("test case passed")
driver.quit()