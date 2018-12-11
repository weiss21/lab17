#Lab 17
#Lab Problem for Today:
#Start with the Green Eggs and Ham word count lab.  
#In this lab, you printed to the screen a list of every word in Green Eggs and Ham and how often it appeared. For today's lab, 
#(1) First, modify your Green Eggs and Ham lab so that instead of printing the words and counts to the screen, it writes them out to an .html file.  
#You should be able to open your html file in a browser to see the results of your word count
#(2) Now, instead of printing the counts for each word, modify the color/size/weight of the word to reflect its frequency in the file.  
#You will probably want to break the counts into ranges for this (e.g. words with a count between 30 and 40 have one color/size, etc).  
#Here is a screen shot showing part of one potential outcome (be creative, this is by no means *the* answer, hopefully every group will have a different product for this lab)

import os


def read():
  #use os library to refer to filename
  directory = os.path.dirname(__file__)
  
  #Opens Green Eggs and Ham File. Reads it into text form. Then closes file.
  fileName = os.path.join(directory, 'eggs.txt')
  file = open(fileName,"r")
  original = file.read()
  file.close()
  
  textfiles = original.lower().replace("-"," ").split()
  uniqueWordCount = 0
  count = {}
  
  
  for word in textfiles:
   if word in count:
     count[word] += 1
   else:
     count[word] = 1
   
  final = sorted(count.iteritems(), key = lambda x: x[1], reverse = True)
  
  #HTML document here
  write(final)
  
#(2) Now, instead of printing the counts for each word, modify the color/size/weight of the word to reflect its frequency in the file.  You will probably want to break the counts into ranges for this 
#(e.g. words with a count between 30 and 40 have one color/size, etc).    

def sizecolor(count):
  if count >= 0 and count <= 10:
       return ('663399', '20')
  elif count > 10 and count <= 20:
       return ('FFFF00', '50')
  elif count > 20 and count <= 30:
       return ('66CC33', '30')
  elif count > 30 and count <= 40:
       return ('00CC00', '80')
  elif count > 40 and count <= 50:
       return ('3399FF', '450')
  else: 
       return ('CCCCFFF', '40')
        
def write(words):
   directory = os.path.dirname(__file__)
   fileName = os.path.join(directory, 'newegg.html')
   
   #setup the HTMLfile
   header = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transition//EN"\
     "http://www.w3.org/TR/html4/loose.dtd">'
   title = '<html>\n<head><title> Green Eggs and Ham </title>\n</head>'
   bodyOpen = '<body>\n<h1>Word Frequency</h1>\n'
   bodyClose = '</body>\n</html>'
   htmlBody = '<p style="color:#%s; font-size:%spx; font-weight:bold">%s</p><br>\n'

   
   #start writing the new file.
   f = open(fileName, 'w') 
  
   f.write(header)
   f.write(title)
   f.write(bodyOpen)
   f.write('Green Eggs and Ham Words:<br>')
   
   f.write(str(words[0]))
   f.write("Hello")
   f.write(bodyClose)
   f.close()
  
if __name__ == '__read__':
  read()     