
with open("input.txt", 'r+') as inputFile:

    # Part I
    countSafe = 0

    for line in inputFile:
        separatedLine   = line.split()
        isSafe          = True
        problemDampener = 1
        direction       = 0 #0 up, 1 down

        for index in range(1, len( separatedLine )): 
            difference = int(separatedLine[index-1]) - int(separatedLine[index])
            if (index == 1):
                if difference > 0:
                    #decreasing
                    direction = 1
                elif difference < 0:
                    #increasing
                    direction = 0
                else:
                    isSafe = False
                    break

            if ( direction == 1 and (difference >  3 or difference <  1) ) or \
            ( direction == 0 and (difference < -3 or difference > -1)):
                    isSafe = False
                    break
        
        if isSafe == True:
            countSafe += 1

    print (countSafe)


    # Part II

    inputFile.seek(0)
    countSafeWDampener = 0

    for line in inputFile:
        separatedLine   = line.split()
        problemDampener = 1
        direction       = 0 #0 up, 1 down
        numFloors       = len( separatedLine )
        isSafeWDampener = False

        for skipFloor in range(-1, numFloors ): 
            isSafe          = True
            firstCheck      = True

            for index in range(1, numFloors ):

                if skipFloor == index - 1:
                    continue

                if skipFloor + 1 == numFloors and index == numFloors - 1:
                    continue

                floor1Pos = index - 1
                floor2Pos = index + 1 if skipFloor == index else index

                difference = int(separatedLine[floor1Pos]) - int(separatedLine[floor2Pos])

                if ( firstCheck ):
                    if difference > 0:
                        #decreasing
                        direction = 1
                    elif difference < 0:
                        #increasing
                        direction = 0
                    else:
                        isSafe = False
                        break
                    firstCheck = False

                if ( direction == 1 and (difference > 3 or difference < 1) ) or ( direction == 0 and (difference < -3 or difference > -1)):
                        isSafe = False
                        break
            if ( isSafe == True ):      
                isSafeWDampener = True
                
        if isSafeWDampener == True:
            countSafeWDampener +=1
            continue

    print (countSafeWDampener)    

inputFile.close()