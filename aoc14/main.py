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
mask = "000000000000000000000000000000000000"
memory = dict()


def setBitmask(maskStr, addressStr, value, memoryDict):
    addressStr = str(bin(int(addressStr)))[2:]
    addressStr = "000000000000000000000000000000000000"[:-len(addressStr)] + addressStr
    addresses = [addressStr]
    for charIndex in range(len(maskStr)):
        if maskStr[charIndex] == '1':
            for addressIndex in range(len(addresses)):
                addresses[addressIndex] = addresses[addressIndex][:charIndex] + '1' + addresses[addressIndex][charIndex + 1:]
        elif maskStr[charIndex] == 'X':
            tempList = list()
            for addressIndex in range(len(addresses)):
                tempList.append(addresses[addressIndex][:charIndex] + '1' + addresses[addressIndex][charIndex + 1:])
                tempList.append(addresses[addressIndex][:charIndex] + '0' + addresses[addressIndex][charIndex + 1:])
            addresses = tempList
    for address in addresses:
        memoryDict[int(address,2)] = value
    return memoryDict

for inst in instructions:
    if 'mask' in inst:
        mask = inst[7:]
    elif 'mem' in inst:
        startIndex = inst.index('[')+1
        endIndex = inst.index(']')
        numb = inst[startIndex:endIndex]
        value = int(inst[inst.index('=') + 2:])
        memory = setBitmask(maskStr=mask, addressStr=numb, value=value, memoryDict = memory)
    else:
        print("cos jeblo", inst)
amount = 0
for i in memory.values():
    amount += i
print(amount)

#part 1
# def setBitmask(number, mask):
#     number = str(bin(int(number)))[2:]
#     number = "000000000000000000000000000000000000"[:-len(number)] + number
#     for i in range(len(mask)):
#         if mask[i] == 'X':
#             continue
#         number = number[:i] + mask[i] + number [i+1:]
#     return int(number, 2)
#
# instructions = loadFile()
# mask = "000000000000000000000000000000000000"
# memory = dict()
# for inst in instructions:
#     if 'mask' in inst:
#         mask = inst[7:]
#     elif 'mem' in inst:
#         startIndex = inst.index('[')+1
#         endIndex = inst.index(']')
#         numb = int(inst[startIndex:endIndex])
#         memory[numb] = setBitmask(inst[inst.index('=') + 2:],mask)
#     else:
#         print("cos jeblo", inst)
#
# amount = 0
# for i in memory.values():
#     amount += i
# print(amount)
a = 123