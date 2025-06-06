import xml.etree.ElementTree as ET
import re
import Interactions
from selenium.webdriver.common.by import By
from getLocatorFromControls import generate_xpath_from_control

import datetime
XML_PATH = "output.xml"
OUTPUT_SCRIPT = "rsat_script.py"

# global varaiables for managing the generation of script
def input_for_filterpane(value):
    if value and ";" in value:
        return [part.strip() for part in value.split(";") if part.strip()]
    elif value:
        return [value.strip()]
    else:
        return []
def extracted_values_for_filterpane_control(parts):
    matches = re.findall(r'"(.*?)"', parts)
 
    if len(matches) >= 3:
        return {
            "value": matches[0],
            "field": matches[1],
            "operator": matches[2]
        }
    else:
        return {
            "value": None,
            "field": None,
            "operator": None
        }

def heirarchy_for_tree(value):
    if value and "\\" in value:
        return [part.strip() for part in value.split("\\") if part.strip()]
    elif value:
        return [value.strip()]
    else:
        return []

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
    new_or_edit_or_save = ""
    input_label = ""
    input_name = ""
    grid_for_table_or_data_selection = ""
    previous_control_type = None
    previous_control_name = ""
    previous_control_description = ""
    previous_user_action_value = None
    previous_control_label = None
    select_a_grid_or_click_a_input_anchor_flag = None
    ignore_grid = False
    filter_manager_value = None
    quickFilterValue = None
    input_flag_for_grid = False
    first_occurence_of_navigation = False
    add_line_flag = False
    dailog_box_line_items = False
    new_line_item_in_dailog_box_item = False
    new_line_in_dailog_already_exist = False
    multiple_select_button = False
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
        "user_input = None\n",
        "save_line_items_without_errors = False\n",
        # "Interactions.wait_and_click(driver, By.XPATH, \"//div[@aria-label='Modules']\")\n"
    ]

    # for key in nav_keys:
    #     xpath = f"//a[@data-dyn-title='{key}']"
    #     lines.append(f"# Clicking navigation: {key}")
    #     lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
    #     lines.append("time.sleep(1)\n")

    # for control in controls
    for i, control in enumerate(controls):
        label = control["label"]
        name = control["name"]
        ctype = control["type"]
        value = control["value"]
        filtervalue = control["filtervalue"]
        filterManagerLocator = control["filterManagerLocator"]
        description = control["description"]
        second_word = control["second_word"]
        command_name = control["command_name"]
        
        if description.startswith("Go to"):
            first_occurence_of_navigation = True
        
        if first_occurence_of_navigation == True:
            if description and description.strip() == "Close the page." and not control["annotation_present"]:
                lines.append("# Closing the page")
                lines.append("Interactions.click_back_button(driver, By.XPATH, \"//button[@data-dyn-controlname='SystemDefinedCloseButton']\")")
                lines.append("time.sleep(1)")
                continue
            elif description.startswith("Go to"):
                navgation_array = Interactions.extract_navigation_steps(description)
                lines.append("Interactions.wait_and_click(driver, By.XPATH, \"//div[@aria-label='Modules']\")")
                span_or_anchor = "None"
                for key in navgation_array:
                    navigation_xpath = None
                    if key == "Workspaces":
                        span_or_anchor = "span"
                        navigation_xpath = f"//a[@data-dyn-title='{key}']"
                        lines.append(f"# Clicking navigation: {key}")
                        lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{navigation_xpath}\")")
                        continue
                    if span_or_anchor == "span":
                        navigation_xpath = f"//div[@aria-label='{key}']"
                    else:
                        navigation_xpath = f"//a[@data-dyn-title='{key}']"
                    lines.append(f"# Clicking navigation: {key}")
                    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{navigation_xpath}\")")
                    lines.append("time.sleep(1)")
            elif description == "Click Edit.":
                new_or_edit_or_save = "Edit"
            elif description == "Click New.":
                if dailog_box_line_items:
                    new_line_item_in_dailog_box_item = True
            elif previous_control_description == "Click OK." and description == "Click Yes.":
                if dailog_box_line_items:
                    dailog_box_line_items = False

            elif description == "Click Save.":
                if add_line_flag == True:
                    add_line_flag = False   
            elif  description.strip() == "Click Select." and previous_control_type == "grid" and "In the list, select row" in previous_control_description:
                multiple_select_button = False
            elif description.strip() == "In the list, find and select the desired record." :
                grid_for_table_or_data_selection= "table"
                select_a_grid_or_click_a_input_anchor_flag = "select_row"
            elif description.strip() == "In the list, click the link in the selected row." or description.strip() == "In the list, mark the selected row.":
                select_a_grid_or_click_a_input_anchor_flag = "click_row"
            # elif description.startswith("In the list, select row"):
            #     grid_for_table_or_data_selection = "data_selection"
            elif description == "Click Add line.":
                add_line_flag = True

            elif description and description.strip() == "Use the shortcut for switching to View or Edit mode.":
                lines.append("# going to edit view mode")
                lines.append("Interactions.click_back_button(driver, By.XPATH, \"//button[@data-dyn-controlname='SystemDefinedViewEditButton']\")")
                lines.append("time.sleep(1)")
                continue  

            elif previous_control_description == "Click Purchase order line." and description.strip() == "Click Delivery schedule.":
                dailog_box_line_items = True
            
            elif description.strip() == "Refresh the page.":
                lines.append("# Refreshing the page")
                lines.append("Interactions.wait_and_click(driver, By.XPATH, \"//button[@data-dyn-controlname='SystemDefinedRefreshButton']\")")

            xpath = generate_xpath_from_control(ctype, name,label, description, value,second_word)

            multi_input_desc = [
                "In the Broker field, enter or select a value."]

            is_multiple_input = (
                ctype == "input"
                and description.strip() in multi_input_desc
                and command_name == "RequestPopup"  
            )

            # select_first_row = False
            # if (
            # ctype == "grid"
            # and description.strip() == "In the list, mark the selected row."
            # and command_name == "MarkActiveRow"
            # and (value is None or str(value).strip() == "")):
            # # Now check if there's a previous control
            #     if i > 0:
            #         prev_control = controls[i - 1]
            #         prev_description = prev_control.get("description", "").strip()
            #         prev_ctype = prev_control.get("type", "")
    
            #         # Add your condition
            #         if prev_description == "In the Broker field, enter or select a value." and prev_ctype == "input":
            #             select_first_row = True
    

            if ctype == "tree" or ctype == "Tree":
                    print("Entering tree block.")
                    hierarchy = heirarchy_for_tree(value)
                    if command_name == "ExpandingPath":
                        for part in hierarchy:
                            check_path=f"//li[@aria-label='{part}']"
                            xpath = f"//li[@aria-label='{part}']/div/button[@type='button']"

                            lines.append(f"#Expanding paths: {part}")
                            lines.append(f"if not (Interactions.checkInputExpanded(driver, By.XPATH, \"{check_path}\")):")
                            lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
                    elif command_name == "SelectionPathChanged":
                        if hierarchy:
                            last_node = hierarchy[-1]
                            xpath = f"//li[@aria-label='{last_node}']/div/button[@type='button']"
                            lines.append(f"# Clicking on last path: {last_node}")
                            lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
            if xpath:
                if ctype in ["commandbutton", "menuitembutton","dropdialogbutton","button","togglebutton"]:
                    lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                    lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, \"{xpath[0]}\")")
                    lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                    lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, \"{xpath[1]}\")")
                    if add_line_flag and ctype == "commandbutton" and description == "Click Add line.":
                        line_item_container = "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']"
                        line_item_xpath = "//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']//input[contains(@aria-label,'Line number')]"
                        lines.append(f"count = Interactions.check_for_line_item_count(driver, By.XPATH, \"{line_item_xpath}\")")
                        lines.append(f"row_number = Interactions.get_row_number_for_line_item(driver, By.XPATH, \"{line_item_container}\",count)")
                    # elif add_line_flag and ctype == "commandbutton" and description == "Click Save.":
                    #     lines.append("if Interactions.check_element_has_child_elements(driver, By.XPATH, \"//div[@class='messageBar-messageRegion']//ol\") <=0:")
                    #     lines.append("     print(\"There are no errors in the form, please check the messages.\")")
                         
                    #     lines.append("else:")
                    #     lines.append("     print(\"There are errors in the form, please check the messages.\")")
                elif ctype in ["menubutton", "menuitem"]:
                    lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                    lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, \"{xpath[0]}\")")
                    lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                    lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, \"{xpath[1]}\")")

                elif ctype == "segmentedentry":
                    if "SegmentedEntry" in name and label== "Main account":
                        expand_button = f"//div[@data-dyn-controlname='{name}']/ancestor::div[@role='group']/preceding-sibling::div[@role='heading']//button"
                        lines.append(f"if Interactions.check_aria_expanded(driver, By.XPATH, \"{expand_button}\") == True:")
                        lines.append(f"    Interactions.wait_and_click(driver, By.XPATH, \"{expand_button}\")")
                        if previous_control_type == "grid" and "LedgerDimension" in previous_control_name:
                             account_input = f"(//div[@data-dyn-controlname='{name}']//input)[{previous_user_action_value}]"
                             lines.append(f"ActionChains(driver).move_to_element(driver.find_element(By.XPATH,\"{account_input}\")).perform()")
                             lines.append(f"Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{account_input}\", \"{value}\")") 
                        else:
                            account_input = f"(//div[@data-dyn-controlname='{name}']//input)[1]"
                            lines.append(f"Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{account_input}\", \"{value}\")")
                    else:
                        lines.append(f"# Inputting into: {name}")
                        lines.append(f"if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, \"{xpath[0]}\") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, \"{xpath[1]}\") ):")
                        lines.append(f"    #clicking inside grid: {name}")
                        lines.append(f"     if(Interactions.check_element_exist(driver, By.XPATH, \"{'('+xpath[0] +')[1]'}\")):")
                        lines.append(f"          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,\"{xpath[0]}\")).perform()")
                        lines.append(f"          Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{'('+xpath[0] +')[1]'}\", \"{value}\")")
                        lines.append(f"     elif(Interactions.check_element_exist(driver, By.XPATH, \"{'('+xpath[1] +')[1]'}\")):")
                        lines.append(f"          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, \"{xpath[1]}\")).perform()")
                        lines.append(f"          Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{'('+xpath[1] +')[1]'}\", \"{value}\")")
                        lines.append(f"     else:")
                        lines.append(f"          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, \"{'('+xpath[2] +')[1]'}\")).perform()")
                        lines.append(f"          Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{'('+xpath[2] +')[1]'}\", \"{value}\")")
                        lines.append(f"else:")
                        lines.append(f"     if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                        lines.append(f"         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{xpath[0]}\", \"{value}\")")
                        lines.append(f"     elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                        lines.append(f"         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{xpath[1]}\", \"{value}\")")
                        lines.append(f"     else:")
                        lines.append(f"          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, \"{xpath[2]}\")).perform()")
                        lines.append(f"          Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{xpath[2]}\", \"{value}\")")
                elif     ctype in ["input" , "referencegroup"] :
                    dailog_box_container = "//div[@class='DialogContent group editMode no-caption-group col1 fill-width layout-container layout-vertical']"
                    edited_value = value
                    # if ctype == "input":
                    #     input_name = xpath[0]
                    #     input_label= xpath[1]
                    if is_multiple_input:
                            dropdown_xpath = f"//input[@name='{name}']/following-sibling::div//*[contains(@class, 'lookupButton')]"
                            lines.append(f"# Open dropdown for {label}")
                            lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{dropdown_xpath}\")")
                            lines.append("time.sleep(1)")
                    elif ctype == "referencegroup" and command_name == "ResolveChanges":
                        lines.append(f"# clicking dropdown for Tree")
                        # lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"//input[@role='combobox']/parent::div/parent::div/following-sibling::div\")")
                        lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"//input[contains(@name,'{name}')]/parent::div/parent::div/following-sibling::div/div\")")
                    elif command_name == "ExecuteHyperlink" and ctype == "input" and description.startswith("Click to follow the link in the "):
                        if name == "EcoResProduct_DisplayProductNumber":
                            lines.append("user_input = input('Enter the value for the hyperlink: ')")
                            lines.append("Interactions.wait_and_click(driver, By.XPATH, \"//div[@name='EcoResProduct_DisplayProductNumber' and text()='\"+user_input+\"']\")")
                        else:
                            lines.append("user_input = input('Enter the value for the hyperlink: ')")
                            lines.append(f"if Interactions.check_element_exist(driver, By.XPATH, \"//div[contains(@data-dyn-savedtooltip,'\"+user_input+\"')]/preceding-sibling::label[text()='{label}']\"):")
                            lines.append(f"     Interactions.wait_and_click(driver, By.XPATH,  \"//div[contains(@data-dyn-savedtooltip,'\"+user_input+\"')]/preceding-sibling::label[text()='{label}']\")")
                            lines.append(f"     Interactions.press_enter(driver, By.XPATH, \"//div[contains(@data-dyn-savedtooltip,'\"+user_input+\"')]/preceding-sibling::label[text()='{label}']\")")
                            lines.append(f"elif Interactions.check_element_exist(driver, By.XPATH, \"//input[contains(@title,'\"+user_input+\"')]/preceding-sibling::label[text()='{label}']\"):")
                            lines.append(f"     Interactions.wait_and_click(driver, By.XPATH,  \"//input[contains(@title,'\"+user_input+\"')]/preceding-sibling::label[text()='{label}']\")")
                            lines.append(f"     Interactions.press_enter(driver, By.XPATH, \"//input[contains(@title,'\"+user_input+\"')]/preceding-sibling::label[text()='{label}']\")")
                    elif add_line_flag and not dailog_box_line_items:
                        lines.append(f"if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, \"{xpath[0]}\") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, \"{xpath[1]}\") ):")
                        lines.append(f"    #clicking inside grid: {name}")
                        lines.append("    if(Interactions.check_element_exist(driver, By.XPATH, \"(" + xpath[0] + ")[\" + row_number + \"]\")):")
                        lines.append("          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,\"(" + xpath[0] + ")[\" + row_number + \"]\")).perform()")
                        lines.append("          Interactions.wait_and_send_keys(driver, By.XPATH, \"(" + xpath[0] + ")[\" + row_number + \"]\", \"" + value + "\")")
                        lines.append("    elif(Interactions.check_element_exist(driver, By.XPATH, \"(" + xpath[1] + ")[\" + row_number + \"]\")):")
                        lines.append("          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, \"(" + xpath[1] + ")[\" + row_number + \"]\")).perform()")
                        lines.append("          Interactions.wait_and_send_keys(driver, By.XPATH, \"(" + xpath[1] + ")[\" + row_number + \"]\", \"" + value + "\")")
                    elif dailog_box_line_items:
                        if new_line_item_in_dailog_box_item:
                            if new_line_in_dailog_already_exist == False:
                                new_line_in_dailog_already_exist = True
                                lines.append(f"dailog_box_line_count = Interactions.check_for_line_item_count(driver, By.XPATH, \"{dailog_box_container}//input[contains(@aria-label,'Line number')]\")")
                                lines.append(f"line_number = Interactions.get_max_value_from_elements(driver, By.XPATH, \"{dailog_box_container}//input[contains(@aria-label,'Line number')]\", dailog_box_line_count)")
                        else:
                            lines.append("line_number = input('Enter the line number: ')")
                        lines.append(f"if Interactions.check_element_exist(driver, By.XPATH, \"{dailog_box_container}\"):")

                        # Generate dynamic XPath using value match
                        lines.append(f"    target_xpath_1 = f\"{dailog_box_container}//input[contains(@aria-label, 'Line number') and @value='{{line_number}}']/ancestor::div[@role='gridcell']/following-sibling::div{xpath[0]}\"")
                        lines.append(f"    target_xpath_2 = f\"{dailog_box_container}//input[contains(@aria-label, 'Line number') and @value='{{line_number}}']/ancestor::div[@role='gridcell']/following-sibling::div{xpath[1]}\"")
                        lines.append(f"    if Interactions.check_element_exist(driver, By.XPATH, target_xpath_1):")
                        lines.append(f"        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_1, \"{value}\")")

                        lines.append(f"    elif Interactions.check_element_exist(driver, By.XPATH, target_xpath_2):")
                        lines.append(f"        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_2, \"{value}\")")

                        lines.append("    else:")
                        lines.append(f"        print(\"Element not found in either dynamic or fallback XPath for: {name}\")")
                        
                    else:
                        lines.append(f"# Inputting into: {name}")
                        lines.append(f"if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, \"{xpath[0]}\") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, \"{xpath[1]}\") ):")
                        lines.append(f"    #clicking inside grid: {name}")
                        lines.append(f"    if(Interactions.check_element_exist(driver, By.XPATH, \"{'('+xpath[0] +')[1]'}\")):")
                        lines.append(f"          ActionChains(driver).move_to_element(driver.find_element(By.XPATH,\"{xpath[0]}\")).perform()")
                        lines.append(f"          Interactions.wait_and_send_keys(driver, By.XPATH, \"{'('+xpath[0] +')[1]'}\", \"{value}\")")
                        lines.append(f"    elif(Interactions.check_element_exist(driver, By.XPATH, \"{'('+xpath[1] +')[1]'}\")):")
                        lines.append(f"          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, \"{xpath[1]}\")).perform()")
                        lines.append(f"          Interactions.wait_and_send_keys(driver, By.XPATH, \"{'('+xpath[1] +')[1]'}\", \"{value}\")")
                        lines.append(f"else:")
                        lines.append(f"    if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                        lines.append(f"         Interactions.wait_and_send_keys(driver, By.XPATH, \"{xpath[0]}\", \"{value}\")")
                        lines.append(f"    elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                        lines.append(f"         Interactions.wait_and_send_keys(driver, By.XPATH, \"{xpath[1]}\", \"{value}\")")
                        lines.append(f"    Interactions.press_enter(driver, By.XPATH, \"//body\")")
                elif ctype == "listbox":
                    lines.append(f"# Clicking listbox: {name}")
                    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")

                elif ctype in["quickfilter"]:
                    quickFilterValue = filtervalue
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
                    lines.append(f"if Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\"):")
                    lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, \"{xpath[0]}\", \"{formatted_value}\",Keys.RETURN)")
                    lines.append(f"elif Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\"):")
                    lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, \"{xpath[1]}\", \"{formatted_value}\",Keys.RETURN)")
                elif ctype == "date":
                    date = convert_date_format(value)
                    if dailog_box_line_items:
                        if new_line_item_in_dailog_box_item:
                            if new_line_in_dailog_already_exist == False:
                                new_line_in_dailog_already_exist = True
                                lines.append(f"dailog_box_line_count = Interactions.check_for_line_item_count(driver, By.XPATH, \"{dailog_box_container}//input[contains(@aria-label,'Line number')]\")")
                                lines.append(f"line_number = Interactions.get_max_value_from_elements(driver, By.XPATH, \"{dailog_box_container}//input[contains(@aria-label,'Line number')]\", dailog_box_line_count)")
                        else:
                            lines.append("line_number = input('Enter the line number: ')")
                        lines.append(f"if Interactions.check_element_exist(driver, By.XPATH, \"{dailog_box_container}\"):")
                        lines.append(f"    target_xpath_1 = f\"{dailog_box_container}//input[contains(@aria-label, 'Line number') and @value='{{line_number}}']/ancestor::div[@role='gridcell']/following-sibling::div{xpath[0]}\"")
                        lines.append(f"    target_xpath_2 = f\"{dailog_box_container}//input[contains(@aria-label, 'Line number') and @value='{{line_number}}']/ancestor::div[@role='gridcell']/following-sibling::div{xpath[1]}\"")
                        lines.append(f"    if Interactions.check_element_exist(driver, By.XPATH, target_xpath_1):")
                        lines.append(f"        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_1, \"{date}\")")

                        lines.append(f"    elif Interactions.check_element_exist(driver, By.XPATH, target_xpath_2):")
                        lines.append(f"        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_2, \"{date}\")")

                        lines.append("    else:")
                        lines.append(f"        print(\"Element not found in either dynamic or fallback XPath for: {name}\")")
                    else:
                        lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                        lines.append(f"    Interactions.get_locator(driver, By.XPATH, \"{xpath[1]}\")")
                        lines.append(f"    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{xpath[0]}\", \"{date}\")")
                        lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                        lines.append(f"    Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{xpath[1]}\", \"{date}\")")
                elif ctype == "real":
                    dailog_box_container = "//div[@class='dialog-popup-content editMode Dialog fill-width fill-height layout-container layout-vertical']"
                    if add_line_flag and not dailog_box_line_items:
                        # lines.append("line_number_input = \"//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']//input[contains(@aria-label,'Line number')]\"")
                        # lines.append("count = Interactions.check_for_line_item_count(driver, By.XPATH, line_number_input)")
                        # lines.append("row_number = Interactions.get_row_number_for_line_item(driver, By.XPATH, \"//div[text()='Item number'  or text()='Line number' ]/ancestor::div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']\",count)")
                        lines.append(f"if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, \"{xpath[0]}\") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, \"{xpath[1]}\") ):")
                        lines.append(f"    #clicking inside grid: {name}")
                        # lines.append(f"    if(Interactions.check_element_exist(driver, By.XPATH, \"({xpath[0]})[\" + str(row_number) + \"]\")):")
                        lines.append("    if(Interactions.check_element_exist(driver, By.XPATH, \"(" + xpath[0] + ")[\" + row_number + \"]\")):")
                        # lines.append(f"    if(Interactions.check_element_exist(driver, By.XPATH, \"({xpath[0]})[\" + str(row_number) + \"]\")):")
                        lines.append("          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, \"("+xpath[0]+")[\" + row_number + \"]\")).perform()")
                        lines.append("          Interactions.wait_and_send_keys(driver, By.XPATH, \"("+xpath[0]+")[\" + row_number + \"]\", \""+ value + "\")")
                        lines.append("    elif(Interactions.check_element_exist(driver, By.XPATH, \"("+xpath[1]+")[\" + row_number + \"]\")):")
                        lines.append("          ActionChains(driver).move_to_element(driver.find_element(By.XPATH, \"("+xpath[1]+")[\" + row_number + \"]\")).perform()")
                        lines.append("          Interactions.wait_and_send_keys(driver, By.XPATH, \"("+xpath[1]+")[\" + row_number + \"]\", \""+ value + "\")")
                        # lines.append("          Interactions.wait_and_send_keys(driver, By.XPATH, \"(" + xpath[1] + ")[\" + row_number + \"]\", \"" + value + "\")")
 
                    elif dailog_box_line_items:
                        if new_line_item_in_dailog_box_item:
                            if new_line_in_dailog_already_exist == False:
                                new_line_in_dailog_already_exist = True
                                lines.append(f"dailog_box_line_count = Interactions.check_for_line_item_count(driver, By.XPATH, \"{dailog_box_container}//input[contains(@aria-label,'Line number')]\")")
                                lines.append(f"line_number = Interactions.get_max_value_from_elements(driver, By.XPATH, \"{dailog_box_container}//input[contains(@aria-label,'Line number')]\", dailog_box_line_count)")
                        else:
                            lines.append("line_number = input('Enter the line number: ')")
                        lines.append(f"if Interactions.check_element_exist(driver, By.XPATH, \"{dailog_box_container}\"):")

                        # Generate dynamic XPath using value match
                        lines.append(f"    target_xpath_1 = f\"{dailog_box_container}//input[contains(@aria-label, 'Line number') and @value='{{line_number}}']/ancestor::div[@role='gridcell']/following-sibling::div{xpath[0]}\"")
                        lines.append(f"    target_xpath_2 = f\"{dailog_box_container}//input[contains(@aria-label, 'Line number') and @value='{{line_number}}']/ancestor::div[@role='gridcell']/following-sibling::div{xpath[1]}\"")
                        lines.append(f"    if Interactions.check_element_exist(driver, By.XPATH, target_xpath_1):")
                        lines.append(f"        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_1, \"{value}\")")

                        lines.append(f"    elif Interactions.check_element_exist(driver, By.XPATH, target_xpath_2):")
                        lines.append(f"        Interactions.clear_input_field_and_send_keys(driver, By.XPATH, target_xpath_2, \"{value}\")")

                        lines.append("    else:")
                        lines.append(f"        print(\"Element not found in either dynamic or fallback XPath for: {name}\")")

                    else:
                        lines.append(f"if(Interactions.check_input_ancestor_is_table(driver, By.XPATH, \"{xpath[0]}\") or Interactions.check_input_ancestor_is_table(driver, By.XPATH, \"{xpath[1]}\") ):")
                        lines.append(f"    #clicking inside grid: {name}")
                        lines.append(f"    if(Interactions.check_element_exist(driver, By.XPATH, \"{'('+xpath[0] +')[1]'}\")):")
                        lines.append(f"         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,\"{'('+xpath[0] +')[1]'}\")).perform()")
                        lines.append(f"         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{'('+xpath[0] +')[1]'}\", \"{value}\")")
                        lines.append(f"    elif(Interactions.check_element_exist(driver, By.XPATH, \"{'('+xpath[1] +')[1]'}\")):")
                        lines.append(f"         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,\"{'('+xpath[1] +')[1]'}\")).perform()")
                        lines.append(f"         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{'('+xpath[1] +')[1]'}\", \"{value}\")")
                        lines.append(f"else:")
                        lines.append(f"    if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                        lines.append(f"         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,\"{xpath[0]}\")).perform()")
                        lines.append(f"         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{xpath[0]}\", \"{value}\")")
                        lines.append(f"    elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                        lines.append(f"         ActionChains(driver).move_to_element(driver.find_element(By.XPATH,\"{xpath[1]}\")).perform()")
                        lines.append(f"         Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{xpath[1]}\", \"{value}\")")
                        lines.append(f"    Interactions.press_enter(driver, By.XPATH, \"//body\")")

                elif ctype == "multilineinput":
                    lines.append(f"# Inputting into: {name}")
                    lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath}\")):")
                    lines.append(f"    Interactions.wait_and_send_keys(driver, By.XPATH, \"{xpath}\", \"{value}\")")
                elif ctype == "checkbox":
                    if description == "Select the Enable check box." and label == "Enable":
                        if previous_control_type == "grid" and previous_user_action_value == "":
                            first_checkbox_xpath = f"(//div[contains(@id,'{name}')]//span)[1]"
                            lines.append(f"if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, \"{first_checkbox_xpath}\", {value}) == False:")
                            lines.append(f"    Interactions.wait_and_click(driver, By.XPATH, \"{first_checkbox_xpath}\")")
                        elif previous_control_type == "grid" and previous_user_action_value != "":
                            check_box_xpath = f"(//div[contains(@id,'{name}')]//span)[{previous_user_action_value}]"
                            lines.append(f"if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, \"{check_box_xpath}\", {value}) == False:")
                            lines.append(f"    Interactions.wait_and_click(driver, By.XPATH, \"{check_box_xpath}\")")
                    else:
                        lines.append(f"# Clicking checkbox: {name}")
                        lines.append(f"if(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\")):")
                        lines.append(f"    if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, \"{xpath[0]}\", {value}) == False:")
                        lines.append(f"         Interactions.wait_and_click(driver, By.XPATH, \"{xpath[0]}\")")
                        lines.append(f"elif(Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\")):")
                        lines.append(f"    if Interactions.check_if_checkbox_is_checked(driver, By.XPATH, \"{xpath[1]}\", {value}) == False:")
                        lines.append(f"         Interactions.wait_and_click(driver, By.XPATH, \"{xpath[1]}\")")
                        # lines.append(f"    Interactions.wait_and_click(driver, By.XPATH, \"//div[text()='{xpath[1]}']\")")
                elif ctype == "combobox":
                    lines.append(f"# Clicking combobox: {name}")
                    lines.append("combox_box_to_click = None")
                    lines.append(f"if Interactions.check_element_exist(driver, By.XPATH, \"{xpath[0]}\"):")
                    lines.append(f"     combox_box_to_click = \"{xpath[0]}\"")
                    lines.append(f"elif Interactions.check_element_exist(driver, By.XPATH, \"{xpath[3]}\"):")
                    lines.append(f"     combox_box_to_click = \"{xpath[3]}\"")
                    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, combox_box_to_click)")
                    lines.append(f"if Interactions.check_element_exist(driver, By.XPATH, \"{xpath[1]}\"):")
                    lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, \"{xpath[1]}\")")
                    lines.append(f"elif Interactions.check_element_exist(driver, By.XPATH, \"{xpath[4]}\"):")
                    lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, \"{xpath[4]}\")")
                    lines.append(f"else:")
                    lines.append(f"     if Interactions.check_element_exist(driver, By.XPATH, \"{xpath[2]}\"):")
                    lines.append(f"            cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, \"{xpath[2]}\",By.XPATH, \"{xpath[1]}\")")
                    lines.append(f"            if cliked_or_not == False:")
                    lines.append(f"                Interactions.scroll_and_click_dropdown_item(driver, \"{xpath[2]}\",By.XPATH, \"{xpath[4]}\")")
                    lines.append(f"     elif Interactions.check_element_exist(driver, By.XPATH, \"{xpath[5]}\"):")
                    lines.append(f"            cliked_or_not = Interactions.scroll_and_click_dropdown_item(driver, \"{xpath[5]}\",By.XPATH, \"{xpath[1]}\")")
                    lines.append(f"            if cliked_or_not == False:")
                    lines.append(f"                Interactions.scroll_and_click_dropdown_item(driver, \"{xpath[5]}\",By.XPATH, \"{xpath[4]}\")")


                elif ctype == "appbartab":
                    lines.append(f"# Clicking (default) on: {name}")
                    lines.append("time.sleep(3)")
                    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
                elif ctype == "integer":
                    lines.append(f"# Inputting into: {name}")
                    lines.append(f"Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"{xpath}\", \"{value}\")")
               
                elif ctype == "pivotitem":
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
                        filtered_description = Interactions.normalize_description_quotes(description)
                        # filter_manager_data = Interactions.extract_value_and_operator_from_description(description)
                        lines.append(f"filter_manager_data = Interactions.extract_value_and_operator_from_description(\"{filtered_description}\")")
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
                    container = "//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']"
                    previous_desc = f"In the {previous_control_label} field, enter or select a value."
                    if previous_control_type == "input" and previous_control_description == previous_desc and previous_control_label != "Broker":
                        lines.append("\"Skipping grid since previous was control was input\"")
                        input_flag_for_grid = True
                        # ignore_grid = True
                    # the broker multple input
                    elif ctype =="grid" and previous_control_type == "input" and previous_control_description == "In the Broker field, enter or select a value." and previous_control_label == "Broker":
                        lines.append("user_input = input(\"Press data to select: \")")
                        lines.append(f"Interactions.scroll_and_click(driver, By.XPATH, \"{container}\", f\"//input[@value='{{user_input}}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']\")")
                        multiple_select_button = True
                    elif previous_control_type == "grid" and "In the list, select row" in previous_control_description:
                        if multiple_select_button == True:
                            lines.append("user_input = input(\"Press data to select: \")")
                            lines.append(f"Interactions.scroll_and_click(driver, By.XPATH, \"{container}\", f\"//input[@value='{{user_input}}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']\")")
                        else:
                            lines.append("\"Skipping grid selection due input in the ancestor\"")
                    elif description.strip() == "In the list, mark the selected row." and command_name == "MarkActiveRow":
                        lines.append("\"Skipping grid since it is deafault behavior of d365\"")
                    elif previous_control_type == "input" and previous_control_description == previous_desc and description.strip() == "In the list, find and select the desired record.":
                        lines.append("\"Skipping grid\"")
                        print("asdasda")
                    elif previous_control_type == "grid" and previous_control_description == "In the list, find and select the desired record." and description.strip() == "In the list, click the link in the selected row.":
                        if input_flag_for_grid == False:
                            lines.append(f"Interactions.press_enter(driver, By.XPATH, \"//input[@value='\"+user_input+\"']\")")
                            input_flag_for_grid = True
                        else:
                            lines.append("\"Skipping grid since previous was input\"")
                    elif description.strip() == "In the list, find and select the desired record." and name == "ChangeProposalGrid":
                        pass
                    elif ctype == "grid" and description.strip() == "In the list, find and select the desired record." and "LedgerDimensionGrid" in name:
                        pass
                    elif select_a_grid_or_click_a_input_anchor_flag == "select_row":
                        
                        if command_name == "ChangeSelectedIndex":
                            container2 = f"//div[@data-dyn-controlname='{name}//div[contains(@class,'fixedDataTableRowLayout_')]/ancestor::div[@role='grid']"
                            lines.append(f"# Clicking button: {name}")
                            lines.append(f"user_input = input(\"Press data to select: \")")
                            lines.append(f"Interactions.scroll_and_click(driver, By.XPATH, \"{container2}\", f\"//input[@value='{{user_input}}']\")")
                        else:
                             lines.append(f"Interactions.scroll_and_click_row(driver, By.XPATH, \"{container}\", f\"//input[@value='{{user_input}}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']\")")
                    elif select_a_grid_or_click_a_input_anchor_flag == "click_row":
                        if previous_control_type == "grid" and previous_control_description == "In the list, find and select the desired record.":
                                lines.append(f"Interactions.press_enter(driver, By.XPATH, \"//input[@value='\"+user_input+\"']\")")
                        elif  previous_control_type == "quickfilter":
                                lines.append(f"# Clicking button: {name}")
                                lines.append(f"if Interactions.check_element_exist(driver, By.XPATH, f\"//input[@value='{quickFilterValue}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']\"):")
                                lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, f\"//input[@value='{quickFilterValue}']/ancestor::div[@class='fixedDataTableRowLayout_body']/div[1]//div[@role='checkbox']\")")
                                lines.append("else:")
                                lines.append(f"     Interactions.wait_and_click(driver, By.XPATH, f\"//input[@value='{quickFilterValue}']\")")
                                lines.append(f"Interactions.press_enter(driver, By.XPATH, \"//input[@value='{quickFilterValue}']\")")
                        elif previous_control_type == "referencegroup":
                            lines.append(f"# Clicking button: {name}")
                            lines.append(f"user_input = input(\"Press data to select: \")")
                            lines.append(f"Interactions.scroll_and_click_row(driver, By.XPATH, \"{container}\", f\"//input[@value='{{user_input}}']/ancestor::div[@class='fixedDataTableRowLayout_body']\")")
                            lines.append(f"Interactions.press_enter(driver, By.XPATH, \"//input[@value='\"+user_input+\"']\")")
                        else:
                            lines.append(f"# Clicking button: {name}")
                            lines.append(f"user_input = input(\"Press data to select: \")")
                            lines.append(f"Interactions.scroll_and_click_row(driver, By.XPATH, \"{container}\", f\"//input[@value='{{user_input}}']\")")
                            # lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"//input[@value='\"+user_input+\"']\")")
                            lines.append(f"Interactions.press_enter(driver, By.XPATH, \"//input[@value='\"+user_input+\"']\")")
                    

                elif ctype in ["filterpane"]:
                    if command_name == "ApplyFilters":
                        extracted_parts =input_for_filterpane(value)
                        for part in extracted_parts:
                            key_values = extracted_values_for_filterpane_control(part)
                            print(key_values)
                            field = key_values.get("field")
                            operator = key_values.get("operator")
                            val = key_values.get("value")

                            if val is not None and val != "":
                                lines.append(f"#Applying filter:")  
                                #sending filter operator
                                if operator != "begins with":
                                    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"//div[@title='{field}']/following-sibling::div/button\")")
                                    lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"//div[@data-dyn-role='FilterPane']/ancestor::div[@id='mainContainer']/following-sibling::div/div/button/div/span[text()='{operator}']\")")                            #sending inputs
                                lines.append(f"Interactions.clear_input_field_and_send_keys(driver, By.XPATH, \"//div[@title='{field}']/parent::div/parent::div/following-sibling::div//input\",\"{val}\")")      
                                lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath[0]}\")")

                    if command_name=="ResetFilters":
                        lines.append(f"#Resetting filter")
                        lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath[1]}\")")
                    if command_name=="AddAFilterField":
                        lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath[2]}\")")

    

                # else:
                #     lines.append(f"# Clicking (default) on: {name}")
                #     lines.append(f"Interactions.wait_and_click(driver, By.XPATH, \"{xpath}\")")
            # else:
            #     lines.append(f"# ❌ Locator not found for: {name} (Type: {ctype})")
            previous_control_type = ctype
            previous_control_name = name
            previous_control_description = description
            previous_user_action_value = value
            previous_control_label = label
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