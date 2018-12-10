#Lab 17
#Lab Problem for Today:
#Start with the Green Eggs and Ham word count lab.  
#In this lab, you printed to the screen a list of every word in Green Eggs and Ham and how often it appeared. For today's lab, 
#(1) First, modify your Green Eggs and Ham lab so that instead of printing the words and counts to the screen, it writes them out to an .html file.  
#You should be able to open your html file in a browser to see the results of your word count
#(2) Now, instead of printing the counts for each word, modify the color/size/weight of the word to reflect its frequency in the file.  
#You will probably want to break the counts into ranges for this (e.g. words with a count between 30 and 40 have one color/size, etc).  
#Here is a screen shot showing part of one potential outcome (be creative, this is by no means *the* answer, hopefully every group will have a different product for this lab)

import urllib
import os


def read():
  #use os library to refer to filename
  directory = os.path.dirname(__file__)
  
  #Opens Green Eggs and Ham File. Reads it into text form. Then closes file.
  fileName = os.path.join(directory, 'eggs.txt')
  file = open(fileName,"r")
  original = file.read()
  file.close()
  
  return original
  
  