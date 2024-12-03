import re

#Pt1
pattern = re.compile("mul\((\d*),(\d*)\)")

sum = 0
   
for i, line in enumerate(open('3\input.txt')):
    for match in re.finditer(pattern, line):
        sum += int(match.group(1)) * int(match.group(2))

print (sum)


#Pt2

pattern = re.compile("do\(\)|don\'t\(\)|mul\((\d*),(\d*)\)")

sum = 0
instruction = True
   
for i, line in enumerate(open('3\input.txt')):
    for match in re.finditer(pattern, line):
        if ( match.group() == "don't()" ):
            instruction = False
        elif ( match.group() == "do()"):
            instruction = True
        elif  ( instruction == True ):
            sum += int(match.group(1)) * int(match.group(2))
print (sum)