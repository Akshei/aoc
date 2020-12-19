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

instructionsOrig = loadFile()



def makeCommand(instruction, accumulator, instructionNo):
    instruction = instruction.split(" ")
    if instruction[0] == "nop":
        instructionNo += 1
    elif instruction[0] == "acc":
        accumulator += int(instruction[1])
        instructionNo += 1
    elif instruction[0] == "jmp":
        instructionNo += int(instruction[1])
    return accumulator, instructionNo
accumulator = 0
for insNo in range(len(instructionsOrig)):
    accumulator = 0
    instructionNo = 0
    instructionsDone = set()
    instructions = copy.deepcopy(instructionsOrig)
    if "jmp" in instructions[insNo]:
        instructions[insNo] = "nop" + instructions[insNo][3:]
    elif "nop" in instructions[insNo]:
        instructions[insNo] = "jmp" + instructions[insNo][3:]
    else:
        continue
    while instructionNo not in instructionsDone:
        instructionsDone.add(instructionNo)
        accumulator, instructionNo = makeCommand(instructions[instructionNo], accumulator, instructionNo)
        if instructionNo == len(instructions):
            print(accumulator)