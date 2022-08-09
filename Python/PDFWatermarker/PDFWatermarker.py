import sys
from PyPDF4 import PdfFileReader, PdfFileWriter

def PDFWatermarker(input_file_path, output_file_path, watermark_file_path):
    input_file_path = input_file_path
    output_file_path = output_file_path
    watermark_file_path = watermark_file_path
    
    print("1. Initialising watermark, reading: " + input_file_path)
    
    try:
        print("Debug 1")
        watermark_read = PdfFileReader(watermark_file_path)
        print("Debug 2")
        watermark_page = watermark_read.getPage(0)
        
        print("2. Making new file using watermark: " + watermark_file_path)
    
        pdf_reader = PdfFileReader(input_file_path)
        print("Debug 3")
        pdf_writer = PdfFileWriter(output_file_path)
        
        print("Debug 4")
        for page in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page)
            page.mergePage(watermark_page)
            pdf_writer.addPage(page)
        
        print("3. Writing new file to: " + output_file_path)
        print(type(pdf_writer))
        pdf_writer.write()
        
    except Exception as e:
        print("Error: " + str(e))
        sys.exit()
            
if __name__ == '__main__':
    print('PDFWatermarker.py')
    print(".\TestPDF\test.pdf" + ".\TestPDF\draft.pdf" + ".\TestPDF\output.pdf")
    if(len(sys.argv) == 3):
        pdfwm = PDFWatermarker(sys.argv[0], sys.argv[1], sys.argv[2])
    else:
        PDFWatermarker(input_file_path="test.pdf", watermark_file_path="draft.pdf", output_file_path="output.pdf")