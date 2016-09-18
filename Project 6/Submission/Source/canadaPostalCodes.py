'''
Created on Dec 6, 2015

@author: Nathan Guenther
'''

import re

# Ask user for file input
fileName = input('Please enter the name of the file containing the input Canadian postal codes: ')

# Read and save file data
fileObj = open(fileName, 'r')
allLines = fileObj.readlines()
fileObj.close()

# Regular Expression
test = '[ABCEGHJKLMNPRSTVXY][0-9][ABCEGHJKLMNPRSTVWXYZ] ?[0-9][ABCEGHJKLMNPRSTVWXYZ][0-9]'

print('\n\n')

# Check each IP address
for eachLine in allLines:
    #Regex check
    if re.search("[ABCEGHJKLMNPRSTVXY][0-9][ABCEGHJKLMNPRSTVWXYZ] ?[0-9][ABCEGHJKLMNPRSTVWXYZ][0-9]", eachLine , re.IGNORECASE | re.DOTALL):
        print("Match found - valid Canadian address: ", eachLine)
    else: 
        print("Error - no match - invalid Canadian address: ", eachLine)
        

