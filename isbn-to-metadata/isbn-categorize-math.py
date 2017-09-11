import sys
import json
import urllib
import time

def levelCat(description, certain):
    """ Guess student level book is intended for """

    if "undergrad" in description:
        level = "Undergrad"    
    else:
        level = "Graduate"
    
    if not certain: 
        level += "(~)"
        
    return level
    
def bookCat(bookTitle):
    """ Try to categorize math subfield of book """

    categoryString = ""
    
    if "Analysis" in bookTitle and "-Analysis" not in bookTitle:
        categoryString += "Analysis; "
    if "Topolog" in bookTitle:
        categoryString += "Topology; "
    if "Probability" in bookTitle or "Stochastic" in bookTitle: #and stochastic
        categoryString += "Probability Theory; "
    if "Logic" in bookTitle:
        categoryString += "Logic; "
    if "Number Theory" in bookTitle:
        categoryString += "Number Theory; "
    if "Application" in bookTitle or "Engineering" in bookTitle: #or engineering
        categoryString += "Applications; "
    if "Comput" in bookTitle:
        categoryString += "Computation; "
    if "Algebra" in bookTitle:
        categoryString += "Algebra; "
        
    return categoryString

####

inputPath = "input.txt"
outputPath = "output.csv"

gBooksPath = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
isbndbPath = "http://isbndb.com/api/v2/json/5QXMWUUV/book/"

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
        
        # so you can rerun analysis on same file
        if len(line) > 15:
            outputFile.write(line)
            print "Already done!:" + line.replace("\n", "")
            continue
        else:
            
            try:
                # should make  api calls less sad
                time.sleep(3)
                string = line.replace("\n", "") #strip newline 
                
                # api call and categorization
                try:
                    apiPath = urllib.urlopen(gBooksPath + string)
                    metadata = json.loads(apiPath.read())

                    try:
                        string += ", " + levelCat(metadata['items'][0]['volumeInfo']['description'], True)
                    except:
                        string += ", " + levelCat(metadata['items'][0]['searchInfo']['textSnippet'], False)

                    string += ", " + bookCat(metadata['items'][0]['volumeInfo']['title'])
              
                    outputFile.write(string + "\n")
                    print "Success!: " + line.replace("\n", "")
                
                # if Google doesn't have data, switch to isbnDB
                except:
                    apiPath = urllib.urlopen(isbndbPath + string)
                    metadata = json.loads(apiPath.read())
                
                    string += ", " + levelCat(metadata['data'][0]['summary'], True)
                    
                    string += ", " + bookCat(metadata['data'][0]['title_latin'])
              
                    outputFile.write(string + "\n")
                    print "Success!: " + line.replace("\n", "")
            
                string += ", "
                    # uses other metadata field if full description is not available
                         
            except:
                outputFile.write(line)
                print "Sad!:" + line.replace("\n", "")
