import sys
import os

path = "E:\\Customer Tickets\\PSP - CAC mods\\2022-01-04 CAC loop test modifications"

def folders_in_folder():
    print("Starting...")
    try:
        if(os.path.exists(path)):
            if(len(os.listdir(path)) > 0):
                output_file = os.path.basename(path) + ".csv"
                print("Outputting to " + output_file)
                with open(output_file, "w") as f:
                    f.write(path + "\n")
                    for x in os.listdir(path):
                        f.write(x + ",\n")
        else:
            print("Path doesnt exist")
    except Exception as exc:
        print("Exception: " + str(exc))

if __name__ == "__main__":
    folders_in_folder()