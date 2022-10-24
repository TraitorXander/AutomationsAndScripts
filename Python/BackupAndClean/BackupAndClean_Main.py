import configparser
import sys
import os
from ConfigurationParser import ConfigParserXML

backup_to = ""
backup_paths = []

delete_older_than = 30
filter = []
clean_paths = []

def load_config():
    try:
        print("Loading config...")
        cp = ConfigParserXML()
        if(cp.is_backup_enabled()):
            print("Running backup...")
            backup_to, backup_paths = cp.get_backup_config()
            print(backup_to)
            print(backup_paths)
        
        if(cp.is_spring_clean_enabled()):
            print("Cleaning...")
            delete_older_than, filter, clean_paths = cp.get_spring_clean_config()
            print(delete_older_than)
            print(filter)
            print(clean_paths)

    except Exception as exc:
        print("Exception caught:\n" + str(exc))

def main():
    load_config()

if __name__ == "__main__":
    main()
