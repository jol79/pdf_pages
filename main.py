from PyPDF2 import PdfFileReader
from PyPDF2 import *
import webbrowser as wb
import os.path

global path
path = "book/Django_3_By_Example_Build_powerful_and_reliable_Python_web_applications.pdf"


def pdf_read(path__file=path):
    # pdf = PdfFileReader(open(path, 'rb'))
    # print("File path: ", pdf)
    file__location = open(path__file, "rb")
    inp = PdfFileReader(file__location)
    page_13 = inp.getPage(13)
    print(page_13)

    file__location.close()
    print(file__location)


if __name__ == '__main__':
    pdf_read()
    wb.open(fr'{path}')


