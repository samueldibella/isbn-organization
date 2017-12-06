import sys
import urllib.request
import time
import re
from bs4 import BeautifulSoup

inputPath = "UTMtitles.txt"
outputPath = "UTM.csv"

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
                time.sleep(.1)
                string = line.replace("\n", "") #strip newline
                url = springerPath + string

                #  api call and categorization
                apiPath = urllib.request.urlopen(url)

                soup = BeautifulSoup(apiPath.read(), "html.parser")

                chapterString = soup.find("span", class_="chapter-count").contents
                chapterNumber = re.findall('\d+', chapterString[0])

                title = soup.find("p", class_="title").contents
                authors = soup.find("p", class_="authors").contents
                copyrightYear = soup.find("div", class_="copyright").contents


                """
                metadata = json.loads(apiPath.read())

                # add ebook isbn
                string += ", " + metadata['records']['electronicIsbn']

                # add number of chapters
                string += ", " + metadata['result'][0]
                """

                outputFile.write(string + ", " + chapterNumber[0] + ", " + title[0] + ", " + authors[0] + ", " + copyrightYear[0] + "\n")
                print("Success!: " + line.replace("\n", ""))

            except:
                outputFile.write(string + "\n")
                print("Sad!: " + line.replace("\n", ""))
