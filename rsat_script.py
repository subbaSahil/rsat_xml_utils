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
# Clicking navigation: Procurement and sourcing
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Procurement and sourcing']")
# Clicking navigation: Vendors
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Vendors']")
# Clicking navigation: All vendors
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All vendors']")
     user_input = input("Press data to select: ")
     Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']")
     Interactions.press_enter(driver, By.XPATH, "//input[@value='"+user_input+"']")
# Clicking (default) on: VendorTab
     time.sleep(3)
     Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='VendorTab']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='OnHoldDropDialogButton']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='OnHoldDropDialogButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='On hold']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='On hold']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='OnHoldDropDialogButton']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='OnHoldDropDialogButton']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='On hold']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='On hold']")
# Clicking combobox: OnHold
     combox_box_to_click = None
     if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='OnHold']/following-sibling::div"):
          combox_box_to_click = "//input[@name='OnHold']/following-sibling::div"
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[@aria-label='Vendor hold']/following-sibling::div"):
          combox_box_to_click = "//input[@aria-label='Vendor hold']/following-sibling::div"
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[@name='OnHold']/parent::div/following-sibling::div/div"):
          combox_box_to_click = "//input[@name='OnHold']/parent::div/following-sibling::div/div"
     Interactions.wait_and_click(driver, By.XPATH, combox_box_to_click)
     if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'OnHold')]//li[@data-dyn-index='2']"):
          Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'OnHold')]//li[@data-dyn-index='2']")
     elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id,'OnHold')]//li[2]"):
          Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@id,'OnHold')]//li[2]")
     else:
          if Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'OnHold')]"):
                 cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'OnHold')]",By.XPATH, "//ul[contains(@aria-labelledby, 'OnHold')]//li[@data-dyn-index='2']")
                 if cliked_or_not == False:
                     Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@aria-labelledby, 'OnHold')]",By.XPATH, "//ul[contains(@id,'OnHold')]//li[2]")
          elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@id, 'OnHold')]"):
                 cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'OnHold')]",By.XPATH, "//ul[contains(@aria-labelledby, 'OnHold')]//li[@data-dyn-index='2']")
                 if cliked_or_not == False:
                     Interactions.scroll_and_click_dropdown_item(driver, "//ul[contains(@id, 'OnHold')]",By.XPATH, "//ul[contains(@id,'OnHold')]//li[2]")
# Inputting into: ReasonCode
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'ReasonCode')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Reason code')]") ):
         #clicking inside grid: ReasonCode
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'ReasonCode')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'ReasonCode')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'ReasonCode')])[1]", "QUALITY")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Reason code')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Reason code')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Reason code')])[1]", "QUALITY")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'ReasonCode')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'ReasonCode')]", "QUALITY")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Reason code')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Reason code')]", "QUALITY")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid selection due input in the ancestor"
     if Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'BlockedReleaseDate')]"):
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'BlockedReleaseDate')]", "11/30/2025 12:00 AM")
     elif Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Vendor hold release date')]"):
         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Vendor hold release date')]", "11/30/2025 12:00 AM")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='CommandButtonOK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='CommandButtonOK']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
     Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Procurement and sourcing
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Procurement and sourcing']")
# Clicking navigation: Purchase orders
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Purchase orders']")
# Clicking navigation: All purchase orders
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All purchase orders']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='SystemDefinedNewButton']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: PurchTable_OrderAccount
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]") ):
         #clicking inside grid: PurchTable_OrderAccount
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_OrderAccount')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]", "")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Vendor account')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]", "")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]", "")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]", "")
     Interactions.press_enter(driver, By.XPATH, "//body")
# Inputting into: PurchTable_OrderAccount
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]") ):
         #clicking inside grid: PurchTable_OrderAccount
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_OrderAccount')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]", "checkgrid2")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Vendor account')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]", "checkgrid2")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]", "checkgrid2")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]", "checkgrid2")
     Interactions.press_enter(driver, By.XPATH, "//body")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Close']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Close']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Close']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Close']")
# Inputting into: PurchTable_OrderAccount
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]") ):
         #clicking inside grid: PurchTable_OrderAccount
         if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'PurchTable_OrderAccount')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'PurchTable_OrderAccount')])[1]", "checkgrid2")
         elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Vendor account')]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Vendor account')])[1]", "checkgrid2")
     else:
         if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'PurchTable_OrderAccount')]", "checkgrid2")
         elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]")):
              Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Vendor account')]", "checkgrid2")
     Interactions.press_enter(driver, By.XPATH, "//body")
#    "Skipping grid since previous was control was input"
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Cancel']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Cancel']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Cancel']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Cancel']")
# Closing the page
     Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
     time.sleep(1)
     Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts payable
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts payable']")
# Clicking navigation: Payments
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Payments']")
# Clicking navigation: Vendor payment journal
     Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Vendor payment journal']")
#    "Skipping grid since it is deafault behavior of d365"
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='JournalLines']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='JournalLines']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Lines']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Lines']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='JournalLines']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='JournalLines']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Lines']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Lines']")
#    "Skipping grid since it is deafault behavior of d365"
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='PostJournal']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@name='PostJournal']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Post']")):
          Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Post']")
     else:
          Interactions.wait_and_click(driver, By.XPATH, "//div[@data-dyn-controlname='ActionPane']//div[@class='appBar-toolbar']//div[@data-dyn-role='OverflowButton']")
          if(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='PostJournal']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@name='PostJournal']")
          elif(Interactions.check_element_exist(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Post']")):
               Interactions.wait_and_click(driver, By.XPATH, "//div[@class='overflow-menu sysPopup allowFlyoutClickPropagation']//button[@aria-label='Post']")
     if(Interactions.check_element_exist(driver, By.XPATH, "//button[@name='Close']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@name='Close']")
     elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Close']")):
         Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Close']")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
# Inputting into: LedgerJournalTrans_AccountNum
     if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]") ):
          #clicking inside grid: LedgerJournalTrans_AccountNum
           if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//input[contains(@name,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]")):
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')])[1]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[contains(@id,'LedgerJournalTrans_AccountNum')])[1]")).perform()
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//input[@title='Account'])[1]")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "(//input[@title='Account'])[1]", "1001")
     else:
           if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@name,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Account') and contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]")):
               Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[contains(@id,'LedgerJournalTrans_AccountNum')]", "1001")
           else:
                ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//input[@title='Account']")).perform()
                Interactions.clear_input_field_and_send_keys(driver, By.XPATH, "//input[@title='Account']", "1001")
except Exception as e:
     test_passed = False
     Interactions.take_screenshot_on_pass(driver, "test_case_passed")
     print("Test case failed:"+ e)
finally:
     driver.quit()
     if test_passed:
          print("✅ Test case passed")
     else:
          print("❌ Test case failed")