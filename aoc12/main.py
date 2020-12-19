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

instructions = loadFile()
instructions = [(x[0],int(x[1:])) for x in instructions]
x,y = 10,1
ship_x, ship_y = 0,0
curDirect = 1
directions = {0:(0,1), 1:(1,0),2:(0,-1),3:(-1,0)}
directions = {0:(0,1), 1:(1,0),2:(0,-1),3:(-1,0)}
for i in range(len(instructions)):
    if instructions[i][0] == 'F':

        ship_x += x * instructions[i][1]
        ship_y += y * instructions[i][1]
    if instructions[i][0] == 'N':
        x += directions[0][0] * instructions[i][1]
        y += directions[0][1] * instructions[i][1]
    if instructions[i][0] == 'E':
        x += directions[1][0] * instructions[i][1]
        y += directions[1][1] * instructions[i][1]
    if instructions[i][0] == 'S':
        x += directions[2][0] * instructions[i][1]
        y += directions[2][1] * instructions[i][1]
    if instructions[i][0] == 'W':
        x += directions[3][0] * instructions[i][1]
        y += directions[3][1] * instructions[i][1]
    if instructions[i][0] == 'R':
        temp_x = 0
        temp_y = 0
        if (instructions[i][1]/90) == 1:
            temp_x = y
            temp_y = -x
        if (instructions[i][1]/90) == 2:
            temp_x = -x
            temp_y = -y
        if (instructions[i][1]/90) == 3:
            temp_x = -y
            temp_y = x
        x = temp_x
        y = temp_y
    if instructions[i][0] == 'L':
        cur = (4 - (instructions[i][1] / 90))
        temp_x = 0
        temp_y = 0
        if cur == 1:
            temp_x = y
            temp_y = -x
        if cur == 2:
            temp_x = -x
            temp_y = -y
        if cur == 3:
            temp_x = -y
            temp_y = x
        x = temp_x
        y = temp_y

print(abs(ship_x) + abs(ship_y))
