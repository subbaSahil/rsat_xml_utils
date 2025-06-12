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
# Clicking navigation: Product information management
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Product information management']")
# Clicking navigation: Products
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Products']")
# Clicking navigation: Released products
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Released products']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: Identification_ProductNumber
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Identification_ProductNumber')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Product number')]") ):
         #clicking inside grid: Identification_ProductNumber
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Identification_ProductNumber')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Identification_ProductNumber')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Identification_ProductNumber')])[1]", "A0054")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Product number')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Product number')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Product number')])[1]", "A0054")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Identification_ProductNumber')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Identification_ProductNumber')]", "A0054")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Product number')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Product number')]", "A0054")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: Identification_Name
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Identification_Name')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Product name')]") ):
         #clicking inside grid: Identification_Name
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Identification_Name')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Identification_Name')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Identification_Name')])[1]", "Phone")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Product name')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Product name')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Product name')])[1]", "Phone")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Identification_Name')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Identification_Name')]", "Phone")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Product name')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Product name')]", "Phone")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: ModelGroupId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'ModelGroupId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item model group')]") ):
         #clicking inside grid: ModelGroupId
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'ModelGroupId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'ModelGroupId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'ModelGroupId')])[1]", "FIFO")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item model group')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item model group')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item model group')])[1]", "FIFO")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'ModelGroupId')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'ModelGroupId')]", "FIFO")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item model group')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item model group')]", "FIFO")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
# Inputting into: ItemGroupId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'ItemGroupId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item group')]") ):
         #clicking inside grid: ItemGroupId
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'ItemGroupId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'ItemGroupId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'ItemGroupId')])[1]", "Charger-gr")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item group')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item group')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item group')])[1]", "Charger-gr")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'ItemGroupId')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'ItemGroupId')]", "Charger-gr")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item group')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item group')]", "Charger-gr")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
#    "Skipping grid selection due input in the ancestor"
# clicking dropdown for Tree
     Interactions.wait_and_click(driver, By.XPATH, "//input[contains(@name,'StorageDimensionGroup')]/parent::div/parent::div/following-sibling::div/div")
# Clicking button: Grid
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
#    "Skipping grid selection due input in the ancestor"
# clicking dropdown for Tree
     Interactions.wait_and_click(driver, By.XPATH, "//input[contains(@name,'TrackingDimensionGroup')]/parent::div/parent::div/following-sibling::div/div")
# Clicking button: Grid
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
#    "Skipping grid selection due input in the ancestor"
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchasePrice')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Purchase price')]") ):
         #clicking inside grid: PurchasePrice
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchasePrice')])[1]")):
              ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'PurchasePrice')])[1]")).perform()
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchasePrice')])[1]", "400.00")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase price')])[1]")):
              ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@aria-label,'Purchase price')])[1]")).perform()
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Purchase price')])[1]", "400.00")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchasePrice')]")):
              ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchasePrice')]")).perform()
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchasePrice')]", "400.00")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Purchase price')]")):
              ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@aria-label,'Purchase price')]")).perform()
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Purchase price')]", "400.00")
         Interactions.press_enter(driver, By.XPATH, "//body")
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'SalesPrice')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Sales price')]") ):
         #clicking inside grid: SalesPrice
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'SalesPrice')])[1]")):
              ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@name,'SalesPrice')])[1]")).perform()
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'SalesPrice')])[1]", "500.00")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Sales price')])[1]")):
              ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"(//input[contains(@aria-label,'Sales price')])[1]")).perform()
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Sales price')])[1]", "500.00")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'SalesPrice')]")):
              ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'SalesPrice')]")).perform()
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'SalesPrice')]", "500.00")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Sales price')]")):
              ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@aria-label,'Sales price')]")).perform()
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Sales price')]", "500.00")
         Interactions.press_enter(driver, By.XPATH, "//body")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OKButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OKButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
# Clicking (default) on: ActionPaneTabDefine
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='ActionPaneTabDefine']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
# Clicking (default) on: ActionPaneTabEngineer
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='ActionPaneTabEngineer']")
# Inputting into: QuickFilter
     if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'QuickFilter')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@name,'QuickFilter')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "A0054")
         Interactions.press_enter(driver, By.XPATH, locator)
     elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'')]")):
         locator=Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'')]")
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, "A0054")
         Interactions.press_enter(driver, By.XPATH, locator)
#    "Skipping grid since it is deafault behavior of d365"
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='BOMConsistOfAction']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='BOMConsistOfAction']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='BOM versions']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='BOM versions']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='BOMConsistOfAction']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='BOMConsistOfAction']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='BOM versions']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='BOM versions']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewFormMenuButton']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewFormMenuButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='New']/ancestor::button")):
          Interactions.wait_and_click(driver, By.XPATH, "//span[text()='New']/ancestor::button")
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='BOMConsistOfAction']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='BOMConsistOfAction']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='BOM versions']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='BOM versions']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='BOMConsistOfAction']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='BOMConsistOfAction']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='BOM versions']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='BOM versions']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewFormMenuButton']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewFormMenuButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='New']/ancestor::button")):
          Interactions.wait_and_click(driver, By.XPATH, "//span[text()='New']/ancestor::button")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='CreateBOM']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='CreateBOM']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//span[text()='BOM and BOM version']/ancestor::button")):
          Interactions.wait_and_click(driver, By.XPATH, "//span[text()='BOM and BOM version']/ancestor::button")
# Inputting into: Fld2_1
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Fld2_1')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Name')]") ):
         #clicking inside grid: Fld2_1
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Fld2_1')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Fld2_1')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Fld2_1')])[1]", "Charger BOM")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Name')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]", "Charger BOM")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Fld2_1')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Fld2_1')]", "Charger BOM")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Name')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Name')]", "Charger BOM")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: Fld4_1
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Fld4_1')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Site')]") ):
         #clicking inside grid: Fld4_1
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Fld4_1')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'Fld4_1')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Fld4_1')])[1]", "1")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Site')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Site')])[1]", "1")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Fld4_1')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Fld4_1')]", "1")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Site')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Site')]", "1")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OkButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OkButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewBomLine']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewBomLine']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
#    "Skipping grid since it is deafault behavior of d365"
# Inputting into: BOM_ItemId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'BOM_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
         #clicking inside grid: BOM_ItemId
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'BOM_ItemId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'BOM_ItemId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'BOM_ItemId')])[1]", "SC000001")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "SC000001")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'BOM_ItemId')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'BOM_ItemId')]", "SC000001")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "SC000001")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='NewBomLine']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='NewBomLine']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: BOM_ItemId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'BOM_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
         #clicking inside grid: BOM_ItemId
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'BOM_ItemId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'BOM_ItemId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'BOM_ItemId')])[1]", "SC00003")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "SC00003")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'BOM_ItemId')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'BOM_ItemId')]", "SC00003")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "SC00003")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: BOM_ItemId
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'BOM_ItemId')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]") ):
         #clicking inside grid: BOM_ItemId
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'BOM_ItemId')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'BOM_ItemId')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'BOM_ItemId')])[1]", "")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Item number')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Item number')])[1]", "")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'BOM_ItemId')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'BOM_ItemId')]", "")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Item number')]", "")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Clicking button: Grid
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
#    "Skipping grid selection due input in the ancestor"
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='BOMApprove']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='BOMApprove']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Approval']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Approval']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='BOMApprove']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='BOMApprove']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Approval']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Approval']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OkButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OkButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
     if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'General_BOMVersion_FromDate')]")):
        Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'From date')]")
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'General_BOMVersion_FromDate')]", "06/04/2025")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'From date')]")):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'From date')]", "06/04/2025")
     if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'General_BOMVersion_ToDate')]")):
        Interactions.get_locator(driver, By.XPATH, "//input[contains(@aria-label,'To date')]")
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'General_BOMVersion_ToDate')]", "06/18/2025")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'To date')]")):
        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'To date')]", "06/18/2025")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedSaveButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='BOMVersionApprove']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='BOMVersionApprove']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Approval']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Approval']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='BOMVersionApprove']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='BOMVersionApprove']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Approval']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Approval']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OkButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OkButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='BOMRouteVersionActivate']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='BOMRouteVersionActivate']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Activate']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Activate']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='BOMRouteVersionActivate']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='BOMRouteVersionActivate']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Activate']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Activate']")
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