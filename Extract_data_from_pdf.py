import PyPDF2
pdf_obj =open(r"C:\Python312\tree.pdf","rb")
pdf_reader=PyPDF2.PdfReader(pdf_obj)
print(len(pdf_reader.pages))
page_obj = pdf_reader.pages[0]
print(page_obj.extract_text())
pdf_obj.close()
