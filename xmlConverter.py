import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from collections import defaultdict

def extract_user_actions(input_xml, output_xml='output.xml'):
    try:
        tree = ET.parse(input_xml)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return
    except FileNotFoundError:
        print(f"File not found: {input_xml}")
        return

    namespaces = {
        '': 'http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.Client.ServerForm.TaskRecording',
        'd2p1': 'http://schemas.microsoft.com/2003/10/Serialization/Arrays',
        'd7p1': 'http://schemas.microsoft.com/2003/10/Serialization/Arrays',
        'i': 'http://www.w3.org/2001/XMLSchema-instance',
        'z': 'http://schemas.microsoft.com/2003/10/Serialization/'
    }

    user_actions_with_details = ET.Element("UserActionsWithDetails")
    user_actions = root.findall(".//UserActions//d2p1:anyType", namespaces=namespaces)

    grouped_actions = defaultdict(lambda: {
        "description": "",
        "sequence": None,
        "control_names": [],
        "from_nav_path": False,
        "control_label": "",
        "control_type": "",
        "value": ""
    })

    for index, action in enumerate(user_actions):
        ref = action.attrib.get("{http://schemas.microsoft.com/2003/10/Serialization/}Ref")
        node = root.find(f".//Node[@z:Id='{ref}']", namespaces=namespaces)

        if node is None:
            continue

        entry = grouped_actions[ref]
        if entry["sequence"] is None:
            entry["sequence"] = index + 1

        desc_elem = node.find(".//Description", namespaces=namespaces)
        if desc_elem is not None and desc_elem.text:
            entry["description"] = desc_elem.text

        control_label_elem = node.find(".//ControlLabel", namespaces=namespaces)
        if control_label_elem is not None and control_label_elem.text:
            entry["control_label"] = control_label_elem.text

        control_type_elem = node.find(".//ControlType", namespaces=namespaces)
        if control_type_elem is not None and control_type_elem.text:
            entry["control_type"] = control_type_elem.text

        control_name_elem = node.find(".//ControlName", namespaces=namespaces)
        if control_name_elem is not None and control_name_elem.text:
            name = control_name_elem.text.strip()
            if name != "Grid" or entry["control_type"] != "Grid":
                entry["control_names"].append(name)
                entry["from_nav_path"] = False
        else:
            nav_path = node.find(".//NavigationPath", namespaces=namespaces)
            if nav_path is not None:
                for part in nav_path.findall(".//d7p1:string", namespaces=namespaces):
                    if part.text:
                        entry["control_names"].append(part.text.strip())
                entry["from_nav_path"] = True

        value_elem = node.find(".//Annotations//Annotation//CanonicalUserAction//Value", namespaces=namespaces)
        if value_elem is not None and value_elem.text:
            entry["value"] = value_elem.text.strip()

    for ref, data in sorted(grouped_actions.items(), key=lambda x: x[1]["sequence"]):
        user_action = ET.SubElement(user_actions_with_details, "UserAction")
        user_action.set("Ref", ref)
        ET.SubElement(user_action, "Description").text = data["description"]
        ET.SubElement(user_action, "NodeId").text = ref
        ET.SubElement(user_action, "Sequence").text = str(data["sequence"])

        if data["from_nav_path"]:
            for nav in data["control_names"]:
                ET.SubElement(user_action, "Navigation").text = nav
        elif data["control_names"]:
            ET.SubElement(user_action, "ControlName").text = data["control_names"][0]

        ET.SubElement(user_action, "ControlLabel").text = data["control_label"]
        ET.SubElement(user_action, "ControlType").text = data["control_type"]
        ET.SubElement(user_action, "Value").text = data["value"]

    xml_str = ET.tostring(user_actions_with_details, encoding='utf-8')
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="  ")

    with open(output_xml, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

# Run the function
extract_user_actions("recording.xml")
