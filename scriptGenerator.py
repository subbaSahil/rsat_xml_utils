import xml.etree.ElementTree as ET
import re
import Interactions
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
    def extract_field_name_from_filtermanager(description_text):
        if description_text:
            match = re.search(r'Open (.*?) column filter\.', description_text.strip())
            if match:
                return match.group(1)
        return ""

    for elem in root.iter():
        label = None
        control_name = None
        control_type = None
        value = None
        filtervalue = None
        filterManagerLocator = None
        description = None
        annotation_present = False
        

        for child in elem:
            tag = child.tag.split('}')[-1]
            if tag == "ControlLabel":
                label = child.text.strip() if child.text else None
            elif tag == "ControlName":
                control_name = child.text.strip() if child.text else None  
            elif tag == "ControlType":
                control_type = child.text.strip().lower() if child.text else None
                if control_type == "filtermanager":
                    description_elem = elem.find("Description")
                    description_text = description_elem.text if description_elem is not None else ""
                    filterManagerLocator = extract_field_name_from_filtermanager(description_text)
            elif tag == "Value":
                value = child.text.strip() if child.text else None
            elif tag == "Description":
                description = child.text.strip() if child.text else None
            elif tag == "Annotations":
                # If Annotations has at least one child, it's present
                annotation_present = len(child.findall(".//*")) > 0


        if control_name and control_type:
            controls.append({
                "label": label or "",
                "name": control_name,
                "type": control_type or "",
                "value": value or "",
                "filtervalue": filtervalue or "",
                "filterManagerLocator": filterManagerLocator or "",
               "description": description or "",  # Now we'll always have this
                "annotation_present": annotation_present
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
        "filter_manager_cloumn_last_opened = \"\"",
        "filter_manager_dropdown_item_index = 1\n",
        "column_to_open = \"\"",
        "Interactions.wait_and_click(driver, By.XPATH, \"//div[@aria-label='Modules']\")\n"
        

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
        filterManagerLocator = control["filterManagerLocator"]
        description = control["description"]
        xpath = generate_xpath_from_control(ctype, name,label)

        if xpath:
            if ctype in ["input" , "referencegroup","segmentedentry"] :
                lines.append(f"# Inputting into: {name}")
                # xpath_controlname = xpath[0]+"/following-sibling::div"
                lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                lines.append(f"    locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[0]}\")")
                lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, locator, \"{value}\")")
                lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                lines.append(f"    locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[1]}\")")
                lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, locator, \"{value}\")")
            
            elif ctype in["quickfilter"]:
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
            elif ctype == "checkbox":
                lines.append(f"# Clicking checkbox: {name}")
                lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                lines.append(f"    Interactions.wait_and_click(driver, By.XPATH, \"{xpath[0]}\")")
                lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                lines.append(f"    Interactions.wait_and_click(driver, By.XPATH, \"{xpath[1]}\")")
                # lines.append(f"    Interactions.wait_and_click(driver, By.XPATH, \"//div[text()='{xpath[1]}']\")")
            elif ctype == "appbartab":
                lines.append(f"# Clicking (default) on: {name}")
                lines.append("time.sleep(3)")
                lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
            elif ctype == "filtermanager":
                if description.startswith("Open"):
                    lines.append(f"# Clicking filter manager: {name}")
                    lines.append(f"column_to_open = \"{filterManagerLocator}\"")
                    lines.append(f"open_divs = driver.find_elements(By.XPATH, \"//div/parent::div[contains(@class, 'dyn-headerCell')]\")")
                    lines.append("filter_manager_cloumn_last_opened = ''")
                    lines.append("for i, div in enumerate(open_divs, start=1):")
                    lines.append("    class_attr = div.get_attribute('class')")
                    lines.append("    if 'hasOpenPopup' in class_attr:")
                    lines.append("        filter_manager_cloumn_last_opened = Interactions.get_element_text(driver, By.XPATH, f\"(//div/parent::div[contains(@class, 'dyn-headerCell')])[{i}]\")")
                    lines.append("        print(f\"filter_manager_cloumn_last_opened: {filter_manager_cloumn_last_opened}\")")
                    lines.append("        break")
                    lines.append(f"if filter_manager_cloumn_last_opened == '{filterManagerLocator}' and filter_manager_cloumn_last_opened != '':")
                    lines.append(f"    Interactions.wait_and_click(driver, By.XPATH, \"//div[text()='{filterManagerLocator}']\")")
                    lines.append(f"    Interactions.wait_and_click(driver, By.XPATH, \"//div[text()='{filterManagerLocator}']\")")
                    lines.append("else:")
                    lines.append(f"    Interactions.wait_and_click(driver, By.XPATH, \"//div[text()='{filterManagerLocator}']\")")

                elif description.startswith("Sort"):
                    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"//input[contains(@aria-label,'Filter field: \"+column_to_open+\", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-sort']//span[text()='{description}']/ancestor::button\")")
                elif description.startswith("Click Clear"):
                    lines.append("Interactions.wait_and_click(driver, By.XPATH, \"//span[text()='Clear']/ancestor::button\")")
                elif description.startswith("Enter a filter value of"):
                    print(description)
                    description = Interactions.normalize_description_quotes(description)
                    # lines.append("Interactions.wait_and_click(driver, By.XPATH, \"//span[text()='Apply']/ancestor::button\")")
                    # lines.append("text=Interactions.get_element_text(driver, By.XPATH, \"//span[contains(@class,'button-label-dropDown')]/ancestor::button[contains(@class,'dynamicsButton')]/ancestor::div[@class='filterField-titleContainer']//button//span[@class='button-label button-label-dropDown']\")")
                    # lines.append("print(text)")
                    lines.append(f"filter_manager_data = Interactions.extract_value_and_operator_from_description(\"{description}\")")
                    lines.append("operator = filter_manager_data['operator']")
                    lines.append("new_val = filter_manager_data['value']")
                    lines.append("field_name = filter_manager_data['field_name']")
                    lines.append("drop_down_item = \"//input[contains(@aria-label,'Filter field: \"+field_name+\",')]/ancestor::div[@class='columnHeader-popup sysPopup']/ancestor::body/child::div[@class='sysPopup flyoutButton-flyOut layout-root-scope']//button//span[text()='\"+operator+\"']\"")
                    # lines.append("print(drop_down_item)")
                    lines.append("input_field = \"//input[contains(@aria-label,'Filter field: \"+field_name+\",')]\"")
                    lines.append("apply_button = \"//input[contains(@aria-label,'Filter field: \"+field_name+\", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-buttons']//span[text()='Apply']/ancestor::button\"")
                    lines.append("dropDown_button = \"//span[contains(@class,'button-label-dropDown')]/ancestor::button[contains(@class,'dynamicsButton')][ancestor::div[@class='filterFieldContainer']//input[contains(@aria-label,'Filter field: \"+field_name+\"')]]\"")
                    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, dropDown_button)")
                    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, drop_down_item)")
                    lines.append("if operator == 'is one of' or operator == 'matches':")
                    lines.append("    new_val = Interactions.extract_multiple_values(new_val)")
                    lines.append("    print(new_val)")
                    lines.append("    for new_val_value in new_val:")
                    lines.append("        Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val_value)")
                    lines.append("        Interactions.wait_and_click(driver, By.XPATH, apply_button)")
                    lines.append("elif operator == 'between':")
                    lines.append("    new_val = Interactions.extract_dates(new_val)")
                    lines.append("    from_date_locator = \"(//input[contains(@aria-label,'Filter field: \" + field_name + \",')])[1]\"")
                    lines.append("    to_date_locator = \"(//input[contains(@aria-label,'Filter field: \" + field_name + \",')])[2]\"")
                    lines.append("    Interactions.wait_and_send_keys(driver, By.XPATH, from_date_locator, new_val[0])")
                    lines.append("    Interactions.wait_and_send_keys(driver, By.XPATH, to_date_locator, new_val[1])")
                    lines.append("else:")
                    lines.append("    Interactions.wait_and_send_keys(driver, By.XPATH, input_field, new_val)")
                    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, apply_button)")
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