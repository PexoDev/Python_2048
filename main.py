import GameManager
from os import system
import random
from Block import Block

map = []
freeSpots = []
isGameOver = False

def clearMap():
    for i in range(4):
        m = []
        for j in range(4):
            m.append(None)
            freeSpots.append((i, j))
        map.append(m)


def generateBlocks(count):
        for i in range(count):
            block = Block();
            rand = random.randint(0,len(freeSpots)-1)
            spot = freeSpots[rand]
            map[spot[0]][spot[1]] = block
            freeSpots.remove(spot);

def move():
    def MoveBlocksProcess(i,j, direction):
        if map[i][j] is not None:
            if i + direction[0] > 3: return
            if j + direction[1] > 3: return
            if i + direction[0] < 0: return
            if j + direction[1] < 0: return

            nextI = i + direction[0]
            nextJ = j + direction[1]
            if (map[nextI][nextJ] is None):
                map[nextI][nextJ] = map[i][j]
                freeSpots.remove((nextI, nextJ))
                map[i][j] = None
                freeSpots.append((i, j))
            else:
                if map[nextI][nextJ].value == map[i][j].value:
                    map[nextI][nextJ].Stack(map[i][j])
                    map[i][j] = None
                    freeSpots.append((i, j))
                else:
                    return

    def MoveVertically(i,direction):
        if direction[1] >= 0:
            for j in range(len(map[i])):
                MoveBlocksProcess(i, j, direction)
        else:
            for j in range(len(map[i]) - 1, -1, -1):
                MoveBlocksProcess(i, j, direction)

    def MoveBlocks(direction):
        if direction[0] >= 0:
            for i in range(len(map)):
                MoveVertically(i,direction)
        else:
            for i in range(len(map)-1,-1,-1):
                MoveVertically(i,direction)

    userInput = input()
    if userInput == 'd': MoveBlocks([0, 1])
    if userInput == 'a': MoveBlocks([0, -1])
    if userInput == 'w': MoveBlocks([-1, 0])
    if userInput == 's': MoveBlocks([1, 0])

def render():
    system('mode con: cols=100 lines=40')
    system("cls")
    for i in range(len(map)):
        for j in range(len(map[i])):
            if(map[i][j] is not None):
                print("["+str(map[i][j].value)+"]", end='')
            else:
                print ("[ ]", end='')
        print("\n", end='')
clearMap()
generateBlocks(2)
while not isGameOver:
    render()
    move()
    generateBlocks(1)
    if len(freeSpots) <= 0:
        isGameOver = True

print("GAME OVER! \n Your score: " + GameManager.Score)
input();