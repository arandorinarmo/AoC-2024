import math

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

with open('input.txt', "r") as file:

    total = 0
    for row in file.readlines():
        equation = row.split(":")
        result = int(equation[0])
        items = equation[1].split()

        bit = 0

        for i in range (0, int(math.pow(3,len(items)-1))):      
            checkSum = int(items[0])

            opList = numberToBase(i,3)
            for ctr in range (len(opList), len(items)-1):
                opList.insert(0,0)
            
            for j in range (1,len(items)):
                if opList[j-1] == 0:
                    checkSum += int(items[j])
                if opList[j-1] == 1:
                    checkSum = checkSum * int(items[j])
                if opList[j-1] == 2:
                    tempSum = str(checkSum) + str(items[j]) 
                    checkSum = int( tempSum )
            
            if (result == checkSum):
                total += checkSum
                break

            bit += 1
    print (total)