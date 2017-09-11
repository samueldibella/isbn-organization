import os

def main():
    categoryPath = "categories/"
    inputPath = "input.txt"
    outputPath = "output.csv"

    inputFile = open(inputPath, 'r')
    outputFile = open(outputPath, 'a')
    
    for inputLine in inputFile:
        string = inputLine.strip('\n')
        reader = ""
        foundISBN = False
        
        for subjectFile in os.listdir(categoryPath):
            f = open(categoryPath + subjectFile, 'r')
            reader = f.read()
            
            if string in reader:
                string += ", " + os.path.basename(f.name).strip('.txt')
                foundISBN = True
           
        if not foundISBN:
            string += ", None"
            
        outputFile.write(string.strip('\n') + "\n")

main()
