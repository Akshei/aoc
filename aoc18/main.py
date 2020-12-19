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

def changeEquation(equation):
    new_equation = equation.replace("(", "( ")
    new_equation = new_equation.replace(")", " )")
    return new_equation.split(" ")


def makeONPFromChangedEquation(changedEquation):
    wyjscie = list()
    stos = list()
    for char in changedEquation:
        if char.isdigit():
            wyjscie.append(char)
        elif char == '(':
            stos.append(char)
        elif char == ')':
            ch = stos.pop(-1)
            while ch != '(':
                wyjscie.append(ch)
                ch = stos.pop(-1)
        else:
            stos.append(char)
    result = wyjscie + stos
    return result


def calculateONPValue(onp):
    stos = list()
    for char in onp:
        if char.isdigit():
            stos.append(char)
        else:
            a = stos.pop(-1)
            b = stos.pop(-1)
            x = eval(b + char + a)
            stos.append(str(x))
    return stos[0]


def calculateValue(changedEquation):
    value = changedEquation[0]


def calculateValueFrom(equation):
    changedEquation = changeEquation(equation)
    # onp = makeONPFromChangedEquation(changedEquation)
    # result = calculateONPValue(onp)
    result = calculateValue(changedEquation)
    return result


rownania = loadFile()
results = list()
for r in rownania:
    results.append(calculateValueFrom(r))
a = 123