###
#
# The aim of this program is to open the pdf file
# based on previous opened page and after you
# finish your reading session you need to write in
# the console phrase: "done", program will read the last
# page that will be the current page where you stopped.
# And page number will be saved in the txt file, it means
# that we will need to open in write mode txt file
# and add, regarding with string pattern current page num
#
###

###
# There are two ways to get the current page where user
# finish reading, first one:
##
# 1) open file using built-in function open from module web
# and then try to get the current page number using PyPDF2
# module
##
# 2) open file using built-in function open from module web
# and then using selenium get the current page number
###

from PyPDF2 import PdfFileReader
import webbrowser as wb
from bs4 import BeautifulSoup

global path
path = "book/Django_3_By_Example_Build_powerful_and_reliable_Python_web_applications.pdf"


def pdf_read(path__file=path):

    # open file in read mode:
    file__location = open(path__file, "rb")

    # # first way:
    # inp = PdfFileReader(file__location)
    # global page_13
    # # opens page with number:
    # page_13 = inp.getPage(13)
    # print(page_13)


if __name__ == '__main__':
    pdf_read()

    # # first way:
    # # get the text of the page:
    # page_data = page_13.extractText()
    # print(page_data)

    # opens file by defined path
    wb.open(fr'{path}')

