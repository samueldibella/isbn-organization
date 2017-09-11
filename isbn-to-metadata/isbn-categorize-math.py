import sys
import json
import urllib
import time

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
        time.sleep(5)
        
        # metadata is default read as JSON object & implicitly cast to dict
        string = line.replace("\n", "") #strip newline 
        gBooksHTML = urllib.urlopen(gBooksPath + string)
        
        metadata = json.loads(gBooksHTML.read())
        string += ", "
        
        try: 
            #if metadata description contains "undergrad"
            #else "grad
            #print metadata
           
            try: 
                if "undergrad" in metadata['items'][0]['volumeInfo']['description']:
                    string += "Undergrad"    
                else:
                    string += "Graduate"
            except:
                if "undergrad" in metadata['items'][0]['searchInfo']['textSnippet']:
                    string += "Undergrad (~)"    
                else:
                    string += "Graduate (~)"
            
            string += ", "
            
            bookTitle = metadata['items'][0]['volumeInfo']['title']
            # sorry this is so gross
            if "Analysis" in bookTitle and "-Analysis" not in bookTitle:
                string += "Analysis; "
            if "Topolog" in bookTitle:
                string += "Topology; "
            if "Probability" in bookTitle or "Stochastic" in bookTitle: #and stochastic
                string += "Probability Theory; "
            if "Logic" in bookTitle:
                string += "Logic; "
            if "Number Theory" in bookTitle:
                string += "Number Theory; "
            if "Application" in bookTitle or "Engineering" in bookTitle: #or engineering
                string += "Applications; "
            if "Comput" in bookTitle:
                string += "Computation; "
            if "Algebra" in bookTitle:
                string += "Algebra; "
          
            outputFile.write(string + "\n")
            print "Success!: " + line.replace("\n", "")
        except:
            outputFile.write(line)
            print "Sad!:" + line.replace("\n", "")
