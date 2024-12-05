from functools import cmp_to_key

def checkRulePairOn(pages, rule):
    rule1 = int(rule[0])
    rule2 = int(rule[1])

    indexPage1 = pages.index( rule1 ) if rule1 in pages else -1
    indexPage2 = pages.index( rule2 ) if rule2 in pages else -1

    if (indexPage1 == -1 or indexPage2 == -1):
        return True
    else:
        return indexPage1 < indexPage2


def orderRuleSet2(ruleSet):
    uniqueNumbers = []

    for item in ruleSet:
        if item[0] not in uniqueNumbers:
            uniqueNumbers.append(item[0])

        if item[1] not in uniqueNumbers:
            uniqueNumbers.append(item[1])   

    for uniqueNumber in uniqueNumbers:
        smallerNumbers = []
        biggerNumbers = []

        for item in ruleSet:
            if uniqueNumber == item[0]:
                biggerNumbers.append(item[1])

            if uniqueNumber == item[1]:
                smallerNumbers.append(item[0])    

        numberStat.append( [uniqueNumber, smallerNumbers, biggerNumbers] ) 

def compare(num1, num2):
    for num in numberStat:
        if num[0] == num1:
            if num2 in num[1]:
                return 1
            elif num2 in num[2]:
                return -1
            else:
                return 0

ruleSet     = []
pageSet     = []
readRuleSet = True
cnt = 0
numberStat = []

with open("input.txt", 'r+') as inputFile:
    for line in inputFile:
        cnt += 1
        if len(line) < 2:
            readRuleSet = False
        else:
            if (readRuleSet):
                numPair = line.strip().split("|")
                rule1 = int(numPair[0])
                rule2 = int(numPair[1])
                ruleSet.append ([rule1, rule2])                
            else:
                pages = line.strip().split(',')
                pagesInt = [int(item) for item in pages]
                pageSet.append ( pagesInt )

    sum = 0
    sumInvalid = 0

    orderRuleSet2(ruleSet)

    for pageLine in pageSet:
        isValidLine = True
        for ruleLine in ruleSet:
            if checkRulePairOn(pageLine, ruleLine) == False:
                isValidLine = False
                pageInvalid = sorted(pageLine, key=cmp_to_key(compare))
                sumInvalid += int(pageInvalid[ len(pageInvalid) // 2 ])
                break
        if ( isValidLine == True ):
            sum += int(pageLine[ len(pageLine) // 2 ])

    print (sum)
    print (sumInvalid)  
inputFile.close()