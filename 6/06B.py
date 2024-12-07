import sys
import os
import copy
import datetime

current = os.path.dirname(os.path.realpath(__file__))
parent  = os.path.dirname(current)
sys.path.append(parent)
from utils import util

'''
     2(0)
 7(3)    3(1)
     5(2)
'''
def printMap(map):
    for row in map:
        print(*row)
    print('\n')


scriptStart = datetime.datetime.now()
print("Script start: ", scriptStart)

guardStartingDirections = ['^', '>', 'v', '<']
guardDirectionPrimes    = [ 2,   3,   5,   7]
guardMovementY  = [-1, 0, 1,  0]
guardMovementX  = [ 0, 1, 0, -1]
map = []
mapOriginal = []
mapDimensions = (0,0)
guardVector = (0,0,0)
guardVectorOriginal = (0,0,0)

with open('input.txt', "r") as file:
    posY = 0
    for row in file.readlines():
        posX = 0
        maprow = []
        for char in row:
            if char in guardStartingDirections:
                maprow.append(".")
                guardVectorOriginal = (posY, posX, guardStartingDirections.index(char))
            elif(char != '\n'):
                maprow.append(char)
            posX += 1
        map.append (maprow)
        posY += 1
file.close()

mapDimensions = (len(map), len(map[0]))
mapOriginal = copy.deepcopy(map)

cntLoopScenarios = 0

curVar = 0
numVar = mapDimensions[0] * mapDimensions[1]

print 
for idxRows in range (0, mapDimensions[0]):
    for idxColumns in range (0, mapDimensions[1]):
        
        curVar = idxRows *  mapDimensions[0] + idxColumns + 1
        if idxRows == guardVectorOriginal[0] and idxColumns==guardVectorOriginal[1]:
            continue
        else:
            guardLeft = False
            guardLoop = False
            map[idxRows][idxColumns] = 'O'
            guardVector = guardVectorOriginal[:]
            
        while guardLeft == False and guardLoop == False:
            guardDirection = guardVector[2]

            #printMap(map)

            for cntDrs in range(0,4):
                newPlannedPosY = guardVector[0] + guardMovementY[guardDirection]
                newPlannedPosX = guardVector[1] + guardMovementX[guardDirection]
                plannedDirPrime= guardDirectionPrimes[guardDirection]

                if newPlannedPosY not in range(0, mapDimensions[0] ) or \
                newPlannedPosX not in range(0, mapDimensions[1] ):
                    # Guard left the area
                    map[guardVector[0]][guardVector[1]] = plannedDirPrime
                    guardLeft = True

                    #
                    break

                if ( map[newPlannedPosY][newPlannedPosX] not in ['#', 'O'] ):
                    plannedPosHistory = map[newPlannedPosY][newPlannedPosX]
                    currentPosHistory = map[guardVector[0]][guardVector[1]]

                    if (currentPosHistory != '.' and plannedDirPrime in util.primeFactors(int(currentPosHistory))) :
                        #Guard traversed the same direction, so started a loop
                        guardLoop = True
                        
                        break
                    else:
                        #Guard go on and marks its way                
                        if currentPosHistory == '.':
                            map[guardVector[0]][guardVector[1]] = plannedDirPrime
                        else:
                            map[guardVector[0]][guardVector[1]] = map[guardVector[0]][guardVector[1]] * plannedDirPrime                  
                        guardVector = (newPlannedPosY, newPlannedPosX, guardDirection)
                        break
                else:
                    guardDirection = guardDirection + 1 if guardDirection != 3 else 0

        map = copy.deepcopy(mapOriginal)
        cntLoopScenarios += 1 if guardLoop else 0

        curVar = idxRows *  mapDimensions[0] + idxColumns + 1
        util.refreshProgressBar(curVar,numVar,True)

print (cntLoopScenarios)
scriptEnd = datetime.datetime.now()
print("Script end: ", scriptStart, "\nExecution time: ", scriptEnd-scriptStart)
