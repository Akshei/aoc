def loadFile(isInt = False):
    file = open('abc', 'r')
    passList = [x for x in file]
    for i in range(len(passList)):
        if passList[i][-1] == "\n":
            passList[i] = passList[i][:-1]
    if isInt:
        passList = [int(x) for x in passList]
    return passList

def printAll(listOfStrings):
    for i in listOfStrings:
        print([i])

def getAmount(curJolt, connectors, currentAmount):
    if curJolt == connectors[-1]:
        return currentAmount + 1
    conn = [x for x in connectors if curJolt < x < curJolt + 4]
    for co in conn:
        currentAmount = getAmount(co, connectors, currentAmount)
    return currentAmount

def splitConnectors(connectors):
    result = list()
    temp = list()
    for i,j in zip(connectors,connectors[1:]):
        temp.append(i)
        if j-i == 3:
            result.append(temp)
            temp = list()
    return result


jolts = dict()
jolts[1] = 0
jolts[2] = 0
jolts[3] = 0

connectors = loadFile(True)
connectors.append(0)
connectors.sort()
connectors.append(connectors[-1] + 3)
# for connector1,connector2 in zip(connectors,connectors[1:]):
#     jolts [connector2 - connector1] += 1
#
# print(jolts[1] * jolts[3])
connector1 = splitConnectors(connectors)
printAll(connector1)
amount = 1
for cn in connector1:
    amount  = amount * getAmount(cn[0],cn,0)
print(amount)

a = 123