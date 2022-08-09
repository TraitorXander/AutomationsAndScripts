import csv
from locale import currency
import sys
import os
from numpy import average
# from hamcrest import none
# from numpy import empty
import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Files to import/read from
channel_csv_path = "ChannelsConfig_AE3x_UUT_20220722_1004.csv"
xml_config_path = "3005_DSG_CanCcp.xml"

average_dict = {"AverageName" : "AverageID"}
horusid_dict = {"MeasurementName" : "HorusID"}

def main():
    try:
        load_csv()
        #print(average_dict)
        # print(str(horusid_dict))
        # print(str(average_dict))
        process_config_xml()
    except Exception as exc:
        print("Exception caught in main()\n" + str(exc))

def load_csv():
    print("Loading CSV...")

    try:
        if(os.path.exists(channel_csv_path)):
            print("...")
            df = pd.read_csv(channel_csv_path, skip_blank_lines=True)
            csv_dict = pd.Series(df['ChannelID'].values, index = df['Phisycal Name']).to_dict()

            for x in csv_dict:
                if("_AVERAGE" in x):
                    average_dict[x] = csv_dict[x]
                else:
                    horusid_dict[x] = csv_dict[x]
                    
            print("Loaded channels into channel and average channel dictionaries")
        else:
            print("Could not find file: " + channel_csv_path)
            return

        if(df.empty):
            print("Nothing loaded from channel export CSV, stopping...")
            return
        
    except Exception as exc:
        print("Exception caught load_csv(): " + str(exc))
    
    print("Loaded CSV!")
        
def process_config_xml():
    print("Loading XML config file: " + xml_config_path)
    
    curr_ecu = ""
    curr_eng = ""

    try:
        tree = ET.parse(xml_config_path)
        root = tree.getroot()

        for averChan in average_dict:
            #print("Finding [" + averChan + " (" + str(average_dict[averChan]) + ")] in xml")
            splitAverChan = averChan.split("_")
            if(len(splitAverChan) >= 4):
                #print("Average: " + splitAverChan[len(splitAverChan)-1])
                #print("Engine: " + splitAverChan[len(splitAverChan)-2])
                #print("CCP: " + splitAverChan[len(splitAverChan)-3])
                if("AVERAGE" in splitAverChan[len(splitAverChan)-1]):
                    average = True
                else:
                    average = False
                    
                if(len(splitAverChan) >= 5):
                    #print("Channel: " + splitAverChan[len(splitAverChan)-5] +  "_" + splitAverChan[len(splitAverChan)-4])
                    #   0     1   2   3       4       5
                    #   tez   l   0   CCP1    AE31a   AVERAGE
                    channelName = splitAverChan[len(splitAverChan)-5] +  "_" + splitAverChan[len(splitAverChan)-4] + "_" + splitAverChan[len(splitAverChan)-3]
                    # channelName = ""
                    # ccpIndex = 0
                    # for x in splitAverChan:
                    #     if("CCP" in splitAverChan[ccpIndex]):
                    #         break
                    #     ccpIndex = ccpIndex + 1
                    # for x in range(0, ccpIndex):
                    #     channelName = channelName + splitAverChan[x]
                else:
                    #print("Channel: " + splitAverChan[len(splitAverChan)-4])
                    channelName = splitAverChan[len(splitAverChan)-4]
                
                if(average):
                    #print("Finding [" + channelName + " {" + splitAverChan[len(splitAverChan)-1] + "}] in XML now")

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
                                    meas_name = str(child_node.text)
                                elif(child_node.tag == "HorusID"):
                                    meas_horusid = str(child_node.text)
                                elif(child_node.tag == "AverageID"):
                                    aver_node = child_node
                                    
                            if(meas_name == channelName):
                                if("tez_" in channelName):
                                    print("2")
                                    
                                if(curr_eng == splitAverChan[len(splitAverChan)-2] and curr_ecu == splitAverChan[len(splitAverChan)-3]):
                                    if("tez_ " in channelName):
                                        print("3")
                                    
                                    print("Found correct channel: " + curr_ecu + ", " + curr_eng + ", " + meas_name + " [" + meas_horusid + "]")
                                    print("Adding average: " + averChan + " [" + str(average_dict[averChan]) + "]")
                                    aver_node.text = str(average_dict[averChan])
                                    
        print("Writing new XML...")
        dirname, filename = os.path.split(xml_config_path)
        tree.write(dirname + "NEW_" + filename, encoding='utf8')
        
        return
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
                        print("Grabbed "+ str(child_node.text))
                        meas_name = str(child_node.text)
                    elif(child_node.tag == "HorusID"):
                        meas_horusid = str(child_node.text)

                print(meas_horusid + " " + meas_name)
                

        print("Writing new XML...")
        dirname, filename = os.path.split(xml_config_path)
        tree.write(dirname + "NEW_" + filename, encoding='utf8')
    except Exception as exc:
        print("Exception caught in open_config_xml():\n" + str(exc))

if __name__ == "__main__":
    main()