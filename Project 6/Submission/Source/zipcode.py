'''
Created on Dec 6, 2015

@author: Nathan Guenther
'''

import re

# Ask user for input file
fileName = input('Please enter the name of the file containing the input zipcodes: ')

# Read and save file contents
fileObj = open(fileName, 'r')
allLines = fileObj.readlines()
fileObj.close()

# Regular Expression
test = '^\d{5}(?:[-\s]\d{4})?$'

print('\n\n')
# Check each zip code
for eachLine in allLines:
    #Regex check
    if re.search(test, eachLine):
        print("Match found - valid U.S. zipcode: ", eachLine)
    else: 
        print("Error - no match - invalid U.S. zipcode: ", eachLine)
        