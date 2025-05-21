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
Interactions.wait_and_click(driver, By.XPATH, "//div[@aria-label='Modules']")
# Clicking navigation: Accounts receivable
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Accounts receivable']")
time.sleep(1)
# Clicking navigation: Customers
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Customers']")
time.sleep(1)
# Clicking navigation: Customers on hold
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Customers on hold']")
time.sleep(1)
# ❌ Locator not found for: No Control Name (Type: )
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='NewCustomer']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='NewCustomer']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: DynamicHeader_AccountNum
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'DynamicHeader_AccountNum')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]") ):
    #clicking inside grid: DynamicHeader_AccountNum
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'DynamicHeader_AccountNum')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DynamicHeader_AccountNum')])[1]", "US-012")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Customer account')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DynamicHeader_AccountNum')])[1]", "US-012")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DynamicHeader_AccountNum')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'DynamicHeader_AccountNum')]", "US-012")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Customer account')]", "US-012")
Interactions.send_enter(driver, By.XPATH, "//body")
# Clicking button: Grid
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']")
# Inputting into: Org_Name
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Org_Name')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Name')]") ):
    #clicking inside grid: Org_Name
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Org_Name')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Org_Name')])[1]", "Contoso Retail New York")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Name')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Org_Name')])[1]", "Contoso Retail New York")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Org_Name')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Org_Name')]", "Contoso Retail New York")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Name')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Name')]", "Contoso Retail New York")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Select']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Select']")
# Inputting into: DynamicDetail_CustGroup
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'DynamicDetail_CustGroup')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Customer group')]") ):
    #clicking inside grid: DynamicDetail_CustGroup
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'DynamicDetail_CustGroup')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DynamicDetail_CustGroup')])[1]", "40")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Customer group')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'DynamicDetail_CustGroup')])[1]", "40")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'DynamicDetail_CustGroup')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'DynamicDetail_CustGroup')]", "40")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Customer group')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Customer group')]", "40")
Interactions.send_enter(driver, By.XPATH, "//body")
# Clicking button: Grid
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='CancelButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='CancelButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Cancel']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Cancel']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='mibCustPackingSlipJournal']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='mibCustPackingSlipJournal']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Packing slips']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Packing slips']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransactVoucher']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransactVoucher']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Vouchers']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Vouchers']")
# Clicking button: OverviewGrid
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='TransactionLog']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='TransactionLog']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Audit trail']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Audit trail']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransact']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransact']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Voucher transactions']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Voucher transactions']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransAccount']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransAccount']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Transactions']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Transactions']")
# Clicking button: Identification
user_input = input("Press data to select: ")
Interactions.scroll_and_click_row(driver, By.XPATH, "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']", f"//input[@value='{user_input}']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransSettled']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransSettled']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Ledger settlements']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Ledger settlements']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransVoucher']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='LedgerTransVoucher']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Voucher']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Voucher']")
# Clicking (default) on: SystemDefinedOptions
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='SystemDefinedOptions']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='TaxTransactions']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='TaxTransactions']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Posted sales tax']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Posted sales tax']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Cov']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Cov']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Cash flow forecasts']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Cash flow forecasts']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='TaxTransactions']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='TaxTransactions']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Posted sales tax']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Posted sales tax']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
time.sleep(5)
print("test case passed")
driver.quit()