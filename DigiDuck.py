#!/usr/bin/python

from sys import version_info

py3 = version_info[0] > 2 #creates boolean value for test that Python major version > 2

if py3:
   command = input("Enter command to execute: ")
else:
   command = raw_input("Enter command to execute: ")

# Convert to EN Keyboard Layout

i=0

text = list(command)
while i < len(text):
   if text[i] == "-":
      text[i] = "/"
   elif text[i] == "(":
      text[i] = "*"
   elif text[i] == ")":
      text[i] = "("
   elif text[i] == "'":
      text[i] = "-"
   elif text[i] == ":":
      text[i] = ">"
   elif text[i] == "/":
      text[i] = "&"
   elif text[i] == ";":
      text[i] = "<"
   i += 1
cmd = ''.join(text)

# Read in the file
filedata = None
with open('Template.ino', 'r') as file :
   filedata = file.read()

# Replace the target string
filedata = filedata.replace('CMD', cmd)

# Write the file out again
try:
   with open('Attack.ino', 'w') as file:
     file.write(filedata)
   print "Attack.ino file created successfully!"
except:
   print "Error detected!"
