import sys
import os
import shutil
from datetime import datetime

class BackupHandler:

    def run_backup(self, paths, destination):
        for path in paths:
            print(path)
            zip_path = os.path.join(destination, datetime.now().strftime('%Y-%m-%d')  + "_" + path)
            if(os.path.exists(zip_path)):
                zip_path = zip_path + "_1"
            shutil.make_archive(zip_path, "zip", path)
            print("Achived {0} to {1}".format(os.path.abspath(path), os.path.abspath(zip_path)))

if __name__ == "__main__":
    bh = BackupHandler()
    list_paths = []
    list_paths.append("Test\TestFolder")
    list_paths.append("Test\TestFolder2")
    bh.run_backup(list_paths, "Test\BackupDestination")