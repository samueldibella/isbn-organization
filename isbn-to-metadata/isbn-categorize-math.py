import sys
import json
import urllib

inputPath = "input.txt"
outputPath = "output.csv"

gBooksPath = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

if len(sys.argv) != 2:
    print("Using default i/o paths, where possible")
else:
    inputPath = str(sys.argv[1])
    outputPath = str(sys.argv[2])

f = open(inputPath)
outputFile = open(outputPath, 'a')

metadata = {}
lineBuff = ""
bookDescription = ""
bookTitle = ""

with f:
    for line in f:
        # metadata is default read as JSON object & implicitly cast to dict
        string = line.replace("\n", "") #strip newline 
        gBooksHTML = urllib.urlopen(gBooksPath + string)
        
        metadata = json.loads(gBooksHTML.read())
        string += ", "
        
        if metadata is not None and metadata['totalItems'] is not 0: 
            #if metadata description contains "undergrad"
            #else "grad
            print metadata
            if "undergraduate" in metadata['items'][0]['volumeInfo']['description']:
                string += "Undergrad"    
            else:
                string += "Graduate"
            
            string += ", "
            
            bookTitle = metadata['items'][0]['volumeInfo']['title']
            # sorry this is so gross
            if "Analysis" in bookTitle:
                string += "Analysis; "
            if "Topolog" in bookTitle:
                string += "Topology; "
            if "Probability" or "Stochastic" in bookTitle: #and stochastic
                string += "Probability Theory; "
            if "Logic" in bookTitle:
                string += "Logic; "
            if "Number Theory" in bookTitle:
                string += "Number Theory; "
            if "Application" or "Engineering" in bookTitle: #or engineering
                string += "Applications; "
            if "Comput" in bookTitle:
                string += "Computation; "
            if "Algebra" in bookTitle:
                string += "Algebra; "
          
            outputFile.write(string +"\n")
            
        else: 
            outputFile.write("Error with ISBN: " + line)
