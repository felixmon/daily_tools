# split text with multiple separators from a text file and write the result to a new text file.

import sys
import os
import re

# open the source file to read
f = open('1.txt','r')
# open the destination file to write
f2 = open('2.txt','w')
# state the list type variable 'result'
result=[]

# read each line and split
# use regex split method to split with multiple separators
for item in f.readlines():
    result.append(re.split('，|。',item))

# write the result into new text file
# the reason that using two loops is that 'result' has two levels of list, and you cannot write a list directly to a text file, 
# or it will raise a Type error: TypeError: write() argument must be str, not list
for item in result:
    for item2 in item:
        f2.write(item2)
        f2.write('\n')
