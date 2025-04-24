import xml.etree.ElementTree as ET
 
def extract_user_actions(input_xml):
    tree = ET.parse(input_xml)
    root = tree.getroot()
 
    namespaces = {
        '': 'http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.Client.ServerForm.TaskRecording',
        'd2p1': 'http://schemas.microsoft.com/2003/10/Serialization/Arrays',
        'd7p1': 'http://schemas.microsoft.com/2003/10/Serialization/Arrays',
        'i': 'http://www.w3.org/2001/XMLSchema-instance',
        'z': 'http://schemas.microsoft.com/2003/10/Serialization/'
    }
 
    user_actions_with_details = ET.Element("UserActionsWithDetails")
    user_actions = root.findall(".//UserActions//d2p1:anyType", namespaces=namespaces)
 
    actions_dict = {}  # To store actions grouped by Ref
 
    for index, action in enumerate(user_actions):
        ref = action.attrib.get("{http://schemas.microsoft.com/2003/10/Serialization/}Ref")
        node = root.find(f".//Node[@z:Id='{ref}']", namespaces=namespaces)
 
        description = ''
        control_label = ''
        control_type = ''
        control_names = []
        value = ''
        value_label = ''
        navigation_path = []
 
        if node is not None:
            desc_elem = node.find(".//Description", namespaces=namespaces)
            if desc_elem is not None and desc_elem.text:
                description = desc_elem.text
 
            control_label_elem = node.find(".//ControlLabel", namespaces=namespaces)
            if control_label_elem is not None and control_label_elem.text:
                control_label = control_label_elem.text
 
            control_type_elem = node.find(".//ControlType", namespaces=namespaces)
            if control_type_elem is not None and control_type_elem.text:
                control_type = control_type_elem.text
 
            control_name_elem = node.find(".//ControlName", namespaces=namespaces)
            if control_name_elem is not None and control_name_elem.text:
                control_name_text = control_name_elem.text
                if control_name_text.strip() == "Grid" and control_type.strip() == "Grid":
                    continue
                control_names.append(control_name_text)
            else:
                nav_path = node.find(".//NavigationPath", namespaces=namespaces)
                if nav_path is not None:
                    path_parts = nav_path.findall(".//d7p1:string", namespaces=namespaces)
                    for part in path_parts:
                        if part.text:
                            navigation_path.append(part.text)
 
            # Get value
            annotation_value = node.find(".//Annotations//Annotation//CanonicalUserAction//Value", namespaces=namespaces)
            if annotation_value is not None and annotation_value.text:
                value = annotation_value.text.strip()
            else:
                direct_value = node.find(".//Value", namespaces=namespaces)
                if direct_value is not None and direct_value.text:
                    value = direct_value.text.strip()
 
            # Get value label if it exists
            value_label_elem = node.find(".//ValueLabel", namespaces=namespaces)
            if value_label_elem is not None and value_label_elem.text:
                value_label = value_label_elem.text.strip()
 
        if ref not in actions_dict:
            actions_dict[ref] = {
                "Description": description,
                "ControlNames": set(),
                "ControlLabel": control_label,
                "ControlType": control_type,
                "Value": value,
                "ValueLabel": value_label,
                "NavigationPath": navigation_path
            }
 
        for control_name in control_names:
            actions_dict[ref]["ControlNames"].add(control_name)
 
    # Generate output XML
    for ref, action_data in actions_dict.items():
        user_action = ET.SubElement(user_actions_with_details, "UserAction")
        user_action.set("Ref", ref)
        ET.SubElement(user_action, "Description").text = action_data["Description"]
        ET.SubElement(user_action, "NodeId").text = ref
        ET.SubElement(user_action, "Sequence").text = str(index + 1)
 
        for nav_item in action_data["NavigationPath"]:
            ET.SubElement(user_action, "Navigation").text = nav_item
 
        if action_data["ControlNames"]:
            for control_name in action_data["ControlNames"]:
                ET.SubElement(user_action, "ControlName").text = control_name
        else:
            ET.SubElement(user_action, "ControlName").text = 'No Control Name'
 
        ET.SubElement(user_action, "ControlLabel").text = action_data["ControlLabel"]
        ET.SubElement(user_action, "ControlType").text = action_data["ControlType"]
        ET.SubElement(user_action, "Value").text = action_data["Value"]
        ET.SubElement(user_action, "ValueLabel").text = action_data["ValueLabel"]
 
    tree_out = ET.ElementTree(user_actions_with_details)
    tree_out.write('output.xml', encoding='UTF-8', xml_declaration=True)
 
# Run the function
extract_user_actions('recording.xml')
 
 