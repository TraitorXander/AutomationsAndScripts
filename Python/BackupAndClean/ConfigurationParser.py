import sys
import os
from bs4 import BeautifulSoup as BS

class ConfigParserXML:
    backup_enabled = False
    backup_to = ""
    backup_paths = []

    springclean_enabled = False
    delete_older_than = 5
    filters = []
    clean_paths = []
    
    def __init__(self):
        with open("Config.xml", "r") as f:
            content = f.read()
            xmlcontent = BS(content, features="xml")

            self.backup_enabled = xmlcontent.BackupAndClean_Config.Backup.attrs["enabled"]

            if(self.backup_enabled):
                self.backup_to = xmlcontent.BackupAndClean_Config.Backup.BackupLocation.text

                backup_paths_nodes = xmlcontent.BackupAndClean_Config.Backup.BackupPaths
                for x in backup_paths_nodes:
                    if(len(x.text) > 1):
                        self.backup_paths.append(x.text)

            self.springclean_enabled = xmlcontent.BackupAndClean_Config.SpringClean

            if(self.springclean_enabled):
                self.delete_older_than = int(xmlcontent.BackupAndClean_Config.SpringClean.DeleteOlderThan.text)

                filters_node = xmlcontent.BackupAndClean_Config.SpringClean.Filter.text
                self.filters = filters_node.split(',')

                clean_paths_nodes = xmlcontent.BackupAndClean_Config.SpringClean.CleanPaths
                for x in clean_paths_nodes:
                    if(len(x.text) > 1):
                        self.clean_paths.append(x.text)

    def is_backup_enabled(self):
        return self.backup_enabled

    def get_backup_config(self):
        return self.backup_to, self.backup_paths

    def is_spring_clean_enabled(self):
        return self.springclean_enabled

    def get_spring_clean_config(self):
        return self.delete_older_than, self.filters, self.clean_paths