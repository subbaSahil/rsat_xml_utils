import xml.etree.ElementTree as ET
import re

from selenium.webdriver.common.by import By

XML_PATH = "output.xml"
OUTPUT_SCRIPT = "rsat_script.py"

def generate_xpath_from_control(control_type, control_name):
    if control_type.lower() == "commandbutton":
        return f"//button[@data-dyn-controlname='{control_name}']"
    elif control_type.lower() == "input":
        return f"//input[contains(@name,'{control_name}')]"
    elif control_type.lower() == "appbartab":
        return f"//div[@data-dyn-controlname='{control_name}']"
    else:
        return f"//*[contains(@data-dyn-controlname, '{control_name}')]"

# def extract_navigation_keys(root):
#     """Extract values from <Navigation> tags."""
#     return [elem.text.strip() for elem in root.findall(".//Navigation") if elem.text]

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

def extract_controls_with_types(root):
    controls = []
    for elem in root.iter():
        label = None
        control_name = None
        control_type = None
        value = None

        for child in elem:
            tag = child.tag.split('}')[-1]
            if tag == "ControlLabel":
                label = child.text.strip() if child.text else None
            elif tag == "ControlName":
                control_name = child.text.strip() if child.text else None
            elif tag == "ControlType":
                control_type = child.text.strip().lower() if child.text else None
            elif tag == "Value":
                value = child.text.strip() if child.text else None

        if control_name and control_type:
            controls.append({
                "label": label or "",
                "name": control_name,
                "type": control_type or "",
                "value": value or ""
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
        "login.login(driver)\n"
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
        xpath = generate_xpath_from_control(ctype, name)

        if xpath:
            if ctype == "input":
                lines.append(f"# Inputting into: {name}")
                lines.append(f"Interactions.wait_and_send_keys(driver, By.XPATH, \"{xpath}\", \"{value}\")")
                lines.append(f"Interactions.wait_and_send_keys(driver, By.XPATH, \"{xpath}\", Keys.RETURN)")
            elif ctype == "commandbutton":
                lines.append(f"# Clicking button: {name}")
                lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
            else:
                lines.append(f"# Clicking (default) on: {name}")
                lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
        else:
            lines.append(f"# ❌ Locator not found for: {name} (Type: {ctype})")

    lines.append("time.sleep(5)")
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
