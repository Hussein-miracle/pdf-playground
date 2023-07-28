import PyPDF2


template = PyPDF2.PdfReader(open('mod.pdf','rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf','rb'))

output = PyPDF2.PdfWriter()


for i in range(len(template.pages)):
  page = template.pages[i]
  # print(page)
  page.merge_page(watermark.pages[0])
  
  output.add_page(page)
  
  
  with open('watermarked_output.pdf','wb') as file:
    output.write(file)
