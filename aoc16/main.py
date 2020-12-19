import copy, math
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

inst = loadFile()


def makeThisThing(inst):
    spaceAmount = 0
    specs = dict()
    myTicket = "kromka"
    nearbyTickets = list()
    for line in inst:
        if line == '':
            spaceAmount += 1
            continue
        splitted = line.split(' ')
        if spaceAmount == 0:
            specs[line[:line.index(':')]] =list()
            for i in range(len(splitted) -3,len(splitted),2):
                minimum, maximum = splitted[i][:splitted[i].index('-')],splitted[i][splitted[i].index('-') + 1 :]
                specs[line[:line.index(':')]].append((int(minimum),int(maximum)))
        elif spaceAmount == 1:
            if "your" in line:
                continue
            myTicket = [int(x) for x in line.split(',')]
        else:
            if "nearby" in line:
                continue
            nearbyTickets.append([int(x) for x in line.split(',')])
    return specs, myTicket, nearbyTickets


specs,myTicket,nearbyTickets = makeThisThing(inst)
rejectedTicketNumbers = list()


def checkTicketWithSpecs(ticketNumber, specs):
    numberPassed = False
    for specsList in specs.values():
        for spec in specsList:
            if spec[0] <= ticketNumber <= spec[1]:
                numberPassed = True
    return numberPassed


goodTickets = [myTicket]
ticktApproved = True
for ticket in nearbyTickets:
    ticktApproved = True
    for ticketNumber in ticket:
        ticketPass = checkTicketWithSpecs(ticketNumber,specs)
        if ticketPass is False:
            ticktApproved = False
            rejectedTicketNumbers.append(ticketNumber)
    if ticktApproved is True:
        goodTickets.append(ticket)


def trySpecs(specs, goodTickets):
    specsNumber = dict()
    specsNames = [specName for specName in specs.keys()]
    resultSpecsNumber = dict()
    for i in range(len(goodTickets[0])):
        specsNumber[i] = [specName for specName in specs.keys()]
    for ticket in goodTickets:
        for i in range(len(ticket)):
            for spec in specsNames:
                if not (specs[spec][0][0] <= ticket[i] <= specs[spec][0][1] or specs[spec][1][0] <= ticket[i] <= specs[spec][1][1]):
                    if spec in specsNumber[i]:
                        specsNumber[i].pop(specsNumber[i].index(spec))

    change = True
    while change is True:
        change = False
        for key in specsNumber.keys():
            if len(specsNumber[key]) == 1:
                nameOfField = specsNumber[key].pop(0)
                resultSpecsNumber[key] = nameOfField
                change = True
                for key2 in specsNumber.keys():
                    if nameOfField in specsNumber[key2]:
                        specsNumber[key2].pop(specsNumber[key2].index(nameOfField))

    return resultSpecsNumber



specsNumber = trySpecs(specs, goodTickets)
amount = 0
for n in rejectedTicketNumbers:
    amount += n
print("rejected tickets numbers:",amount)
amount = 1
for key in specsNumber.keys():
    if 'departure' in specsNumber[key]:
        amount *= myTicket[key]
print("departures multiply is: ", amount)
a = 123