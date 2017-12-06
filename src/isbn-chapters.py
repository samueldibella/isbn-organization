import sys
import urllib
import time
import re
from bs4 import BeautifulSoup

inputPath = "UTMtitles.txt"
outputPath = "output.csv"

springerPath = "http://www.springer.com/us/book/"
# springerPath = "https://api.springer.com/metadata/json?q=isbn:"
# apiKey = "&api_key=11546426cde8dcfabbadfec6cf3a7cdc"

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
        if len(line) > 18:
            outputFile.write(line)
            print("Already done!: " + line.replace("\n", ""))
            continue
        else:
            try:
                # should make  api calls less sad
                time.sleep(1)
                string = line.replace("\n", "") #strip newline
                url = springerPath + string
                print(url)

                # api call and categorization
                apiPath = urllib.urlopen(url)
                soup = BeautifulSoup(apiPath.read(), "html.parser")

                chapterString = soup.find(span, class_="chapter-count").content
                chapterNumber = re.findal('\d+', chapterString)



                """
                metadata = json.loads(apiPath.read())

                # add ebook isbn
                string += ", " + metadata['records']['electronicIsbn']

                # add number of chapters
                string += ", " + metadata['result'][0]
                """

                outputFile.write(string + ", " + chapterNumber + "\n")
                print("Success!: " + line.replace("\n", ""))

            except:
                outputFile.write(line)
                print("Sad!: " + line.replace("\n", ""))
