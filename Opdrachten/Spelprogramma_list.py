from random import randint

gameList = ['Monoply','Yathzee','Bridge','Poker','Pesten','Mens erger je niet','Cluedo']

def gameProgram():
    minOrMax = input("-------------------------------\nMinimum or Maximum? (Min/Max)\n-------------------------------\n").lower()
    if minOrMax == "min":
        minOrMax = 4
    else:
        minOrMax = 11
    for i in range(minOrMax):
        print(gameList[randint(0,len(gameList)-1)])
    gameProgram()

gameProgram()