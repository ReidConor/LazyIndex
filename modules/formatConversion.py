#this module will contain functions related to converting a docuemnt to a text file for easier scoring
import os
import PyPDF2
import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

def sayHelloWorld ():
    print(3)

#depr this
def convertPdfToText_depr(pathToFile):
    pdfFileObj = open(pathToFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    filename = os.path.basename(pathToFile)

    destinationFile="data/" + filename + ".txt"
    numberOfPages = pdfReader.getNumPages()
    text_file = open(destinationFile, "w")
    for x in range(0, numberOfPages):
        pageObj = pdfReader.getPage(x)
        text_file.write(pageObj.extractText())

    text_file.close()
    return (destinationFile)


def convertPdfToText(pathToFile):
    #setup required objects
    output = io.StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)


    #read the pdf
    numberOfPages = 0
    pagenums = set()
    infile = open(pathToFile, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
        numberOfPages+=1
    infile.close()
    converter.close()

    #get the text from the pdf
    text = output.getvalue()
    output.close

    #write that text to a file
    filename = os.path.basename(pathToFile)
    destinationFile="data/" + filename + ".txt"
    text_file = open(destinationFile, "w")
    text_file.write(text)
    text_file.close()

    return (destinationFile, numberOfPages)
