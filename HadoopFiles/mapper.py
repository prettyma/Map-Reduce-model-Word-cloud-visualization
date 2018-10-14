#!/usr/bin/env python
"""mapper.py"""

import sys
reload(sys)
sys.setdefaultencoding('utf8')
#import enchant
#dictionary = enchant.Dict("en_US")
from nltk.corpus import words


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
    #words = line.split()
    #words = line.split('.| ')
    wordsList = re.split('[:",. \'\/@-]',line)
    #pattern = re.compile(r';|, ')
    #words = pattern.split(line)
    #words = nltk.word_tokenize(unicode(line))

    # increase counters
    for word in wordsList:
	word = word.lower()
	word = word.strip()
	#word = word.strip(string.punctuation)
	#print (word)
	if word and word not in stop_words:
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		#
		# tab-delimited; the trivial word count is 1
		if word[0].isdigit():	
			continue
		if word[0].startswith('\xe2'):
			continue
		if word[0].startswith('_'):
			continue
		if word[0].startswith('\xc2'):
			continue
		if word[0].startswith(')'):
			continue
		if word[0].startswith('&'):
			continue
		if word[0].startswith('$'):
			continue
		if word[0].startswith('['):
			continue
		if word[0].startswith('('):
			continue
		print '%s\t%s' % (word, 1)
		#try:
		#	if word in words.words()
		#		print '%s\t%s' % (word, 1)
		#except:
		#	continue