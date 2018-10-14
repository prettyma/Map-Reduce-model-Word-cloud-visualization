#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
#sorting
import csv, operator


current_word = None
current_count = 0
word = None

write_file = open('reducer_output_4-2_new.csv', 'w')
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
	count = int(count)
    except ValueError:
	# count was not a number, so silently
	# ignore/discard this line
	continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
	current_count += count
    else:
	if current_word:
	    # write result to STDOUT
	    write_file.write(current_word+','+str(current_count)+'\n')
	    #print '%s\t%s' % (current_word, current_count)
	current_count = count
	current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    write_file.write(current_word+','+str(current_count)+'\n')
    #print '%s\t%s' % (current_word, current_count)
wordCountList = csv.reader(open('reducer_output_4-2_new.csv'),delimiter=',')
data=[]
for row in wordCountList:
	if row:	
	     if len(row)==2:
		data.append(row)
#data = [row for row in wordCountList if row]
#data = [row for row in data if row[1]]
#sortedlist = sorted(wordCountList, key=operator.itemgetter(1),reverse=True)
sortedlist = sorted(data, key=lambda t: float(t[1]),reverse=True)
with open("sort_reducer_output_4-2_new.csv", "wb") as f:
          fileWriter = csv.writer(f, delimiter=',')
          for row in sortedlist:
              fileWriter.writerow(row)
	      print(row) 	
#print(wordCount)
write_file.close()
