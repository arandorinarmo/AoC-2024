inputFile = open("input.txt", "rt")

countSafe = 0

for line in inputFile:
    separatedLine = line.split()
    isSafe = True
    problemDampener = 1
    direction = 0 #0 up, 1 down
    for index in range(1, len( separatedLine ) ): 
        difference = int(separatedLine[index-1]) - int(separatedLine[index])
        print (index, ': ', difference)
        if (index == 1):
            if difference > 0:
                #decreasing
                direction = 1
                print ("down(1)")
            elif difference < 0:
                #increasing
                direction = 0
                print ("up(0)")
            else:
                isSafe = False
                print ("same")
                break

        if ( direction == 1 and (difference > 3 or difference < 1) ) or ( direction == 0 and (difference < -3 or difference > -1)):
                isSafe = False
                break
    
    if isSafe == True:
        countSafe += 1

print (countSafe)
    
inputFile.close()