import xml.etree.ElementTree as ET
import re

from selenium.webdriver.common.by import By
from getLocatorFromControls import generate_xpath_from_control
XML_PATH = "output.xml"
OUTPUT_SCRIPT = "rsat_script.py"



def convert_date_format(date_str):
    """Convert date from YYYY-MM-DD to DD/MM/YYYY format."""
    from datetime import datetime
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%m/%d/%Y")
    except ValueError:
        return "Invalid date format"

def extract_navigation_from_description(root):
    """Extract navigation items from <Description> text."""
    description_navs = []
    for elem in root.findall(".//UserAction"):
        desc_elem = elem.find("Description")
        if desc_elem is not None and desc_elem.text:
            match = re.search(r"Go to (.+)", desc_elem.text)
            if match:
                nav_items = [item.strip().strip('.') for item in re.split(r">|&gt;", match.group(1))]
                for item in nav_items:
                    if item:
                        description_navs.append(item)
    return description_navs

import re

def extract_controls_with_types(root):
    controls = []

    def get_quickfilter_value_from_description(elem):
        """
        Extract the value from the Description tag, specifically for quickfilter and filtermanager controls.
        Prioritizes:
        - Values in single quotes (e.g. '000008') for Quick Filter instructions.
        - Values in double quotes (e.g. "100") for filter instructions.
        """
        description_elem = elem.find("Description")
        if description_elem is not None and description_elem.text:
            desc_text = description_elem.text.strip()

            # Priority 1: Match value in single quotes
            single_match = re.search(r"'([^']+)'", desc_text)
            if single_match:
                return single_match.group(1)

            # Priority 2: Match value in double quotes
            double_match = re.search(r'"([^"]+)"', desc_text)
            if double_match:
                return double_match.group(1)

        return None
    
    def extract_target_field(elem):
        """
        Extract field name like 'Vendor account' from description such as:
        'Open Vendor account column filter.'
        """
        description_elem = elem.find("Description")
        if description_elem is not None and description_elem.text:
            match = re.search(r'Open (.*?) column filter\.', description_elem.text.strip())
            if match:
                return match.group(1)
        return ""

    for elem in root.iter():
        label = None
        control_name = None
        control_type = None
        value = None
        filtervalue = None
        manageFilterLocator = None

        for child in elem:
            tag = child.tag.split('}')[-1]
            if tag == "ControlLabel":
                label = child.text.strip() if child.text else None
            elif tag == "ControlName":
                control_name = child.text.strip() if child.text else None
            elif tag == "ControlType":
                control_type = child.text.strip().lower() if child.text else None
                if control_type in ("quickfilter", "filtermanager"):
                    filtervalue = get_quickfilter_value_from_description(elem)
                    manageFilterLocator = extract_target_field(elem)
            elif tag == "Value":
                value = child.text.strip() if child.text else None

        if control_name and control_type:
            controls.append({
                "label": label or "",
                "name": control_name,
                "type": control_type or "",
                "value": value or "",
                "filtervalue": filtervalue or "",
                "manageFilterLocator": manageFilterLocator or ""
            })

    return controls


def generate_selenium_script(nav_keys, controls):
    lines = [
        "from selenium import webdriver",
        "from selenium.webdriver.common.by import By",
        "from selenium.webdriver.common.keys import Keys",
        "import time\n",
        "import login",
        "import Interactions",
        "driver = webdriver.Chrome()",
        "driver.maximize_window()",
        "time.sleep(3)\n",
        "login.login(driver)\n",
        "locator = \"\"\n",
        "Interactions.wait_and_click(driver, By.XPATH, \"//div[@aria-label='Modules']\")"

    ]

    for key in nav_keys:
        xpath = f"//a[@data-dyn-title='{key}']"
        lines.append(f"# Clicking navigation: {key}")
        lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
        lines.append("time.sleep(1)\n")

    for control in controls:
        label = control["label"]
        name = control["name"]
        ctype = control["type"]
        value = control["value"]
        filtervalue = control["filtervalue"]
        xpath = generate_xpath_from_control(ctype, name,label)
        # print(xpath)

        if xpath:
            if ctype in ["input" , "referencegroup"] :
                lines.append(f"# Inputting into: {name}")
                # xpath_controlname = xpath[0]+"/following-sibling::div"
                lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                lines.append(f"    locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[0]}\")")
                lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, locator, \"{value}\")")
                lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                lines.append(f"    locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[1]}\")")
                lines.append(f"    print(locator)")
                lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, locator, \"{value}\")")
            
            elif ctype in["quickfilter", "filtermanager"]:
                lines.append(f"# Inputting into: {name}")
                # xpath_controlname = xpath[0]+"/following-sibling::div"
                lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                lines.append(f"    locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[0]}\")")
                lines.append(f"    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, \"{filtervalue}\")")
                lines.append(f"    Interactions.press_enter(driver, By.XPATH, locator)")
                lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                lines.append(f"    locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[1]}\")")
                lines.append(f"    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, locator, \"{filtervalue}\")")
                lines.append(f"    Interactions.press_enter(driver, By.XPATH, locator)")
            
            elif ctype == "date":
                date = convert_date_format(value)
                lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                lines.append(f"    Interactions.get_locator(driver, By.XPATH, \"{xpath[1]}\")")
                lines.append(f"    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{xpath[0]}\", \"{date}\")")
                lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                lines.append(f"    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{xpath[1]}\", \"{date}\")")
            elif ctype == "real":
                lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                lines.append(f"    Interactions.get_locator(driver, By.XPATH, \"{xpath[1]}\")")
                lines.append(f"    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{xpath[0]}\", \"{value}\")")
                lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                lines.append(f"    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{xpath[1]}\", \"{value}\")")

            elif ctype == "commandbutton" or ctype == "checkBox":
                lines.append(f"# Clicking button: {name}")
                lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")

            elif ctype == "multilineinput":
                lines.append(f"# Inputting into: {name}")
                lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath}\")):")
                lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, \"{xpath}\", \"{value}\")")
            else:
                lines.append(f"# Clicking (default) on: {name}")
                lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
        else:
            lines.append(f"# ❌ Locator not found for: {name} (Type: {ctype})")

    lines.append("time.sleep(5)")
    lines.append("print(\"test case passed\")")
    lines.append("driver.quit()")
    return "\n".join(lines)

# Main logic
tree = ET.parse(XML_PATH)
root = tree.getroot()

# Combine and deduplicate navigation keys
navigation_keys = list(dict.fromkeys(extract_navigation_from_description(root)))

# Get controls
controls = extract_controls_with_types(root)

# Generate and write script
selenium_code = generate_selenium_script(navigation_keys, controls)

with open(OUTPUT_SCRIPT, "w", encoding="utf-8") as f:
    f.write(selenium_code)

print(f"✅ Selenium script generated in: {OUTPUT_SCRIPT}")