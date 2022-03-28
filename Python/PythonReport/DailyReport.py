from datetime import datetime
import sys
import os
from HTMLCreator import HtmlReport

def main():
    print("Creating report...")
    html_creator = HtmlReport
    
    html_creator.add_section(section_1())
    html_creator.save_to_img()

def section_1():
    text = "<img href=\"funkyDino.png\">"
    text += "<u>Alex's Report</u>\n"
    text += datetime.now("%Y-%m-%d %H:%M")
    return text

if __name__ == "__main__":
    main()