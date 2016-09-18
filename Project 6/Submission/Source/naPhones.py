'''
Created on Dec 6, 2015

@author: Nathan Guenther
'''

import re

#Ask user for file input
fileName = input('Please enter the name of the file containing the input North American phone numbers: ')

# Read in and save file contents
fileObj = open(fileName, 'r')
allLines = fileObj.readlines()
fileObj.close()

# Regular Expression
test = '\D*([2-9]\d{2})(\D*)([2-9]\d{2})(\D*)(\d{4})\D*'

print('\n\n')

# Check each zip code
for eachLine in allLines:
    #Regex check
    if re.search(test, eachLine):
        print("Match found - valid North American phone number: ", eachLine)
    else: 
        print("Error - no match - invalid North American phone number: ", eachLine)
        