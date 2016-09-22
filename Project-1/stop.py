#!/usr/bin/env python

"""
A filter that removes stop words.
"""

import fileinput
import re

def process(line):
    """For each line of input, retrieve all words in the line without special character and split into one word per line.
       Then remove the stop words."""
    
    line = re.findall(r'\w+',line)
    stopwords = ['and','the','to','a','e','i','o','u','t','s','of','her','it','in','you','that']
    
    for word in line:
        if word not in stopwords:
            print(word.strip())
            
for line in fileinput.input():
    process(line)
