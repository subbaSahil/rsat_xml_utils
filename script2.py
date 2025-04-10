import xml.etree.ElementTree as ET
from selenium.webdriver.common.by import By
 
# File paths
XML_PATH = "output.xml"
OUTPUT_SCRIPT = "rsat_script.py"
 
def generate_xpath_from_navigation(description):
    segments = description.replace("Go to", "").strip().rstrip('.').split('>')
    segments = [seg.strip() for seg in segments]
 
    if len(segments) < 2:
        return []
 
    first = segments[0]
    last = segments[-1]
    middle = segments[1:-1]
 
    lines = []
    lines.append(f"# Navigate to: {description}")
    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"//div[@aria-label='Modules']\")")
    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"//a[text()='{first}']\")\n")
 
    for mid in middle:
        safe_var = mid.lower().replace(' ', '_')
        expanded_xpath = f"//a[text()='{mid}' and @data-dyn-expanded='true']"
        collapsed_xpath = f"//a[text()='{mid}' and @data-dyn-expanded='false']"
 
        lines.append(f"# Expand if collapsed: {mid}")
        lines.append(f"{safe_var}_expanded_xpath = \"{expanded_xpath}\"")
        lines.append(f"{safe_var}_collapsed_xpath = \"{collapsed_xpath}\"\n")
        lines.append("try:")
        lines.append(f"    driver.find_element(By.XPATH, {safe_var}_expanded_xpath)")
        lines.append(f"    print(\"{mid} is already expanded.\")")
        lines.append("except Exception:")
        lines.append(f"    print(\"Expanding {mid}...\")")
        lines.append(f"    Interactions.wait_and_click(driver, By.XPATH, {safe_var}_collapsed_xpath)\n")
 
    lines.append(f"# Final click on: {last}")
    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"//a[text()='{last}']\")\n")
    return lines
 
def extract_controls(root):
    controls = []
    for user_action in root.findall(".//UserAction"):
        description = user_action.findtext("Description", default="").strip()
        control_name = user_action.findtext("ControlName", default="").strip()
        control_label = user_action.findtext("ControlLabel", default="").strip()
        control_type = user_action.findtext("ControlType", default="").strip()
        value = user_action.findtext("Value", default="").strip()
 
        controls.append({
            "description": description,
            "control_name": control_name,
            "label": control_label,
            "type": control_type,
            "value": value,
        })
 
    return controls
 
def generate_selenium_script(controls):
    lines = [
        "from selenium import webdriver",
        "from selenium.webdriver.common.by import By",
        "import time",
        "import login",
        "import Interactions",
        "from selenium.common.exceptions import NoSuchElementException\n",
        "driver = webdriver.Chrome()",
        "driver.maximize_window()",
        "time.sleep(3)",
        "login.login(driver)\n"
    ]
 
    for control in controls:
        description = control["description"]
        control_name = control["control_name"]
        control_label = control["label"]
        control_type = control["type"]
        value = control["value"]
 
        # Handle navigation
        if description.startswith("Go to"):
            lines += generate_xpath_from_navigation(description)
 
        # Handle other UI control actions
        if control_name and control_name != "No Control Name":
            lines.append(f"# Clicking control: {control_name} (Type: {control_type})")
            lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"//button[@name='{control_name}']\")")
            lines.append("time.sleep(1)\n")
 
    lines.append("driver.quit()")
    return "\n".join(lines)
 
def main():
    tree = ET.parse(XML_PATH)
    root = tree.getroot()
    controls = extract_controls(root)
    script = generate_selenium_script(controls)
 
    with open(OUTPUT_SCRIPT, "w") as f:
        f.write(script)
 
    print(f"Selenium script has been written to {OUTPUT_SCRIPT}")
 
if __name__ == "__main__":
    main()
 
 