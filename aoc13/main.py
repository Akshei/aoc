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

def findMult(mult, bus, index):
    i = 1
    while (mult * i + index) % bus != 0:
        i += 1
    return i * mult

def is_prime(n):
   if n <= 1:
      return False
   else:
      for i in range(2, n):
         # checking for factor
         if n % i == 0:
            # return False
            return False
      # returning True
   return True

instructions = loadFile()
time = int(instructions[0])
buses = list()
for i in range(len(instructions[1].split(','))):
    if instructions[1].split(',')[i].isdigit():
        y = int(instructions[1].split(',')[i])
        buses.append((i,y))

mult = buses[0][1]
time = mult
for bus in buses[1:]:
    while (time + bus[0]) % bus[1] != 0:
        time += mult
    mult *= bus[1]

print(time)
# mult = buses[0]
# # for i in range(1,len(buses)):
# #     if buses[i] == 'x':
# #         continue
# #     mult = findMult(mult, buses[i], i)
# # print(mult)


#
# multiplier = 0
# minutes = 0
# end = False
# nearEnd = 0
# while end is False:
#     time = multiplier * buses[0]
#     for bus in buses:
#         if bus == 'x':
#             minutes += 1
#             continue
#         if (minutes + time) % bus != 0:
#             break
#         minutes += 1
#     else:
#         print(time)
#         if nearEnd  == 10:
#             end = True
#         nearEnd += 1
#     multiplier += 1
#     minutes = 0
# print(time)



#part 1
# instructions = loadFile()
# time = int(instructions[0])
# buses = set([int(x) for x in instructions[1].split(',') if x!='x'])
# timewaitres = (max(buses),max(buses))
# for bus in buses:
#     timewait = bus - (time % bus)
#     if timewait < timewaitres[0]:
#         timewaitres = (timewait,bus)
# print (timewaitres[0] * timewaitres[1])
a = 123