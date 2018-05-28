#this is the main module that will be run each time, taking the pdf as an argument
import os
import sys
from modules import formatConversion

if __name__ == "__main__":
    os.system('clear')

    if (len(sys.argv) < 2):
        print ("No pdf supplied. Exiting")
        exit(1)

    pathToFile = sys.argv[1]
    outputFile, numberOfPages = formatConversion.convertPdfToText(pathToFile)
    
