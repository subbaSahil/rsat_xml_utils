SIDE_NAVIGATION  = {
    "mainmenu": "//div[@aria-label='Modules']",
    "AccountsPayable": "//a[text()='Accounts payable']",
    "PurchaseOrders": "//a[text()='All purchase orders']"  
}

TOP_NAVIGATION  = {
    "Purchase order":"//span[text()='Purchase order']/parent::button",
    "New": "//span[text()='New']/ancestor::button",
    "Purchase":"//span[text()='Purchase']/parent::button",
    "Manage":"//span[text()='Manage']/parent::button",
    "Receive":"//span[text()='Receive']/parent::button",
    "Invoice":"//span[text()='Invoice']/parent::button",
    "Retail":"//span[text()='Retail']/parent::button",
    "Warehouse":"//span[text()='Warehouse']/parent::button",
    "Transportation":"//span[text()='Transportation']/parent::button",
    "General":"//span[text()='General']/parent::button",
    "Options":"//span[text()='Options']/parent::button"
}

INPUTS = {
    "Vendor account": "//input[@name='PurchTable_OrderAccount']",
    "Site" : "//input[@name='PurchTable_InventSiteId']",
    "Warehouse" : "//input[@name='PurchTable_InventLocationId']"     
}

CLICKS = {
    "OK": "//button[@data-dyn-controlname='OK']"
}