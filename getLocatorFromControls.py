def generate_xpath_from_control(control_type, control_name, control_label, description,value):
    control_type = control_type.lower()
#filter manager/quick filter
    if control_type in ["commandbutton", "menuitembutton","dropdialogbutton","button","togglebutton"]:
        return f"//button[@data-dyn-controlname='{control_name}']"
    elif control_type in ["menubutton", "menuitem"]:
        return f"//button[@name='{control_name}']"
    # elif control_type in ["combobox"]:
    #     return f"//div[@data-dyn-controlname='{control_name}']"
    elif control_type == "combobox":
        return [f"//input[@name='{control_name}']",
                f"//ul[contains(@aria-labelledby, '{control_name}')]//li[@data-dyn-index='{value}']"
            ]
    elif control_type == "sectionpage":
        return f"//button[contains(text(),'{control_label}')]"
    elif control_type == "checkbox":
        return [
            f"//label[contains(text(),'{control_label}')]/following-sibling::div/span[1]",
            f"//span[contains(@id, '{control_name}') and (@class='toggle-box' or @class='checkBox')]"
            ]
    elif control_type == "pivotitem":
        return f"//li[contains(@data-dyn-controlname,'{control_name}')]"
    elif control_type in ["input", "real", "referencegroup","date","radiobutton", "quickfilter","filtermanager", "segmentedentry"]:
        return [
            f"//input[contains(@name,'{control_name.strip()}')]",
            f"//input[contains(@aria-label,'{control_label.strip()}')]"
        ]
    elif control_type == "appbartab":
        return f"//button/parent::div[@data-dyn-controlname='{control_name}']"
    elif control_type == "multilineinput":
        return f"//textarea[@name='{control_name}']"
    elif control_type == "formrunpersonalizationtoolbarcontrol":
        if second_word:
            return f"(//span[contains(text(),'{second_word}')]/parent::div/parent::button)[2]"
        return f"(//span[contains(text(),'Personalize')]/parent::div/parent::button)[2]"
 
    # if control_type == "formrunpersonalizationtoolbarcontrol" and description and description.lower().startswith("click "):
    #     parts = description.split()
    #     if len(parts) > 1:
    #         second_word = parts[1]
    #         if second_word.lower() == "close":
    #             continue
 

    # elif control_type == "quickfilter":
