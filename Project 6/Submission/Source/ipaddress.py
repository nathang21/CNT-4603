'''
Created on Dec 6, 2015

@author: Nathan Guenther
'''

import re

# Ask user for file input
fileName = input('Please enter the name of the file containing the input IP addresses: ')

# Read and save file info
fileObj = open(fileName, 'r')
allLines = fileObj.readlines()
fileObj.close()

# Regular Expression
test = '^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'

print('\n\n')

# Check each IP address
for eachLine in allLines:
    #Regex checkSub
    if re.search(test, eachLine):
        print("Match found - valid IP address: ", eachLine)
    else: 
        print("Error - no match - invalid IP address: ", eachLine)
        

