import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def wait_and_click(driver, by, value, timeout=10):
    # Wait for element to be present
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

    # Get the aria-expanded attribute (if any)
    aria_expanded = element.get_attribute("aria-expanded")
    flag = False
    if(element): 
        flag = True
        if aria_expanded is not None:
        # print(f"aria-expanded attribute found: {aria_expanded}")
            if aria_expanded.lower() == "false":
                WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
                element.click()
        else:
            # print("aria-expanded not found. Clicking by default.")
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
            element.click()
    time.sleep(2)
    return flag;  
        

def wait_and_send_keys(driver, by, value, keys,timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    # element.click()
    element.clear()
    element.send_keys(keys)
    time.sleep(2) 
    # if press_enter:
    #     element.send_keys(Keys.RETURN)
     # Optional: wait for the action to complete
def check_element_exist(driver, by, value, timeout=10):
    element = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((by, value))
    )
    if element:
        return True
    return False

def checkInputExpanded(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
        )
        aria_expanded = element.get_attribute("aria-expanded")
        if aria_expanded is not None:
            if aria_expanded.lower() == "false":
                return False
            else:
                return True
    except:
        return False

def clearInputField(driver, by, value, keys,timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.clear()
    time.sleep(2)
    # if press_enter: