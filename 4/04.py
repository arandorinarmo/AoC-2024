
'''
recursive funcion for walking the word in each direction
directions:
 8  1  2
 7     3
 6  5  4
'''

def readWordFrom(i,j):
    cntWords = 0

    for nextDir in range(1,9):
        
        moveH = 0
        moveV = 0

        if (nextDir == 8 or nextDir == 1 or nextDir == 2):
            moveV = -1
        if (nextDir == 8 or nextDir == 7 or nextDir == 6):
            moveH = -1
        if (nextDir == 2 or nextDir == 3 or nextDir == 4):
            moveH = 1
        if  (nextDir == 6 or nextDir == 5 or nextDir == 4):
            moveV = 1

        if ((nextDir == 8 or nextDir == 1 or nextDir == 2) and i < 3 ) or \
           ((nextDir == 8 or nextDir == 7 or nextDir == 6) and j < 3 ) or \
           ((nextDir == 2 or nextDir == 3 or nextDir == 4) and j > inputWidth - 4 ) or \
           ((nextDir == 6 or nextDir == 5 or nextDir == 4) and i > inputHeight -4 ):
            continue

        if  wordList[i+moveV]  [j+moveH]   == "M" and \
            wordList[i+moveV*2][j+moveH*2] == "A" and \
            wordList[i+moveV*3][j+moveH*3] == "S":
            cntWords += 1
        
    return cntWords    
            
''' global variables '''

wordList = []


''' main '''

with open('4\input.txt', "r") as file:
    for line in file.readlines():
        wordList.append(line)


inputHeight = len(wordList)
inputWidth = len(wordList[0]) - 1

wordCountXMAS  = 0
wordCountX_MAS = 0

# iterate trough any word starting point
for i in range(0,inputHeight):
    for j in range(0,inputWidth):
        #Itarate trough ever possible location
        if ( wordList[i][j] == "X" ):
            wordCountXMAS += readWordFrom(i,j)

        if i >= 1 and i < inputHeight - 1 and j >= 1 and j < inputWidth - 1:
            if ( wordList[i][j] == "A" ):
                if wordList[i-1][j-1] == "M" and \
                   wordList[i-1][j+1] == "M" and \
                   wordList[i+1][j-1] == "S" and \
                   wordList[i+1][j+1] == "S":
                    wordCountX_MAS += 1

                if wordList[i-1][j-1] == "M" and \
                   wordList[i-1][j+1] == "S" and \
                   wordList[i+1][j-1] == "M" and \
                   wordList[i+1][j+1] == "S":
                    wordCountX_MAS += 1

                if wordList[i-1][j-1] == "S" and \
                   wordList[i-1][j+1] == "M" and \
                   wordList[i+1][j-1] == "S" and \
                   wordList[i+1][j+1] == "M":
                    wordCountX_MAS += 1

                if wordList[i-1][j-1] == "S" and \
                   wordList[i-1][j+1] == "S" and \
                   wordList[i+1][j-1] == "M" and \
                   wordList[i+1][j+1] == "M":                    
                    wordCountX_MAS += 1

print (wordCountXMAS)
print (wordCountX_MAS)
file.close()

