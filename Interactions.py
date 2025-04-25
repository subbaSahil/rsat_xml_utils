import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

def wait_and_click(driver, by, value, timeout=20):
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
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
                WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
                element.click()
        else:
            # print("aria-expanded not found. Clicking by default.")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
            WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
            )
            element.click()
    time.sleep(2)
    return flag;  
        

def wait_and_send_keys(driver, by, value, keys,timeout=20):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()
    element.send_keys(keys)
    time.sleep(2) 
def check_element_exist(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return True
    except TimeoutException:
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

def clear_input_field_and_send_keys(driver, by, value, keys, timeout=20):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()
    time.sleep(0.5)  # brief wait before sending keys
    element.send_keys(Keys.CONTROL + "a")  # Select all text
    element.send_keys(Keys.DELETE)
    element.send_keys(keys)         # Send the desired keys
    time.sleep(1) 
    # if press_enter:


def no_of_elements_present(driver, by, value, timeout=20):
    try:
        elements = WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((by, value))
        )
        return len(elements)
    except TimeoutException:
        return 0

def get_locator(driver, by, value,):
    try:
        if(no_of_elements_present(driver, by, value)>1):
            print("Multiple elements found")
            return "("+value+")[1]"
        return value
    except TimeoutException:
        return None

def press_enter(driver, by, value, timeout=20):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.send_keys(Keys.ENTER)
    