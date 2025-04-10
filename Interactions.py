import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def wait_and_click(driver, by, value, timeout=10):
    # Wait for element to be present
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

    # Get the aria-expanded attribute (if any)
    aria_expanded = element.get_attribute("aria-expanded")

    if aria_expanded is not None:
        print(f"aria-expanded attribute found: {aria_expanded}")
        if aria_expanded.lower() == "false":
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
            element.click()
    else:
        print("aria-expanded not found. Clicking by default.")
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
        element.click()
    time.sleep(2)

def wait_and_send_keys(driver, by, value, keys, press_enter=True, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()
    element.send_keys(keys)
    time.sleep(2) 
    if press_enter:
        element.send_keys(Keys.RETURN)
     # Optional: wait for the action to complete