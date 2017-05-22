import os
import sys


def info(message):
    print ("[PYTHON]    ", message)

def getMetrics(FILE_NAME):
    info("Getting the word count.")

    resultsDict={}
    num_lines = 0
    num_words = 0
    num_chars = 0

    with open(FILE_NAME, 'r') as f:
        for line in f:
            words = line.split()

            num_lines += 1
            num_words += len(words)
            num_chars += len(line)

    resultsDict["num_lines"]=num_lines
    resultsDict["num_words"]=num_words
    resultsDict["num_chars"]=num_chars

    return resultsDict

def scalculateIndex(metrics):
    info("Calculating the LazyIndex")


if __name__ == "__main__":
    FILE=sys.argv[1]
    metrics = getMetrics(FILE)
    calculateIndex(metrics)
    #info (metrics["num_lines"])
    #info (metrics["num_words"])
    #info (metrics["num_chars"])
