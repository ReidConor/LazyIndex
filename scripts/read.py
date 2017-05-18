import os
import sys
import PyPDF2
from collections import Counter

def readInFile(file):
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    return pdfReader


def writeToTextFile(reader, filename):
    text_file = open(filename + ".txt", "w")
    pageObj = reader.getPage(0)
    text_file.write(pageObj.extractText())
    text_file.close()

def analyzeDoc(file):
    textFile = open(file)
    wordcount = Counter(textFile.read().split())
    for item in wordcount.items(): print("{}\t{}".format(*item))

    print(wordcount)

if __name__ == "__main__":
    os.system('clear')
    filename = os.path.splitext(sys.argv[1])
    reader = readInFile(sys.argv[1])
    writeToTextFile(reader, filename[0])
    analyzeDoc(filename[0] + ".txt")
