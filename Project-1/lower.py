#!/usr/bin/env python

"""
A filter that transforms all the words to lower case words.
"""

import fileinput

def process(line):
    """For each line of input, all characters have been stripped from the beginning and the end of the string."""
    print(line.strip())

for line in fileinput.input():
    process(line.lower())
