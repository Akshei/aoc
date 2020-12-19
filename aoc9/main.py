import copy

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

def getNumbers(index,actualNumber, numbersList, actualNumbersAdded ):
    if index in actualNumbersAdded:
        return False,actualNumbersAdded
    actualNumber -= numbersList[index][1]
    if actualNumber < 0:
        return False,actualNumbersAdded
    actualNumbersAdded.append(index)
    if actualNumber == 0:
        return True,actualNumbersAdded
    numbersList[index] = (True,numbersList[index][1])
    number = index + 1
    if numbersList[number][0] == False:
        result = getNumbers(index=number, numbersList=numbersList,actualNumbersAdded= actualNumbersAdded,actualNumber=actualNumber)
        if result[0] is True:
            return result
    numbersList[index] = (False, numbersList[index][1])
    actualNumbersAdded.pop()
    return False,actualNumbersAdded

numbers = loadFile()
numbers = [(False,int(x)) for x in numbers]
preambleSize = 25
number_we_are_looking_for = 1398413738
number_we_are_looking_for1 = 127
res = None
for i in range(len(numbers)):
    result = getNumbers(index=i, numbersList=numbers,actualNumbersAdded= [],actualNumber=number_we_are_looking_for)
    if result[0] is True and len(result[1]) != 1:
        print (result)
        res = result
kromka = list()
for i in res[1]:
    kromka.append(numbers[i][1])
minimum = min(kromka)
maximum = max(kromka)
print(minimum + maximum , minimum,maximum)