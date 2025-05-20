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
# Clicking navigation: Product information management
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Product information management']")
time.sleep(1)
# Clicking navigation: Products
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='Products']")
time.sleep(1)
# Clicking navigation: All products and product masters
Interactions.wait_and_click(driver, By.XPATH, "//a[@data-dyn-title='All products and product masters']")
time.sleep(1)

if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='EcoResProductInventoryDimensionGroups']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='EcoResProductInventoryDimensionGroups']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Dimension groups']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Dimension groups']")
# Inputting into: StorageDimensionGroup
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'StorageDimensionGroup')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Storage dimension group')]") ):
    #clicking inside grid: StorageDimensionGroup
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'StorageDimensionGroup')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'StorageDimensionGroup')])[1]", "Site")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Storage dimension group')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'StorageDimensionGroup')])[1]", "Site")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'StorageDimensionGroup')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'StorageDimensionGroup')]", "Site")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Storage dimension group')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Storage dimension group')]", "Site")
Interactions.send_enter(driver, By.XPATH, "//body")
# Inputting into: TrackingDimensionGroup
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'TrackingDimensionGroup')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Tracking dimension group')]") ):
    #clicking inside grid: TrackingDimensionGroup
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'TrackingDimensionGroup')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'TrackingDimensionGroup')])[1]", "Owner")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Tracking dimension group')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'TrackingDimensionGroup')])[1]", "Owner")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'TrackingDimensionGroup')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'TrackingDimensionGroup')]", "Owner")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Tracking dimension group')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Tracking dimension group')]", "Owner")
Interactions.send_enter(driver, By.XPATH, "//body")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='ProductAttributes']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='ProductAttributes']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Product attributes']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Product attributes']")
# Clicking (default) on: SystemDefinedOptions
time.sleep(3)
Interactions.wait_and_click(driver, By.XPATH, "//button/parent::div[@data-dyn-controlname='SystemDefinedOptions']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='EcoResProductNumberRename']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='EcoResProductNumberRename']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Change product number']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Change product number']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='CancelButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='CancelButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Cancel']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Cancel']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='ProductCategory']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='ProductCategory']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Product categories']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Product categories']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedNewButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: EcoResProductCategory_CategoryHierarchy
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_CategoryHierarchy')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Category hierarchy')]") ):
    #clicking inside grid: EcoResProductCategory_CategoryHierarchy
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_CategoryHierarchy')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_CategoryHierarchy')])[1]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Category hierarchy')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_CategoryHierarchy')])[1]", "")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_CategoryHierarchy')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_CategoryHierarchy')]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Category hierarchy')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Category hierarchy')]", "")
# ❌ Locator not found for: No Control Name (Type: )
# Inputting into: EcoResProductCategory_CategoryHierarchy_Name
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_CategoryHierarchy_Name')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Category hierarchy')]") ):
    #clicking inside grid: EcoResProductCategory_CategoryHierarchy_Name
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_CategoryHierarchy_Name')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_CategoryHierarchy_Name')])[1]", "REtail category2")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Category hierarchy')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_CategoryHierarchy_Name')])[1]", "REtail category2")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_CategoryHierarchy_Name')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_CategoryHierarchy_Name')]", "REtail category2")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Category hierarchy')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Category hierarchy')]", "REtail category2")
# Inputting into: EcoResProductCategory_CategoryHierarchy
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_CategoryHierarchy')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Category hierarchy')]") ):
    #clicking inside grid: EcoResProductCategory_CategoryHierarchy
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_CategoryHierarchy')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_CategoryHierarchy')])[1]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Category hierarchy')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_CategoryHierarchy')])[1]", "")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_CategoryHierarchy')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_CategoryHierarchy')]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Category hierarchy')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Category hierarchy')]", "")
# Inputting into: EcoResProductCategory_CategoryHierarchy_Name
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_CategoryHierarchy_Name')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Category hierarchy')]") ):
    #clicking inside grid: EcoResProductCategory_CategoryHierarchy_Name
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_CategoryHierarchy_Name')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_CategoryHierarchy_Name')])[1]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Category hierarchy')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_CategoryHierarchy_Name')])[1]", "")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_CategoryHierarchy_Name')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_CategoryHierarchy_Name')]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Category hierarchy')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Category hierarchy')]", "")
Interactions.send_enter(driver, By.XPATH, "//body")
# Inputting into: EcoResProductCategory_Category1
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_Category1')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Category')]") ):
    #clicking inside grid: EcoResProductCategory_Category1
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_Category1')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_Category1')])[1]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Category')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'EcoResProductCategory_Category1')])[1]", "")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_Category1')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'EcoResProductCategory_Category1')]", "")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Category')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Category')]", "")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OKButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='Yes']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Yes']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Yes']")
# Closing the page
Interactions.click_back_button(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedCloseButton']")
time.sleep(1)
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='ProductCatalog']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='ProductCatalog']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Product catalogs']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Product catalogs']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='NewCatalogButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='NewCatalogButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='New']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='New']")
# Inputting into: CatalogName
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'CatalogName')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Catalog name')]") ):
    #clicking inside grid: CatalogName
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'CatalogName')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'CatalogName')])[1]", "catalog newname")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Catalog name')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'CatalogName')])[1]", "catalog newname")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'CatalogName')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'CatalogName')]", "catalog newname")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Catalog name')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Catalog name')]", "catalog newname")
# Inputting into: CatalogTranslationDescription
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'CatalogTranslationDescription')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Description')]") ):
    #clicking inside grid: CatalogTranslationDescription
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'CatalogTranslationDescription')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'CatalogTranslationDescription')])[1]", "catalog desc")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Description')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'CatalogTranslationDescription')])[1]", "catalog desc")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'CatalogTranslationDescription')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'CatalogTranslationDescription')]", "catalog desc")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Description')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Description')]", "catalog desc")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OK']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='ExplodeVariantsButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='ExplodeVariantsButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Include all variants']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Include all variants']")
# Inputting into: Fld3_1
if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@name,'Fld3_1')]") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, "//input[contains(@aria-label,'Batch group')]") ):
    #clicking inside grid: Fld3_1
    if(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@name,'Fld3_1')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Fld3_1')])[1]", "AIFBatch")
    elif(Interactions.check_element_exist(driver, By.XPATH, "(//input[contains(@aria-label,'Batch group')])[1]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "(//input[contains(@name,'Fld3_1')])[1]", "AIFBatch")
else:
    if(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@name,'Fld3_1')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@name,'Fld3_1')]", "AIFBatch")
    elif(Interactions.check_element_exist(driver, By.XPATH, "//input[contains(@aria-label,'Batch group')]")):
         Interactions.wait_and_send_keys(driver, By.XPATH, "//input[contains(@aria-label,'Batch group')]", "AIFBatch")
Interactions.send_enter(driver, By.XPATH, "//body")
# Clicking checkbox: Fld1_1
if(Interactions.check_element_exist(driver, By.XPATH, "//label[contains(text(),'Batch processing')]/following-sibling::div/span[1]")):
    Interactions.wait_and_click(driver, By.XPATH, "//label[contains(text(),'Batch processing')]/following-sibling::div/span[1]")
elif(Interactions.check_element_exist(driver, By.XPATH, "//span[contains(@id, 'Fld1_1') and (@class='toggle-box' or @class='checkBox')]")):
    Interactions.wait_and_click(driver, By.XPATH, "//span[contains(@id, 'Fld1_1') and (@class='toggle-box' or @class='checkBox')]")
# Clicking combobox: Fld6_1
if Interactions.check_element_exist(driver, By.XPATH, "//input[@name='Fld6_1']"):
     Interactions.wait_and_click(driver, By.XPATH, "//input[@name='Fld6_1']")
elif Interactions.check_element_exist(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'Fld6_1')]//li[@data-dyn-index='4']"):
     Interactions.wait_and_click(driver, By.XPATH, "//ul[contains(@aria-labelledby, 'Fld6_1')]//li[@data-dyn-index='4']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='OkButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='OK']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='OK']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='ViewResults']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='ViewResults']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='View results']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='View results']")
if(Interactions.check_element_exist(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@data-dyn-controlname='SystemDefinedSaveButton']")
elif(Interactions.check_element_exist(driver, By.XPATH, "//button[@aria-label='Save']")):
     Interactions.wait_and_click(driver, By.XPATH, "//button[@aria-label='Save']")
time.sleep(5)
print("test case passed")
driver.quit()