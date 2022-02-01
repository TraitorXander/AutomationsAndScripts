import csv
from locale import currency
import sys
import os
from hamcrest import none
from numpy import empty
import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom import minidom

channel_csv_path = "20220131_ChannelExport.csv"
xml_config_path = "3005_DSG_CanCcp.xml"

def main():
    try:
        csv_dict = load_csv()
        print(csv_dict)
        process_config_xml(csv_dict)
    except Exception as exc:
        print("Exception caught in main()\n" + str(exc))

def load_csv():
    print("Loading CSV...")

    try:
        if(os.path.exists(channel_csv_path)):
            print("...")
            df = pd.read_csv(channel_csv_path, skip_blank_lines=True)
            csv_dict = pd.Series(df['ChannelID'].values, index = df['Phisycal Name']).to_dict()
        else:
            print("Could not find file: " + channel_csv_path)
            return

        if(df.empty):
            print("Nothing loaded from channel export CSV, stopping...")
            return
        
        return csv_dict

    except Exception as exc:
        print("Exception caught load_csv(): " + str(exc))
    
    print("Loaded CSV!")
    
def process_config_xml(xml_dict):
    print("Loading XML config file: " + xml_config_path)
    
    curr_ecu = ""
    curr_eng = ""

    try:
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
                        print("Grabbed: " + str(child_node.text))
                        meas_name = str(child_node.text)
                    elif(child_node.tag == "HorusID"):
                        meas_horusid = str(child_node.text)

                print(meas_horusid + " " + meas_name)

                if(meas_name != ""):
                    meas_name_updated = meas_name + "_" + curr_ecu + "_" + curr_eng
                    print("1: " + meas_name_updated)
                    new_horusid = str(xml_dict[meas_name_updated])
                    print("2: " + new_horusid)
                    new_node = ET.Element("HorusID")
                    print("3: " + str(new_node))
                    new_node.text = new_horusid
                    iter_node.append(new_node)

        print("Writing new XML...")
        dirname, filename = os.path.split(xml_config_path)
        tree.write(dirname + "NEW_" + filename, encoding='utf8')
    except Exception as exc:
        print("Exception caught in open_config_xml():\n" + str(exc))

if __name__ == "__main__":
    main()