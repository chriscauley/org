import sys
import re

if len(sys.argv) ==1:
  print """Usage:
python iconmoon.py [input-file] [class-name] [font-family] > [output-file]"""

f = open(sys.argv[1],'r')
lines = f.readlines()
f.close()

pattern = r'^([\w\d]+ ?\-?[\w\d]+)\s+(\S+)\s+content: \'.+\'\;$'
matches = [re.findall(pattern,line) for line in lines]
pattern2 = r'^([\w\d]+ ?\-?[\w\d]+)\s+content:'
space = [re.findall(pattern2,line) for line in lines]
space = [l for l in space if l]
print ".%s { font-family:\"%s\"; }"%(sys.argv[2],sys.argv[3])
classes = {}
for match in matches:
  if not match: continue
  t = (sys.argv[2],match[0][0].replace(" ","-").lower(),match[0][1].replace("\\","\\\\"))
  print ".%s.%s::after { content: \"%s\"; }"%t
print ".%s.%s::after { content: \"%s\"; }"%(sys.argv[2],space[0][0].lower().replace(" ","-"),' ')
