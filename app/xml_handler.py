import xml.etree.ElementTree as ET

def to_xml(data_dict):
    root = ET.Element("FirewallScanResult")
    for key, value in data_dict.items():
        ET.SubElement(root, key).text = value
    return ET.tostring(root, encoding='unicode')
