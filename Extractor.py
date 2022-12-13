from PyPDF2 import PdfReader
import os
dir = os.path.dirname(__file__)
fileName = "Academic Planner 2022 23 ODD.pdf" 
path = os.path.join(dir,"PDFs",fileName)
reader = PdfReader(f"{path}")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)     # Output Text on Console