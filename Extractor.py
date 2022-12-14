from PyPDF2 import PdfReader
import os
dir = os.path.dirname(__file__)
fileName = "Test.pdf" 
path = os.path.join(dir,"PDFs",fileName)
reader = PdfReader(f"{path}")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)     # Output Text on Console