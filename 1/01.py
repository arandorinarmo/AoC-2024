inputFile = open("input.txt", "rt")

list1 = []
list2 = []

for line in inputFile:
    separatedLine = line.split()
    list1.append(int(separatedLine[0]))
    list2.append(int(separatedLine[1]))
inputFile.close()

list1.sort()
list2.sort()

sumDistance     = 0
similarityScore = 0

for i in range(len(list1)):
    sumDistance     += abs( list1[i] - list2[i])
    similarityScore += list1[i] * list2.count(list1[i])

print (sumDistance)
print (similarityScore)
