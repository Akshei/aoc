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

def expandA(map):
    addDimensionZero, addDimensionNPlusOne = False, False
    for layer in map[0]:
        for row in layer:
            for cell in row:
                if cell == "#":
                    addDimensionZero = True
    for layer in map[-1]:
        for row in layer:
            for cell in row:
                if cell == "#":
                    addDimensionNPlusOne = True
    if addDimensionZero is True:
        newdim = copy.deepcopy(map[0])
        for layer in newdim:
            for row in layer:
                for cellIndex in range(len(row)):
                    row[cellIndex] = "."
        map.insert(0,newdim)
    if addDimensionNPlusOne is True:
        newdim = copy.deepcopy(map[0])
        for layer in newdim:
            for row in layer:
                for cellIndex in range(len(row)):
                    row[cellIndex] = "."
        map.append(newdim)

    return map

def expandZ(map,x,y):
    addLayerEnd, addLayerFirst = False, False
    for dimension in map:
        for row in dimension[-1]:
            for cell in row:
                if cell == "#":
                    addLayerEnd = True
        for row in dimension[0]:
            for cell in row:
                if cell == "#":
                    addLayerFirst = True
    if addLayerEnd is True:
        for dimension in map:
            newLayer = copy.deepcopy(map[0][0])
            for row in newLayer:
                for cellIndex in range(len(row)):
                    row[cellIndex] = "."

            dimension.append(newLayer)
    if addLayerFirst is True:
        for dimension in map:
            newLayer = copy.deepcopy(map[0][0])
            for row in newLayer:
                for cellIndex in range(len(row)):
                    row[cellIndex] = "."
            dimension.insert(0,newLayer)
    return map

def expandY(map,x,y):
    addTop = False
    addBot = False
    for dimension in map:
        for layer in dimension:
            for cell in layer[0]:
                if cell == '#':
                    addTop = True
            for cell in layer[-1]:
                if cell == '#':
                    addBot = True
    if addTop is True:
        y += 1
        for dimension in map:
            for layer in dimension:
                layer.insert(0, list('.' * x))
    if addBot is True:
        y += 1
        for dimension in map:
            for layer in dimension:
                layer.append(list('.' * x))
    return map,y

def expandX(map,x):
    addBeginning, addEnd = False, False
    for dimension in map:
        for layer in dimension:
            for row in layer:
                if row[0] == '#':
                    addBeginning = True
                if row[-1] == '#':
                    addEnd = True
    if addBeginning is True:
        x += 1
        for dimension in map:
            for layer in dimension:
                for i in range(len(layer)):
                    layer[i] = ['.'] + layer[i]
    if addEnd is True:
        x += 1
        for dimension in map:
            for layer in dimension:
                for i in range(len(layer)):
                    layer[i] = layer[i] + ['.']
    return map,x

def expandMap(map,x,y):
    map = expandA(map)
    map = expandZ(map,x,y)
    map, y = expandY(map,x,y)
    map,x = expandX(map,x)
    return map,x,y


def countNieghboursOnRow(row, cellIndex):
    neighboursAmount = 0
    for cellOffset in range(-1, 2):
        cellNumber = cellOffset + cellIndex
        if not (cellNumber < 0 or cellNumber >= len(row)):
            if row[cellNumber] == '#':
                neighboursAmount += 1
    return neighboursAmount


def countNieghboursOnLayer(layer, rowindex, cellIndex):
    neighboursAmount = 0
    for rowOffset in range(-1, 2):
        rowNumber = rowOffset + rowindex
        if not (rowNumber < 0 or rowNumber >= len(layer)):
            neighboursAmount += countNieghboursOnRow(layer[rowNumber], cellIndex)
    return neighboursAmount

def countNeighboursOnDimension(dimension, layerIndex, rowIndex, cellIndex):
    neighboursAmount = 0
    for layerOffset in range(-1, 2):
        layerNumber = layerIndex + layerOffset
        if not (layerNumber < 0 or layerNumber >= len(dimension)):
            neighboursAmount += countNieghboursOnLayer(dimension[layerNumber], rowIndex, cellIndex)
    return neighboursAmount


def countNeighbours(map,dimensionIndex, layerIndex, rowindex, cellIndex):
    neighboursAmount = 0
    for dimensionOffset in range(-1, 2):
        dimensionNumber = dimensionIndex + dimensionOffset
        if not (dimensionNumber < 0 or dimensionNumber >= len(map)):
            neighboursAmount += countNeighboursOnDimension(map[dimensionNumber], layerIndex, rowindex, cellIndex)
    return neighboursAmount


def makeNewMap(map):
    newmap = copy.deepcopy(map)

    for dimensionIndex in range(len(map)):
        for layerIndex in range(len(map[dimensionIndex])):
            for rowindex in range(len(map[dimensionIndex][layerIndex])):
                for cellIndex in range(len(map[dimensionIndex][layerIndex][rowindex])):
                    neighboursAmount = countNeighbours(map,dimensionIndex, layerIndex, rowindex, cellIndex)
                    if map[dimensionIndex][layerIndex][rowindex][cellIndex] == '#' and neighboursAmount in [3,4]:
                        newmap[dimensionIndex][layerIndex][rowindex][cellIndex] = '#'
                    elif map[dimensionIndex][layerIndex][rowindex][cellIndex] == '.' and neighboursAmount in [3]:
                        newmap[dimensionIndex][layerIndex][rowindex][cellIndex] = '#'
                    else:
                        newmap[dimensionIndex][layerIndex][rowindex][cellIndex] = '.'
    return newmap

def countAllActives(map):
    activeAmount = 0
    for dimension in map:
        for layer in dimension:
            for row in layer:
                for cell in row:
                    if cell == '#':
                        activeAmount +=1
    return activeAmount


map = loadFile()
map2 = list()
for i in map:
    map2.append(list(i))
map = [[map2]]
print('start', countAllActives(map))
x = len(map[0][0])
y = len(map[0])
turn = 0
while turn < 6:
    turn += 1
    print('round',turn -1,countAllActives(map))
    printAll(map)
    map,x,y = expandMap(map,x,y)
    map = makeNewMap(map)





amount = countAllActives(map)
print("end", amount)
a = 123