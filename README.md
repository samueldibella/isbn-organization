# Scripts for Scraping/Cleaning Book Metadata

## isbn-to-metadata
This program reads an input text file of ISBN-13 strings, separated by newlines, searches WorldCat and Google Books, using isbnlib methods, and exports matching titles, authors, and pub years (+ original ISBN-13 number) into a .csv (so they can be put in Excel). If there are multiple ISBN errors in a row, rerunning the script on those ISBNs tends to correctly generate their metadata. 

## isbn-categorize
Takes an input file of ISBN strings, and checks them against a set of ISBN-list files (named for the category). Output specifies which category each of the input ISBNs falls into. 

## isbn-categorize-math
Use gBooks and isbnDB to guess whether a set of texts are undergraduate/graduate level and what subfield of mathematics they  fit into

## corpora-topics
Work in progress (so everything is ugly) to build an implementation of latent semantic analysis for topic modeling (using gensim library). The hope is to eventually be able to take a snapshot of published papers in repositories and, by comparing snapshots, describe whether subfields are becoming more active or declining in popularity. (Currently basing the work off of arXive's API.) Needless to say, this is a very ambitious goal. 
