import sys
import os
from turtle import width
from html2image import Html2Image
from PIL import Image


class HtmlReport:
    TEMPLATE_FILE_PATH = "htmlTemplate.html"

    split_html = ""
    user_sections = ""
    debug = False

    def __init__(self, _debug):
        self.debug = _debug
        if self.debug:
            print("Starting HtmlReport")
            print("Opening template: " + self.TEMPLATE_FILE_PATH)
        htmlTemplate = open(self.TEMPLATE_FILE_PATH, "r")
        self.split_html = self.split_html_text(htmlTemplate.read())

    def split_html_text(self, html_text):
        if self.debug:
            print("Splitting template")

        split_html = html_text.split("[SPLIT]")
        if len(split_html) <= 0:
            print("HTML Template incorrect!")
            return ""
        return split_html

    def add_section(self, text):
        if self.debug:
            print("Adding section: " + text)

        self.user_sections += '<div class="main">' + text + "</div>"

    def combine_html(self):
        if self.debug:
            print("Combining HTML")

        self.split_html.insert(1, self.user_sections)
        return " ".join(self.split_html)

    def save_to_file(self, file_path):
        if ".html" not in file_path:
            file_path += ".html"

        if self.debug:
            print("Writing to file: " + file_path)

        f = open(file_path, "w")
        f.write(self.combine_html())
        f.close()

        if(self.debug): print("Wrote to file: " + file_path)

        return file_path

    def save_to_img(self, file_path):
        file_path += ".jpg" 
        if self.debug:
            print("Saving to image")       
        h2i = Html2Image()
        h2i.screenshot(self.combine_html(), save_as=file_path, size=(225, 1000))
        
        if self.debug:
            print("Saved to image: " + file_path)    
        # self.crop_image(file_path)

    def crop_image(self, file_path):
        img = Image.open(file_path)
        if self.debug:
            print("Image width: " + str(img.width))

        if img.width > 225:
            left = 0
            top = 0
            right = 225
            bottom = img.height

            crop_img = img.crop((left, top, right, bottom))
            crop_img.convert("RGB").save(file_path)

            if self.debug:
                print("Cropped image: " + str(img.width / 2))


if __name__ == "__main__":
    htmlRep = HtmlReport(True)
    htmlRep.add_section("New section 1")
    htmlRep.add_section("New section 2\nTest test\nTest")
    htmlRep.add_section("New section 3\tTab")
    htmlRep.add_section("New section 4\t\tTabTab")
    htmlRep.add_section("New section 5<br>BRRrr")
    htmlRep.add_section("<img src=\"../Images/funkyDino.png\" width=\"90%\" margin=\"5%\">")

    #htmlRep.save_to_img("Output/new_test")
    htmlRep.save_to_file("Output/new_test")
