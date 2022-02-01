import sys
import os
import pandas as pd
import pyperclip3 as pc

def main():
    try:
        df = pd.read_csv("MahaErrors.csv")
        create_switch(df)
    except Exception as exc:
        print("Error in main(): " + str(exc))

def create_switch(df):
        output_statement = "switch(input)\n{"

        for x in df.values:
            output_statement += "\ncase " + str(x[0]) + ":"
            output_statement += "\n\tresult = \"" + str(x[1]) + "\";"
            output_statement += "\n\tbreak;"

        output_statement += "\ndefault:\n\tbreak;\n}"

        pc.copy(output_statement)
        print(output_statement)

if __name__ == "__main__":
    main()