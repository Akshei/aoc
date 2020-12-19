def loadFile():
    file = open('abc', 'r')
    passList = [x for x in file]
    for i in range(len(passList)):
        if passList[i][-1] == "\n":
            passList[i] = passList[i][:-1]
    return passList

def printAll(listOfStrings):
    for i in listOfStrings:
        print([i])

def addDict(name, bagsDict):
    if name not in bagsDict:
        bagsDict[name] = Bag(name)

class Bag():
    def __init__(self, name):
        self.name = name
        self.bagWhoOwnsMe = list()
        self.bagIOwn = dict()

def getAmount(name,bagsDict):
    amount = 1
    for bagName in bagsDict[name].bagIOwn.keys():
        amount +=  bagsDict[name].bagIOwn[bagName] * getAmount(bagName, bagsDict)
    return amount

# faded aqua bags contain 2 drab white bags, 3 faded purple bags, 4 striped maroon bags.
# 0     1    2    3       4 5     6    7     8 9     10     11
bagsStrings = loadFile()
bags = dict()
for bagString in bagsStrings:
    splittedBag = bagString.split(" ")
    bag_name = splittedBag[0] + " " + splittedBag[1]
    bagsAmount = 0
    for i in splittedBag:
        if i.isdigit():
            bagsAmount += int(i)
    addDict(bag_name, bags)
    if "other bags" not in bagString:
        for i in range(4, len(splittedBag),4):
            upperBagName = splittedBag[i+1] + " " + splittedBag[i + 2]
            upperBagAmount = int(splittedBag[i])
            addDict(upperBagName, bags)
            bags[upperBagName].bagWhoOwnsMe.append((upperBagAmount,bags[bag_name]))
            bags[bag_name].bagIOwn[upperBagName] = upperBagAmount

amount = getAmount("shiny gold", bags) -1
abc = 0