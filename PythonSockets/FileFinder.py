import sys, os

def main(path):
    lstFiles = []

    print("Searching Path: " + path)
    
    for root, dirs, files in os.walk(path):
        # print("\nROOT: " + str(root))
        # print("DIRS: " + str(dirs))
        # print("FILES: " + str(files))

        for file in files:
            lstFiles.append(file)

    lstFiles.sort()

    for x in range(0, len(lstFiles)):
        #if('dll' in str(lstFiles[x])):
        print(str(x) + ": " + str(lstFiles[x]))

if __name__ == '__main__':
    print('Starting...')
    if(len(sys.argv) > 1):
        main(sys.argv[1])
    else:
        main(os.getcwd())