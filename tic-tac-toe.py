import random

gameOn = True
values = ["   "]*10
winnerPositions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
playedPositions = []
p1 = ["Player1", "X"]
p2 = ['Player2', "O"]
roundNo = 0


def newgamestart():
    global gameOn
    clearValues()
    print(f"Game started! {p1[0]} uses {p1[1]}, {p2[0]} uses {p2[1]}")
    print("Enter zero to exit main menu during the game")
    while gameOn:
        drawboard()
        makeMove()
        if not gameOn:
            break
    print("Game Over!")


def checkIfWon(p):
    global gameOn
    won = False
    for i in winnerPositions:
        if not won:
            matches = 0
            matchLetter = " " + p[1] + " "
            for x in i:
                if values[x] == matchLetter:
                    matches += 1
                else:
                    break
            if matches == 3:
                drawboard()
                print(p[0] + " won!")
                gameOn = False


def whoIsPlaying():
    global roundNo
    if roundNo % 2 == 0:
        return p1
    else:
        return p2


def makeMove():
    playerMove = False
    global gameOn
    global roundNo
    p = whoIsPlaying()
    print(f"{p[0]} is playing with {p[1]} char")
    while not playerMove:
        movePosition = (input("Choose a cell to play -> "))
        if not movePosition.isdigit():
            print("Please enter a digit!")
            continue
        else:
            movePosition = int(movePosition)
            if movePosition == 0:
                print("exiting")
                gameOn = False
                break
            elif not movePosition in range(1, 10):
                print("Please enter a number between 1 and 9! -> ")
                continue
            elif movePosition in playedPositions:
                print("This position is already filled! Enter another position")
                continue
            else:
                move = p[1]
                values[movePosition] = " " + move + " "
                playedPositions.append(movePosition)
                roundNo += 1
                checkIfWon(p)
                if len(playedPositions) == 9 and gameOn == True:
                    print("No more empty cells! No winner!")
                    gameOn = False
                break


def clearValues():
    global playedPositions
    global values
    global roundNo
    for b in range(10):
        if b != 0:
            values[b] = "   "
    values = ["   "] * 10
    playedPositions = []
    roundNo=random.randint(0, 1)


def drawboard():
    text = "\n"
    for idx, b in enumerate(values):
        if idx != 0:
            newtext = "|" + " " + str(idx) + " "
            text += newtext
            if idx % 3 == 0:
                text += "|\n"
    print(text)

    text = "\n"
    for b in range(10):
        if b != 0:
            text += "|" + values[b]
            if b % 3 == 0:
                text += "|\n"
    print(text)


newGame = "Y"
print("Welcome to Tic Tac Toe game!")
while newGame == "Y":
    newGame = input("do you want to start a new game? Y or N -> ")
    if newGame == "Y":
        gameOn = True
        newgamestart()
    elif newGame == "N":
        print("Good bye!")
        break
