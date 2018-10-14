#!/usr/bin/env python
"""mapper.py"""

import sys

topWordList=[]
topWordList.append('gun')
topWordList.append('people')
topWordList.append('school')
topWordList.append('guns')
topWordList.append('facebook')
topWordList.append('rifle')
topWordList.append('times')
topWordList.append('control')
topWordList.append('common')
topWordList.append('high')
topWordList.append('last')
topWordList.append('president')
topWordList.append('think')
topWordList.append('house')
topWordList.append('know')
topWordList.append('public')
topWordList.append('companies')
topWordList.append('first')
topWordList.append('american')
topWordList.append('home')

# stop words apk
import nltk 
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

#for multiple delimiters
import re
import string

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = re.split('[:",. ]',line)
   
    # increase counters
    for word in words:
	word = word.lower()
	word = word.strip()
	#word = word.strip(string.punctuation)
	#print (word)
	if word in topWordList:
		for wordCheck in words:
			if word != wordCheck and wordCheck in topWordList:
				print '%s-%s\t%s' % (word,wordCheck, 1)