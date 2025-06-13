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

test_passed = True

try:
     Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts receivable
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts receivable']")
# Clicking navigation: Customers
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Customers']")
# Clicking navigation: All customers
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All customers']")
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
# Clicking (default) on: aptabProjects
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='aptabProjectss']")
# going to edit view mode
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedViewEditButton']")
     time.sleep(1)
# Inputting into: Name_LastName
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Name_LastName')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Last name')]") ):
          #clicking inside grid: Name_LastName
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Name_LastName')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Name_LastName')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Name_LastName')])[1]", "Ross")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Last name')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Last name')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Last name')])[1]", "Ross")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Name_LastName')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Name_LastName')]", "Ross")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Last name')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Last name')]", "Ross")
     Interactions.press_enter(driver, By.XPATH, "//body")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewAddress']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewAddress']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='NewAddress']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='NewAddress']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Add']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Add']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='NewAddress']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='NewAddress']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Add']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Add']")
# Inputting into: Details_Description
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Details_Description')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Name or description')]") ):
          #clicking inside grid: Details_Description
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Details_Description')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Details_Description')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Details_Description')])[1]", "Address 2")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Name or description')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Name or description')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Name or description')])[1]", "Address 2")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Details_Description')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Details_Description')]", "Address 2")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Name or description')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Name or description')]", "Address 2")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: LogisticsPostalAddress_Street
     if(Interactions.check_element_exist(driver, By.XPATH, "//textarea[@name='LogisticsPostalAddress_Street']")):
          Interactions.wait_and_send_keys(driver, By.XPATH, "//textarea[@name='LogisticsPostalAddress_Street']", "Street 2A")
# Inputting into: LogisticsPostalAddress_City
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LogisticsPostalAddress_City')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'City')]") ):
          #clicking inside grid: LogisticsPostalAddress_City
          if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LogisticsPostalAddress_City')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LogisticsPostalAddress_City')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LogisticsPostalAddress_City')])[1]", "King Cove")
          elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'City')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'City')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'City')])[1]", "King Cove")
     else:
          if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LogisticsPostalAddress_City')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LogisticsPostalAddress_City')]", "King Cove")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'City')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'City')]", "King Cove")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
# Clicking checkbox: IsPrimary
     if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Primary')]/following-sibling::div/span[1]")):
          if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//label[contains(text(),'Primary')]/following-sibling::div/span[1]", True) == False:
               Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Primary')]/following-sibling::div/span[1]")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'IsPrimary') and (@class='toggle-box' or @class='checkBox')]")):
          if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//span[contains(@id, 'IsPrimary') and (@class='toggle-box' or @class='checkBox')]", True) == False:
               Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'IsPrimary') and (@class='toggle-box' or @class='checkBox')]")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@aria-label='Primary']//span")):
          if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, "//div[@aria-label='Primary']//span", True) == False:
               Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Primary']//span")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='No']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='No']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='No']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='No']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OKButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OKButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")
     Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
# Clicking (default) on: aptabSell
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='aptabSell']")
except Exception as e:
     test_passed = False
     print("Test case failed:"+ e)
finally:
     if test_passed:
          print("✅ Test case passed")
          Interactions.take_screenshot_on_pass(driver, "test_case_passed")
     else:
          print("❌ Test case failed")
          Interactions.take_screenshot_on_failure(driver, "test_case_failed")
     driver.quit()