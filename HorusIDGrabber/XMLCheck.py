import sys
import os

import xml.etree.ElementTree as ET

xml_config_path = "3000_DSG_CanCcp.xml"

def open_config_xml():
    print("Loading XML config file...")
    chan_dict = {}

    curr_ecu = ""
    curr_eng = ""

    try:
        if(os.path.exists(xml_config_path)):
            tree = ET.parse(xml_config_path)
            root = tree.getroot()
            for iter_node in root.iter():
                if(iter_node.tag == "ECU"):
                    curr_ecu = iter_node.attrib["ecuPrefix"].replace(' ', '')
                    curr_eng = iter_node.attrib["engPrefix"].replace(' ', '')
                elif(iter_node.tag == "Measurement"):
                    meas_name = ""
                    meas_horusid = ""
                    # Loop over HorusID, Name, Units, Description, DataType
                    for child_node in iter_node.iter():
                        if(child_node.tag == "Name"):
                            meas_name = child_node.text
                        elif(child_node.tag == "HorusID"):
                            meas_horusid = child_node.text

                    chan_dict[meas_horusid] = meas_name + "_" + curr_ecu + "_" + curr_eng
    
        print(chan_dict)
    
    except Exception as exc:
        print(str(exc))


if __name__ == "__main__":
    open_config_xml()