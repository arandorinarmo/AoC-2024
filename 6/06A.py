'''
    1
 8     2
    4 
'''

def printMap(map):
    for row in map:
        print(*row)
    print('\n')

guardDirections = ['^', '>', 'v', '<']
guardMovementY  = [-1, 0, 1,  0]
guardMovementX  = [ 0, 1, 0, -1]
map = []
mapDimensions = (0,0)
guardPos = (0,0)

with open('test.txt', "r") as file:
    posY = 0
    for row in file.readlines():
        posX = 0
        maprow = []
        for char in row:
            if char in guardDirections:
                maprow.append(char)
                guardPos = (posY, posX)
            elif(char != '\n'):
                maprow.append(char)
            posX += 1
        map.append (maprow)
        posY += 1
file.close()

#guardCircleClosed = False
mapDimensions = (len(map), len(map[0]))


guardLeft = False
while guardLeft == False:
    guardDirection = guardDirections.index( map[guardPos[0]][guardPos[1]] )

    for cntDrs in range(0,4):
        newPlannedPosY = guardPos[0] + guardMovementY[guardDirection]
        newPlannedPosX = guardPos[1] + guardMovementX[guardDirection]

        if newPlannedPosY not in range(0, mapDimensions[0] ) or \
           newPlannedPosX not in range(0, mapDimensions[1] ):
            # Guard left the area
            map[guardPos[0]][guardPos[1]] = guardDirection
            guardLeft = True

            #printMap(map)
            break

        if ( map[newPlannedPosY][newPlannedPosX] != "#" ):
            map[guardPos[0]][guardPos[1]] = guardDirection
            guardPos = (newPlannedPosY, newPlannedPosX)
            map[guardPos[0]][guardPos[1]] = guardDirections[guardDirection]

            break
        else:
            guardDirection = guardDirection + 1 if guardDirection != 3 else 0
            
stepCount = 0
for row in map:
    for step in row:
        stepCount += 1 if step in {0,1,2,3} else 0
print (stepCount)
