# conway's game of life

import random, time, copy, sys
WIDTH = 60
HEIGHT = 20

# create a list of lists for all the cells
nextCells = []
for x in range(WIDTH):
    column = []         # create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')          # append a living cell
        else:
            column.append(' ')
    nextCells.append(column)

loopCounter = 0     # we will run this (X) times only. There seems no way to interrupt this on
                    # an iPad

while True:
    print("loop: {:>4d}\n".format(loopCounter))
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1

            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '

    time.sleep(1)
    loopCounter += 1
    if loopCounter > 20:
        sys.exit(0)

