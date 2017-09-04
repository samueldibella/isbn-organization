# Scripts for Scraping/Cleaning Book Metadata

## isbn-to-metadata
This program reads an input text file of ISBN-13 strings, separated by newlines, searches WorldCat and Google Books, using isbnlib methods, and exports matching titles, authors, and pub years (+ original ISBN-13 number) into a .csv (so they can be put in Excel). If there are multiple ISBN errors in a row, rerunning the script on those ISBNs tends to correctly generate their metadata. 
