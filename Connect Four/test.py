# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 07:42:10 2018

@author: Ryan Gamilo
"""

import sys 

def printGameBoard(gameBoard):
    for row in range(len(gameBoard)):
        print(gameBoard[row])

gameBoard = []
for row in range(0,6):
    gameBoard.append([])
    for col in range(7):
        gameBoard[row].append(" ")
printGameBoard(gameBoard)

turnCount = 0
while True:
    turnCount += 1
    playerStr = ""
    chips = ["1","2"]
    if turnCount % 2 != 0:
        playerStr = "P1, "
        chip = chips[0]
    else:
        playerStr = "P2, "
        chip = chips[1]
    validFlag = False
    while not validFlag:
        colNum = 0
        colNum = input(playerStr + "Place the Column Number\n")
        if not colNum.isnumeric() and colNum != "q":
            colNum = print("Not a valid column!")
        elif colNum =="q":
            sys.exit
        elif int(colNum) not in range(1,8) or gameBoard[0][int(colNum)-1] !=" ":
            colNum = print("Not a valid column!")
        else:
            validFlag = True    
    if colNum == "q":
        break
    colNum = int(colNum)
    filled = 0
    for row in range(len(gameBoard)-1, 0, -1):
        if gameBoard[row][colNum-1] in chips:
            filled += 1
    gameBoard[len(gameBoard)-1-filled][colNum-1] = chip
    print("Turn: " + str(turnCount))
    printGameBoard(gameBoard)
    #check for row connect fours
    for row in gameBoard:
        rowStr = ""
        rowStr = rowStr.join(row)
        if chips[0]*4 in rowStr or chips[1]*4 in rowStr:
            print("Winner! (Row)")
            print(row)
    #check for column connect fours
    for col in range(len(gameBoard[0])):
        colList = []
        colStr = ""
        for row in gameBoard:
            colList.append(row[col])
        colStr = colStr.join(colList)
        if chips[0]*4 in colStr or chips[1]*4 in colStr:
            print("Winner! (Col)")
            print(colList)
    #check for diagonal connect fours   
    for col in range(len(gameBoard[0])):
        diag1List = []
        diag1Str = ""
        if col != len(gameBoard[0])-1:
            for i in range(col+1):
                if i < len(gameBoard):
                    diag1List.append(gameBoard[i][col-i])
            diag1Str=diag1Str.join(diag1List)
            if chips[0]*4 in diag1Str or chips[1]*4 in diag1Str:
                print("Winner! (Diag1)")
                print(diag1List)
        else:
            for row in range(len(gameBoard)):
                diag1List = []
                diag1Str = ""
                for i in range(col+1):
                    if row+i < len(gameBoard):
                        diag1List.append(gameBoard[row+i][col-i])
                diag1Str=diag1Str.join(diag1List)
                if chips[0]*4 in diag1Str or chips[1]*4 in diag1Str:
                    print("Winner! (Diag1)")
                    print(diag1List)
    for col in range(len(gameBoard[0])):
        diag2List = []
        diag2Str = ""
        if col != 0:
            for i in range(col+1):
                if i < len(gameBoard[0]):
                    if len(gameBoard[0])-col+i < len(gameBoard[0]):
                        diag2List.append(gameBoard[i][len(gameBoard[0])-col+i])
            diag2Str=diag2Str.join(diag2List)
            if chips[0]*4 in diag2Str or chips[1]*4 in diag2Str:
                print("Winner! (Diag2)") 
                print(diag2List)
                print(diag2Str)
        else:
            for row in range(len(gameBoard)):
                diag2List = []
                diag2Str = ""
                for i in range(len(gameBoard[0])-col+1):
                    if row+i < len(gameBoard):
                        diag2List.append(gameBoard[row+i][col+i])
                diag2Str=diag2Str.join(diag2List)
                if chips[0]*4 in diag2Str or chips[1]*4 in diag2Str:
                    print("Winner! (Diag2)")
                    print(diag2List)
    

    
    

            
        