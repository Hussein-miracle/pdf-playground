import PyPDF2
import sys


inputs = sys.argv[1:]



# with open('./dummy.pdf','rb') as file:
#   # print(file)
#   reader = PyPDF2.PdfReader(file)
#   # print(len(reader.pages),'reader')
#   page = reader.pages[0]
#   # print(page.rotate(90),'page')
#   page.rotate(270)
#   writer = PyPDF2.PdfWriter()
#   writer.add_page(page)
#   with open('tilt.pdf','wb') as file:
#     writer.write(file)




def pdf_combiner(pdf_list:list):
  merger = PyPDF2.PdfMerger()
  for pdf in pdf_list:
    print(pdf)
    merger.append(pdf)
  merger.write('mod.pdf')
    
    
pdf_combiner(inputs)