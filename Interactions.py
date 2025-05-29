import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import re

from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


def js_click(driver, by, value, timeout=10):
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((by, value)))
    driver.execute_script("arguments[0].click();", element)

def extract_navigation_steps(description):
    if not description or "Go to " not in description:
        return []

    # Extract the part after "Go to"
    path = description.split("Go to ", 1)[-1].strip()

    # Remove trailing period
    if path.endswith("."):
        path = path[:-1]

    # Split by '>' and strip extra spaces
    steps = [step.strip() for step in path.split(">")]

    return steps

# def wait_and_click(driver, by, value, timeout=20):
#     # Wait for element to be present
#     element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
#     # if(check_element_exist(driver, by, "//div[contains(@class,'popupShadow popupView preview')]")):
#     #     element.click()
#     # Get the aria-expanded attribute (if any)
#     aria_expanded = element.get_attribute("aria-expanded")
#     flag = False
#     if(element): 
#         flag = True
#         if aria_expanded is not None:
#         # print(f"aria-expanded attribute found: {aria_expanded}")
#             if aria_expanded.lower() == "false":
#                 driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
#                 WebDriverWait(driver, timeout).until(
#                 EC.element_to_be_clickable((by, value))
#             )
#                 element.click()
#         else:
#             # print("aria-expanded not found. Clicking by default.")
#             driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
#             WebDriverWait(driver, timeout).until(
#             EC.element_to_be_clickable((by, value))
#             )
#             element.click()
#     time.sleep(2)
#     return flag;  

def wait_and_click(driver, by, base_xpath, timeout=10, enable_fallback=True):
    try:
        # Wait for the element to be present
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, base_xpath))
        )

        aria_expanded = element.get_attribute("aria-expanded")

        # Determine if we need to click
        if aria_expanded is None or aria_expanded.lower() == "false":
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, base_xpath)))
            ActionChains(driver).move_to_element(element).perform()
            element.click()
            print(f"Clicked element with base_xpath: {base_xpath}")
        else:
            print(f"Element already expanded (aria-expanded='{aria_expanded}') - Skipping click")

    except Exception as e:
        print(f"Primary click failed on base_xpath: {base_xpath} - {str(e)}")

        if enable_fallback and base_xpath:
            # Try fallback by clicking indexed variants
            for i in range(1, 20):
                indexed_xpath = f"({base_xpath})[{i}]"
                try:
                    fallback_element = WebDriverWait(driver, timeout).until(
                        EC.element_to_be_clickable((by, indexed_xpath))
                    )
                    driver.execute_script("arguments[0].click();", fallback_element)
                    print(f"Successfully clicked fallback element at index {i}")
                    break
                except Exception as ex:
                    print(f"Attempt {i} failed for xpath: {indexed_xpath} - {str(ex)}")
        else:
            print(f"No fallback attempted or no base_xpath provided. Exception: {str(e)}")

    time.sleep(1) 
        
def hover_on_an_element(driver, by, value, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(2)

def mouse_click(driver, by, value, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()

# Scroll into view just in case
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.3)

# Click using JavaScript
    driver.execute_script("arguments[0].click();", element)

def wait_and_send_keys(driver, by, value, keys,timeout=20):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(0.5)
    element.click()
    element.send_keys(keys)
    time.sleep(1)
    # element.send_keys(Keys.RETURN)

def wait_send_keys_and_enter(driver, by, value,keys,timeout=20):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    ActionChains(driver).move_to_element(element).perform()
    element.click()
    element.clear()
    time.sleep(0.5)
    element.send_keys(keys)
    time.sleep(0.5)
    element.send_keys(Keys.ENTER)

def check_element_exist(driver, by, value, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return True
    except TimeoutException:
        return False
    except Exception as e:
        print(f"Unexpected error in check_element_exist: {e}")
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
    try:
        # Wait for the element to be clickable and store it
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
        time.sleep(0.5)  # Short buffer time before interaction
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(keys)
        time.sleep(1)  # Give the page time to register input

    except Exception as e:
        print(f"Error in clear_input_field_and_send_keys: {e}")


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
    


def check_element_has_class(driver, by, locator, class_name, timeout=20):
    """
    Checks if the element's 'class' attribute contains a specific class name.

    Args:
        driver: Selenium WebDriver instance.
        by: Locator strategy (By.XPATH, By.ID, etc.).
        locator: The actual locator value.
        class_name: The class name to check for.
        timeout: Time to wait for the element (default 20 seconds).

    Returns:
        True if class name exists, False otherwise.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        classes = element.get_attribute("class")
        if classes:
            return class_name in classes.split()
        else:
            return False
    except TimeoutException:
        return False
    

def get_element_text(driver, by, locator, timeout=20):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        return element.text
    except TimeoutException:
        return None
    

def normalize_description_quotes(description):
    # Replace values inside double quotes with single quotes
    return re.sub(r'"([^"]+)"', r"'\1'", description)

def extract_value_and_operator_from_description(description):
    description = normalize_description_quotes(description)
    pattern = r"Enter a filter value of '(.+)' on the '(.+)' field using the '(.+)' filter operator."
    match = re.match(pattern, description)
    if match:
        value = match.group(1)
        field_name = match.group(2)
        operator = match.group(3)
        return {"value":value, "operator":operator, "field_name":field_name}
    else:
        return None, None
    

# def extract_multiple_values(description):
#     description = normalize_description_quotes(description)
#     pattern = r"Enter a filter value of '(.+)' on the '(.+)' field using the '(.+)' filter operator."
#     match = re.match(pattern, description)
#     if match:
#         value = match.group(1)
#         values_list = [v.strip() for v in value.split('/')]
#         return values_list
#     else:
#         return None
    
def extract_multiple_values(value_string):
    return [v.strip() for v in value_string.split('/')]

def extract_dates(date_str):
    parts = date_str.split('/')
    if len(parts) != 6:
        raise ValueError("Input string must contain two dates in the format dd/mm/yyyy/dd/mm/yyyy")
    
    from_date = f"{parts[0]}/{parts[1]}/{parts[2]}"
    to_date = f"{parts[3]}/{parts[4]}/{parts[5]}"
    
    return [from_date, to_date]


def click_back_button(driver, by, base_xpath,timeout=10):
    for i in range(1,100):
        # print("Attempt:", i)
        xpath = f"({base_xpath})[{i}]"
        try:
            close_button = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, xpath))
            )
            close_button.click()
            print(f"Successfully clicked button at index {i}")
            break
        except Exception as e:
            print(f"Attempt {i} failed for xpath : {xpath}")

# def scroll_and_click_row(driver, by, container_xpath, target_xpath, timeout=10, max_scrolls=20):
#     time.sleep(2)
#     try:
#         actions = ActionChains(driver)
#         container = WebDriverWait(driver, timeout).until(
#             EC.presence_of_element_located((by, container_xpath))
#         )
#         scroll_driection = None
#         count = container.get_attribute("aria-rowcount")
#         if(check_element_exist(driver, by, f"//div[contains(@class,'fixedDataTableRowLayout_')]/div[@aria-rowindex='{count}']")):
#             scroll_driection = Keys.PAGE_UP
#         else:
#             scroll_driection = Keys.PAGE_DOWN
#         for _ in range(max_scrolls):
#             try:
#                 element_to_click = WebDriverWait(driver, 1).until(
#                     EC.visibility_of_element_located((by, target_xpath))
#                 )
#                 element_to_click.click()
#                 return
#             except TimeoutException:
#                 actions.move_to_element(container).click().send_keys(scroll_driection).perform()
#                 time.sleep(0.5)

#         raise TimeoutException(f"Element {target_xpath} not found after scrolling.")

#     except TimeoutException as e:
#         print(f"Timeout: {e}")

def check_input_ancestor_is_table(driver, by, value_xpath, timeout=10):
    """
    Check if the input element (given by value_xpath) has a visible ancestor 
    with a specific class (e.g. part of a fixed data table row).
    """
    try:
        ancestor_xpath = f"{value_xpath}/ancestor::div[contains(@class,'fixedDataTableRowLayout_rowWrapper')]"
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, ancestor_xpath))
        )
        return element.is_displayed()
    except TimeoutException:
        return False
   
    

def extract_quickfilter_value(description):
    match = re.search(r"with a value of '([^']+)'", description)
    if match:
        return match.group(1)
    return None


def scroll_and_click_row(driver, by, container_xpath, target_xpath, timeout=10, max_scrolls=1000):
    time.sleep(2)
    # Try multiple container elements (if indexed)
    for i in range(1, 10):
        indexed_xpath = f"({container_xpath})[{i}]"
        try:
            container = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, indexed_xpath))
            )
            
            if container.is_displayed():
                print(f"Container found: {indexed_xpath}")
                actions = ActionChains(driver)

                # Determine scroll direction
                count = container.get_attribute("aria-rowcount")
                last_row_xpath = f"//div[contains(@class,'fixedDataTableRowLayout_')]/div[@aria-rowindex='{count}']"
                first_row_xpath = f"//div[contains(@class,'fixedDataTableRowLayout_')]/div[@aria-rowindex='2']"
                scroll_direction = None
                if check_element_exist(driver, by, last_row_xpath):
                    scroll_direction = Keys.PAGE_UP
                elif check_element_exist(driver, by, first_row_xpath):
                    scroll_direction = Keys.PAGE_DOWN

                for _ in range(max_scrolls):
                    try:
                        element_to_click = WebDriverWait(driver, 8).until(
                            EC.visibility_of_element_located((by, target_xpath))
                        )
                        element_to_click.click()
                        print(f"Clicked element: {target_xpath}")
                        return
                    except TimeoutException:
                        actions.move_to_element(container).click().send_keys(scroll_direction).perform()
                        time.sleep(0.5)

                raise TimeoutException(f"Element {target_xpath} not found after scrolling.")

        except TimeoutException as e:
            print(f"Timeout or not displayed: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    print("Visible container not found.")



def scroll_right(driver, by, container_xpath, target_xpath, target_xpath_2, timeout=10, max_scrolls=1000):
    time.sleep(2)
    for i in range(1, 10):
        indexed_xpath = f"({container_xpath})[{i}]"
        try:
            container = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, indexed_xpath))
            )

            if container.is_displayed():
                print(f"Container found: {indexed_xpath}")
                actions = ActionChains(driver)

                scroll_key = Keys.ARROW_RIGHT
                scroll_amount = 200  # pixels for JS scroll
                for _ in range(max_scrolls):
                    try:
                        if check_element_exist(driver, by, target_xpath):
                            element_to_click = WebDriverWait(driver, 5).until(
                                EC.visibility_of_element_located((by, target_xpath))
                            )
                            element_to_click.click()
                            print(f"Clicked element: {target_xpath}")
                            return

                        elif check_element_exist(driver, by, target_xpath_2):
                            element_to_click = WebDriverWait(driver, 5).until(
                                EC.visibility_of_element_located((by, target_xpath_2))
                            )
                            element_to_click.click()
                            print(f"Clicked element: {target_xpath_2}")
                            return

                    except TimeoutException:
                        # Try ActionChains key scroll
                        try:
                            actions.move_to_element(container).click().send_keys(scroll_key).perform()
                        except:
                            pass
                        # Try JavaScript pixel scroll
                        try:
                            driver.execute_script("arguments[0].scrollLeft += arguments[1];", container, scroll_amount)
                        except Exception as e:
                            print(f"JS scroll error: {e}")

                        time.sleep(0.5)

                raise TimeoutException(f"Element {target_xpath} not found after scrolling.")
        except TimeoutException as e:
            print(f"Timeout or not displayed for container: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    print("Visible container not found.")

def scroll_into_view(driver, by, value, timeout=10):
    """
    Scrolls the specified element into view using JavaScript.
    Args:
        driver: Selenium WebDriver instance.
        by: Locator strategy (By.XPATH, By.ID, etc.).
        value: The actual locator value.
        timeout: Time to wait for the element (default 10 seconds).
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        time.sleep(0.5)  # Optional wait after scrolling
         # Click the element after scrolling
    except TimeoutException:
        print(f"Element not found for scrolling: {value}")