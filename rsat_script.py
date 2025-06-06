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
# Clicking navigation: Inventory management
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Inventory management']")
time.sleep(1)
# Clicking navigation: Setup
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Setup']")
time.sleep(1)
# Clicking navigation: Inventory
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Inventory']")
time.sleep(1)
# Clicking navigation: Item groups
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Item groups']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: InventItemGroup_ItemGroup
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'InventItemGroup_ItemGroup')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item group')]") ):
    #clicking inside grid: InventItemGroup_ItemGroup
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'InventItemGroup_ItemGroup')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'InventItemGroup_ItemGroup')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'InventItemGroup_ItemGroup')])[1]", "Keyboard1232")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item group')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item group')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item group')])[1]", "Keyboard1232")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventItemGroup_ItemGroup')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InventItemGroup_ItemGroup')]", "Keyboard1232")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item group')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item group')]", "Keyboard1232")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: InventItemGroup_GroupName
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'InventItemGroup_GroupName')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Name')]") ):
    #clicking inside grid: InventItemGroup_GroupName
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'InventItemGroup_GroupName')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'InventItemGroup_GroupName')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'InventItemGroup_GroupName')])[1]", "Keyboard1232")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Name')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]", "Keyboard1232")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventItemGroup_GroupName')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InventItemGroup_GroupName')]", "Keyboard1232")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Name')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Name')]", "Keyboard1232")
    Interactions.press_enter(driver, By.XPATH, "//body")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
if Interactions.check_aria_expanded(driver, By.XPATH, "//div[@data-dyn-controlname='SalesSegmentedEntry']/ancestor::div[@role='group']/preceding-sibling::div[@role='heading']//button") == True:
    Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='SalesSegmentedEntry']/ancestor::div[@role='group']/preceding-sibling::div[@role='heading']//button")
Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//div[@data-dyn-controlname='SalesSegmentedEntry']//input)[1]", "110115")
if Interactions.check_aria_expanded(driver, By.XPATH, "//div[@data-dyn-controlname='PurchSegmentedEntry']/ancestor::div[@role='group']/preceding-sibling::div[@role='heading']//button") == True:
    Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='PurchSegmentedEntry']/ancestor::div[@role='group']/preceding-sibling::div[@role='heading']//button")
Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//div[@data-dyn-controlname='PurchSegmentedEntry']//input)[1]", "110110")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
time.sleep(5)
print("test case passed")
driver.quit()