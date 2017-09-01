import isbnlib

# isbnlib.registry.bibformatters = "json"
inputFile = "input.txt"
outputFile = open('output.csv', 'a')
f = open(inputFile)
with f:
    for line in f:
        outputFile.write(str(isbnlib.meta(line)))
        outputFile.write("\n")
