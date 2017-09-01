import sys
import isbnlib

inputPath = "input.txt"
outputPath = "output.csv"

if len(sys.argv) != 2:
    print("Using default i/o paths, where possible")
else:
    inputPath = str(sys.argv[1])
    outputPath = str(sys.argv[2])

f = open(inputPath)
outputFile = open(outputPath, 'a')


metadata = {}

with f:
    for line in f:
        # metadata is default read as JSON object & implicitly cast to dict
        metadata = isbnlib.meta(line)
        
        if metadata is not None: 
            outputFile.write((metadata['Title'] + ", ").encode('utf-8'))
            # Authors returns as a list, so string cast and separator needed
            outputFile.write(("; ".join(metadata['Authors']) + ", ").encode('utf-8'))
            # outputFile.write(metadata['Volume'] + ", ") 
            outputFile.write(metadata['Year'] + ", ")
            outputFile.write(metadata['ISBN-13'])
            outputFile.write("\n")
        else: 
            outputFile.write("Error with ISBN: " + line)
            
