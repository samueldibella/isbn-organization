import isbnlib

inputFile = "input.txt"
outputFile = open('output.csv', 'a')
f = open(inputFile)

metadata = {}

with f:
    for line in f:
        # metadata is default read as JSON object & implicitly cast to dict
        metadata = isbnlib.meta(line)

        outputFile.write(metadata['Title'] + ", ")
        # Authors returns as a list, so string cast and separator needed
        outputFile.write("; ".join(metadata['Authors']) + ", ")
        outputFile.write(metadata['Year'] + ", ")
        outputFile.write(metadata['ISBN-13'])

        outputFile.write("\n")
