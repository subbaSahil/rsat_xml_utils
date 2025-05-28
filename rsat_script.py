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
# Clicking navigation: Inventory management
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Inventory management']")
time.sleep(1)
# Clicking navigation: Journal entries
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Journal entries']")
time.sleep(1)
# Clicking navigation: Items
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Items']")
time.sleep(1)
# Clicking navigation: Movement
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Movement']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: RetailStoreInventory_InventSiteId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'RetailStoreInventory_InventSiteId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Site')]") ):
    #clicking inside grid: RetailStoreInventory_InventSiteId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'RetailStoreInventory_InventSiteId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'RetailStoreInventory_InventSiteId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'RetailStoreInventory_InventSiteId')])[1]", "1")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Site')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]", "1")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'RetailStoreInventory_InventSiteId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'RetailStoreInventory_InventSiteId')]", "1")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Site')]", "1")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Clicking button: Grid
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
# Inputting into: RetailStoreInventory_InventLocationId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'RetailStoreInventory_InventLocationId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]") ):
    #clicking inside grid: RetailStoreInventory_InventLocationId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'RetailStoreInventory_InventLocationId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'RetailStoreInventory_InventLocationId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'RetailStoreInventory_InventLocationId')])[1]", "11")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Warehouse')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Warehouse')])[1]", "11")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'RetailStoreInventory_InventLocationId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'RetailStoreInventory_InventLocationId')]", "11")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Warehouse')]", "11")
    Interactions.press_enter(driver, By.XPATH, "//body")
# Clicking button: GridInventLocation
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
# Inputting into: Posting_OffsetLedgerDimension
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Posting_OffsetLedgerDimension')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Offset account')]") ):
    #clicking inside grid: Posting_OffsetLedgerDimension
     if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Posting_OffsetLedgerDimension')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Posting_OffsetLedgerDimension')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Posting_OffsetLedgerDimension')])[1]", "110110")
     elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Offset account')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Offset account')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Offset account')])[1]", "110110")
     else:
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//div[@title='Offset account'])[1]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//div[@title='Offset account'])[1]", "110110")
else:
     if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Posting_OffsetLedgerDimension')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Posting_OffsetLedgerDimension')]", "110110")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Offset account')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Offset account')]", "110110")
     else:
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//div[@title='Offset account']")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "//div[@title='Offset account']", "110110")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Ok']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Ok']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='NewLine']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='NewLine']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Clicking button: Grid
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
# Inputting into: InventJournalTrans_ItemId
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'InventJournalTrans_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
    #clicking inside grid: InventJournalTrans_ItemId
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'InventJournalTrans_ItemId')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'InventJournalTrans_ItemId')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'InventJournalTrans_ItemId')])[1]", "A0001")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
          Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "A0001")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'InventJournalTrans_ItemId')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'InventJournalTrans_ItemId')]", "A0001")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "A0001")
    Interactions.press_enter(driver, By.XPATH, "//body")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='checkJournal']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='checkJournal']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Validate']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Validate']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='postJournal']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='postJournal']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Post']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Post']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
time.sleep(5)
print("test case passed")
driver.quit()