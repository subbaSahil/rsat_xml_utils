import xml.etree.ElementTree as ET
import re
import Interactions
from selenium.webdriver.common.by import By
from getLocatorFromControls import generate_xpath_from_control

import datetime
XML_PATH = "output.xml"
OUTPUT_SCRIPT = "rsat_script.py"

# global varaiables for managing the generation of script


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

def extract_controls_with_types(root):
    controls = []
    def extract_field_name_from_filtermanager(description_text):
        if description_text:
            match = re.search(r'Open (.*?) column filter\.', description_text.strip())
            if match:
                return match.group(1)
        return ""

    for elem in root.findall(".//UserAction"):
        label = None
        control_name = None
        control_type = None
        value = None
        filtervalue = None
        filterManagerLocator = None
        description = None
        annotation_present = False
        second_word = None
        command_name = None
        
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
                elif control_type == "quickfilter":
                    filtervalue = Interactions.extract_quickfilter_value(description)
            elif tag == "Value":
                value = child.text.strip() if child.text else None
            elif tag == "Description":
                description = child.text.strip() if child.text else None
            elif tag == "Annotations":
                # If Annotations has at least one child, it's present
                annotation_present = len(child.findall(".//*")) > 0
            elif tag == "CommandName":
                command_name = child.text.strip() if child.text else None
     
        if control_type == "formrunpersonalizationtoolbarcontrol" and description and description.lower().startswith("click "):
            parts = description.split()
            if len(parts) > 1:
                second_word = parts[1]
                if second_word.lower() == "close":
                    continue

        controls.append({
            "label": label or "",
            "name": control_name,
            "type": control_type or "",
            "value": value or "",
            "filtervalue": filtervalue or "",
            "filterManagerLocator": filterManagerLocator or "",
            "description": description or "", 
            "annotation_present": annotation_present,
            "second_word": second_word or "",
            "command_name": command_name or ""
        })

    return controls

def generate_selenium_script(controls):
    new_or_edit = ""
    input_label = ""
    input_name = ""
    grid_for_table_or_data_selection = ""
    lines = [
        "from selenium import webdriver",
        "from selenium.webdriver.common.by import By",
        "from selenium.webdriver.common.keys import Keys",
        "from selenium.webdriver.common.action_chains import ActionChains\n",
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
        # "Interactions.wait_and_click(driver, By.XPATH, \"//div[@aria-label='Modules']\")\n"
    ]

    # for key in nav_keys:
    #     xpath = f"//a[@data-dyn-title='{key}']"
    #     lines.append(f"# Clicking navigation: {key}")
    #     lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
    #     lines.append("time.sleep(1)\n")

    for control in controls:
        label = control["label"]
        name = control["name"]
        ctype = control["type"]
        value = control["value"]
        filtervalue = control["filtervalue"]
        filterManagerLocator = control["filterManagerLocator"]
        description = control["description"]
        second_word = control["second_word"]
        command_name = control["command_name"]
        
        if description and description.strip() == "Close the page." and not control["annotation_present"]:
            lines.append("# Closing the page")
            lines.append("Interactions.click_back_button(driver, By.XPATH, \"//button[@data-dyn-controlname='SystemDefinedCloseButton']\")")
            lines.append("time.sleep(1)")
            continue
        

        if description.startswith("Go to"):
            navgation_array = Interactions.extract_navigation_steps(description)
            lines.append("Interactions.wait_and_click(driver, By.XPATH, \"//div[@aria-label='Modules']\")")
            for key in navgation_array: 
                navigation_xpath = f"//a[@data-dyn-title='{key}']"
                lines.append(f"# Clicking navigation: {key}")
                lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{navigation_xpath}\")")
                lines.append("time.sleep(1)")
        elif description == "Click Edit.":
            new_or_edit = "Edit"

        if description.strip() == "In the list, find and select the desired record.":
            grid_for_table_or_data_selection= "table"
            print("grid_for_table_or_data_selection")
        elif description.startswith("In the list, select row"):
            grid_for_table_or_data_selection = "data_selection"
            print("grid_for_table_or_data_selection")

        xpath = generate_xpath_from_control(ctype, name,label, description, value,second_word)
        if xpath:
            if ctype in ["commandbutton", "menuitembutton","dropdialogbutton","button","togglebutton"]:
                lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                lines.append(f"     locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[0]}\")")
                lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, locator)")
                lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                lines.append(f"     locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[1]}\")")
                lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, locator)")
            if ctype in ["input" , "referencegroup","segmentedentry"] :
                if ctype == "input":
                    input_flag = True
                input_name = xpath[0]
                input_label= xpath[1]
                edited_value = value
                if new_or_edit == "Edit":
                    lines.append(f"# Clicking button: {name}")
                    
                else:
                    lines.append(f"# Inputting into: {name}")
                    lines.append(f"if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, \"{xpath[0]}\") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, \"{xpath[1]}\") ):")
                    lines.append(f"    #clicking inside grid: {name}")
                    lines.append(f"    if(Interactions.check_element_exist(driver, By.XPATH, \"{'('+xpath[0] +')[1]'}\")):")
                    lines.append(f"         locator=Interactions.get_locator(driver, By.XPATH, \"{'('+xpath[0] +')[1]'}\")")
                    lines.append(f"         Interactions.wait_and_send_keys(driver, By.XPATH, locator, \"{value}\")")
                    lines.append(f"    elif(Interactions.check_element_exist(driver, By.XPATH, \"{'('+xpath[1] +')[1]'}\")):")
                    lines.append(f"         locator=Interactions.get_locator(driver, By.XPATH, \"{'('+xpath[1] +')[1]'}\")")
                    lines.append(f"         Interactions.wait_and_send_keys(driver, By.XPATH, locator, \"{value}\")")
                    lines.append(f"else:")
                    lines.append(f"    if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                    lines.append(f"         locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[0]}\")")
                    lines.append(f"         Interactions.wait_and_send_keys(driver, By.XPATH, locator, \"{value}\")")
                    lines.append(f"    elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                    lines.append(f"         locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[1]}\")")
                    lines.append(f"         Interactions.wait_and_send_keys(driver, By.XPATH, locator, \"{value}\")")
                    # if command_name == "ExecuteHyperlink":
                    #     lines.append(f"# clicking inside grid: {name}")
                    #     lines.append(f"# TODO: Replace with appropriate XPath for the grid input")
                    #     lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"<your-xpath-here>\")")
                    # elif command_name == "RequestPopup":
                    #     lines.append(f"# clicking inside grid: {name}")
                    #     lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                    #     lines.append(f"    locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[0]}/following-sibling::div/div\")")
                    #     lines.append(f"    Interactions.wait_and_click(driver, By.XPATH, locator)")
                    #     lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                    #     lines.append(f"    locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[1]}/following-sibling::div/div\")")
                    #     lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, locator)")
                # else: 
                #         lines.append(f"# Inputting into: {name}")
                #         # xpath_controlname = xpath[0]+"/following-sibling::div"

                #         lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                #         lines.append(f"    locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[0]}\")")
                #         lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, locator, \"{value}\")")
                #         lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                #         lines.append(f"    locator=Interactions.get_locator(driver, By.XPATH, \"{xpath[1]}\")")
                #         lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, locator, \"{value}\")")
               
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
            elif ctype == "datetime":
                dt = datetime.datetime.fromisoformat(value)
                formatted_value = dt.strftime("%#m/%#d/%Y %#I:%M %p")
                # lines.append(f"Interactions.send_input_with_clear(driver, By.XPATH, \"{xpath}\", \"{formatted_value}\")")
                lines.append(f"if Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\"):")
                lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, \"{xpath[0]}\", \"{formatted_value}\",Keys.RETURN)")
                lines.append(f"elif Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\"):")
                lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, \"{xpath[1]}\", \"{formatted_value}\",Keys.RETURN)")
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
            # elif ctype == "commandbutton":
            #     lines.append(f"# Clicking button: {name}")
            #     lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
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
            elif ctype == "combobox":
                lines.append(f"# Clicking combobox: {name}")
                lines.append(f"if Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\"):")
                lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, \"{xpath[0]}\")")
                lines.append(f"elif Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\"):")
                lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, \"{xpath[1]}\")")
            elif ctype == "appbartab":
                lines.append(f"# Clicking (default) on: {name}")
                lines.append("time.sleep(3)")
                lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")") 
            elif ctype == "formrunpersonalizationtoolbarcontrol":
                if second_word:
                    return f"(//span[contains(text(),'{second_word}')]/parent::div/parent::button)[2]"
                return f"(//span[contains(text(),'Personalize')]/parent::div/parent::button)[2]"
            elif ctype == "formrunpersonalizationtoolbarcontrol":
                lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"(//div[@data-dyn-role='OverflowButton'])[2]\")")
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
                    # lines.append("        print(f\"filter_manager_cloumn_last_opened: {filter_manager_cloumn_last_opened}\")")
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
                    description = Interactions.normalize_description_quotes(description)
                    lines.append(f"filter_manager_data = Interactions.extract_value_and_operator_from_description(\"{description}\")")
                    lines.append("operator = filter_manager_data['operator']")
                    lines.append("new_val = filter_manager_data['value']")
                    lines.append("field_name = filter_manager_data['field_name']")
                    lines.append("drop_down_item = \"//input[contains(@aria-label,'Filter field: \"+field_name+\",')]/ancestor::div[@class='columnHeader-popup sysPopup']/ancestor::body/child::div[@class='sysPopup flyoutButton-flyOut layout-root-scope']//button//span[text()='\"+operator+\"']\"")
                    lines.append("input_field = \"//input[contains(@aria-label,'Filter field: \"+field_name+\",')]\"")
                    lines.append("apply_button = \"//input[contains(@aria-label,'Filter field: \"+field_name+\", operator: ')]//ancestor::div/child::div[@class='columnHeaderPopup-buttons']//span[text()='Apply']/ancestor::button\"")
                    lines.append("dropDown_button = \"//span[contains(@class,'button-label-dropDown')]/ancestor::button[contains(@class,'dynamicsButton')][ancestor::div[@class='filterFieldContainer']//input[contains(@aria-label,'Filter field: \"+field_name+\"')]]\"")
                    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, dropDown_button)")
                    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, drop_down_item)")
                    lines.append("if(Interactions.check_element_exist(driver, By.XPATH, \"//div[contains(@class,'popupShadow popupView preview')]\")):")
                    lines.append("    actions = ActionChains(driver)")
                    lines.append("    other_element = driver.find_element(By.XPATH, \"//div[text()='\" + field_name + \"']\")")
                    lines.append("    actions.move_to_element(other_element).perform()")
                    lines.append("if operator == 'is one of' or operator == 'matches':")
                    lines.append("    new_val = Interactions.extract_multiple_values(new_val)")
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
            elif ctype == "grid":   
                if new_or_edit == "Edit":
                    lines.append(f"# Clicking button: {name}")
                    locator_for_table_edit_aria_label = "//div[@aria-rowindex="+f"'{int(value)+1}']"+ input_label
                    locator_for_table_edit_name = "//div[@aria-rowindex="+f"'{int(value)+1}']"+ input_name
                    lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{locator_for_table_edit_aria_label}\")):")
                    lines.append(f"     locator=Interactions.get_locator(driver, By.XPATH, \"{locator_for_table_edit_aria_label}\")")
                    lines.append(f"     Interactions.wait_and_send_keys(driver, By.XPATH, locator, \"{edited_value}\")")
                    lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{locator_for_table_edit_name}\")):")
                    lines.append(f"     locator=Interactions.get_locator(driver, By.XPATH, \"{locator_for_table_edit_name}\")")
                    lines.append(f"     Interactions.wait_and_send_keys(driver, By.XPATH, locator, \"{edited_value}\")")
                elif grid_for_table_or_data_selection == "data_selection":
                    lines.append(f"# Clicking button: {name}")
                else:
                    lines.append(f"# Clicking button: {name}")
                    lines.append(f"# Clicking (default) on: {name}")
                    container = "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']"
                    lines.append(f"Interactions.scroll_and_click_row(driver, By.XPATH, \"{container}\", \"{xpath}\")")
                input_label = ""
                input_name = ""
                edited_value = ""
            # else:
            #     lines.append(f"# Clicking (default) on: {name}")
            #     lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
        else:
            lines.append(f"# ❌ Locator not found for: {name} (Type: {ctype})")
    lines.append("time.sleep(5)")
    lines.append("print(\"test case passed\")")
    lines.append("driver.quit()")
    return "\n".join(lines)
# Main logic
def getScript():
    tree = ET.parse(XML_PATH)
    root = tree.getroot()
# Combine and deduplicate navigation keys
# navigation_keys = list(dict.fromkeys(extract_navigation_from_description(root)))
# Get controls
# print(navigation_keys)
    controls = extract_controls_with_types(root)
# Generate and write script
    selenium_code = generate_selenium_script(controls)
    with open(OUTPUT_SCRIPT, "w", encoding="utf-8") as f:
        f.write(selenium_code)
    return selenium_code
print(f"✅ Selenium script generated in: {OUTPUT_SCRIPT}")

getScript()