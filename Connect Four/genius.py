# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 22:17:13 2018

@author: Visitor
"""

import sys
import pygame
import tkinter
from tkinter import messagebox

#def printGameBoard(gameBoard):
#    for row in range(len(gameBoard)):
#        print(gameBoard[row])
#
#def resetgameboard(gameBoard):
#    for row in gameBoard:
#        for col in range(len(row)):
#            row[col] = " "

#def checkgamelist(gamelist):
#    if "1" * 4 in "".join(gamelist) or "2" * 4 in "".join(gamelist):
#        print("You Win!")
#        return True
#    else:
#        return False

class player():
    PLAYER_COUNT = 0
    CHIP_LIST = ["1","2"]
    COLOR_LIST = [(255,0,0), (0,0,0)]
    
    def __init__(self, name=""):
        player.PLAYER_COUNT += 1
        if name == "":
            self.name = "Player "+str(player.PLAYER_COUNT)
        else:
            self.name = name
        self.chip = player.CHIP_LIST[player.PLAYER_COUNT - 1]
        self.color = player.COLOR_LIST[player.PLAYER_COUNT - 1]

class CFBoard():
    def __init__(self, screen, background):
        self.gameBoard = []
        self.squareBoard = {}
        self.background = background
        self.boardRect = pygame.Rect(0, 0, screen.get_size()[1]//6*7, screen.get_size()[1])
        self.boardRect.center = self.background.get_rect().center
        for row in range(0,6):
            self.gameBoard.append([])
            for col in range(7):
                self.gameBoard[row].append(" ")
                self.squareBoard[str(row) + "_" + str(col)] = square(row, col, self.background, self.boardRect, screen.get_size()[1]).drawsquare()
                
    def printGameBoard(self):
        for row in range(len(self.gameBoard)):
            print(self.gameBoard[row])

    def resetgameboard(self):
        for row in self.gameBoard:
            for col in range(len(row)):
                row[col] = " "
        for square in self.squareBoard:
            self.squareBoard[square].updatesquare((255,255,255))
                
    def drawboard(self):
        #Rect(left, top, width, height) 
        self.boardRect = pygame.Rect(240, 0, 600, 480)
        #pygame.draw.rect(Surface, color, Rect, width=0)
        
class square():
    def __init__(self, row, col, background, boardRect, height):
        self.background = background
        self.row = row
        self.col = col
        self.height = height
        self.color = (255,255,255)
        self.squareRect = ""
        #self.filled = " "
        #square.background = background
        self.boardRect = boardRect
        
    def drawsquare(self):
        self.squareRect = pygame.draw.rect(self.background, (0,0,255), (self.boardRect.left + self.height//6*self.col,self.boardRect.top + self.height//6*self.row,self.height//6,self.height//6))
        # pygame.draw.circle(Surface, color, pos, radius, width=0)
        pygame.draw.circle(self.background, self.color, self.squareRect.center, self.height//6//2 - 5)
        return(self)
                
    def updatesquare(self, color):
        self.color = color
        pygame.draw.circle(self.background, self.color, self.squareRect.center, self.height//6//2 - 5)
        
        

class CFInit():
    #create the window, put a caption on the window titled "Genius Hour", the surface, and make it white
    def __init__(self, width=640, height=480):
        pygame.init()
        pygame.display.set_caption("Genius Hour")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((255,255,255))
        CFGame(self.screen, self.background).mainloop()
        #Rect(left, top, width, height) 
#        self.boardRect = pygame.Rect(0, 0, self.height//6*7, self.height)
#        self.boardRect.center = self.background.get_rect().center
        
        #pygame.draw.rect(Surface, color, Rect, width=0)
        #pygame.draw.rect(self.background, (0,0,255), self.boardRect)
#        for colNum in range(7):
#            for row in range(6):
#                squareRect = pygame.draw.rect(self.background, (0,0,255), (self.boardRect.left + self.height//6*colNum,self.boardRect.top + self.height//6*row,self.height//6,self.height//6))
#                # pygame.draw.circle(Surface, color, pos, radius, width=0)
#                pygame.draw.circle(self.background, (255,255,255), squareRect.center, self.height//6//2 - 5)
                
        
#        running = True
#        while running:
#            self.screen.blit(self.background, (0, 0))
#            pygame.display.flip()
            
            
class CFGame():
    def __init__(self, screen, background):
        self.board = CFBoard(screen, background)
        self.screen = screen
        self.background = background
        self.players = [player(), player()]
    
    def checkgamelist(self, gamelist):
        if "1" * 4 in "".join(gamelist) or "2" * 4 in "".join(gamelist):
            print("You Win!")
            return True
        else:
            return False
    
    def screenrefresh(self):
        #set up a while loop, tells the screen to update, draw background to RAM
#        running = True
#        while running:
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
    
    def mainloop(self):
        loopCheck = "y"
        while loopCheck == "y":
            turncount = 0
            winflag = False
            self.board.printGameBoard()
            while winflag == False:
                for colNum in range(len(self.board.gameBoard[0])):
                    if self.board.gameBoard[0][colNum] == " ":
                        break
                    elif colNum == len(self.board.gameBoard[0]) - 1:
                        winflag = True
                if winflag:
                    winStr = "It's a Draw!"
                    break
                turncount += 1
                if turncount % 2 == 0:                    
                    #chip = "2" 
                    player = self.players[1]
                else:
                    #chip = "1"
                    player = self.players[0]
                print(turncount)
#                print("Player " + chip + " Turn")
#                colNum = input("Input column in which you want to place chip: ")
#                validFlag = False
#                while validFlag == False:
#                    if colNum.isnumeric() == False and colNum != "q":
#                       colNum = input("Please input a number from 1-7")
#                    elif colNum == "q":
#                        sys.exit()
#                    elif int(colNum) < 1 or int(colNum) > 7:
#                        colNum = input("Please input a number from 1-7")
#                    elif self.board.gameBoard[0][int(colNum) - 1] != " ":
#                        colNum = input("Column already filled! Enter another column.")
#                    else:
#                        validFlag = True
                #colNum = "4"
                clickflag = False
                while not clickflag:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.board.boardRect.collidepoint(event.pos):
                            for square in self.board.squareBoard:
                                #print(square)
                                if self.board.squareBoard[square].squareRect.collidepoint(event.pos):
                                    colNum = self.board.squareBoard[square].col + 1
                                    if self.board.gameBoard[0][colNum - 1] == " ":
                                        clickflag = True
                    self.screenrefresh()
                #printGameBoard(gameBoard[colNum-1])
                filled = 0
                for rowNum in range(len(self.board.gameBoard)):
                    if self.board.gameBoard[-rowNum][colNum-1] != " ":
                        filled += 1
                self.board.gameBoard[len(self.board.gameBoard) - 1 - filled][colNum - 1] = player.chip
                self.board.squareBoard[str(len(self.board.gameBoard) - 1 - filled) + "_" + str(colNum - 1)].updatesquare(player.color)
                self.screenrefresh()
                self.board.printGameBoard()
                if not winflag:
                    for row in self.board.gameBoard:
                        winflag = self.checkgamelist(row)
                        if winflag:
                            winStr = player.name + " wins!"
                            break
                if not winflag:
                    for colNum in range(len(self.board.gameBoard[0])):
                        colList = []
                        for rowNum in range(len(self.board.gameBoard)):
                            colList.append(self.board.gameBoard[rowNum][colNum])
                        winflag = self.checkgamelist(colList)
                        if winflag:
                            winStr = player.name + " wins!"
                            break
                if not winflag:
                    for colNum in range(len(self.board.gameBoard[0])):
                        diag1list = []
                        if colNum != len(self.board.gameBoard[0])-1:
                            for i in range(colNum + 1):
                                if i < len(self.board.gameBoard):
                                    diag1list.append(self.board.gameBoard[i][colNum - i])
                                if self.checkgamelist(diag1list):
                                    winflag = True
                                    break
                            #print(diag1list)
                        else:
                            for rowNum in range(len(self.board.gameBoard)):
                                diag1list = []
                                for i in range(colNum + 1):
                                    if rowNum + i < len(self.board.gameBoard):
                                        diag1list.append(self.board.gameBoard[rowNum + i][colNum - i])
                                    if self.checkgamelist(diag1list):
                                        winflag = True
                                        break
                        #winflag = self.checkgamelist(diag1list)
                        if winflag:
                            winStr = player.name + " wins!"
                            break
                if not winflag:
                    for colNum in range(1,len(self.board.gameBoard[0])+1):
                        diag2list = []
                        if -colNum != -len(self.board.gameBoard[0]):
                            for i in range(colNum + 1):
                                if -colNum + i < 0:
                                    diag2list.append(self.board.gameBoard[i][-colNum + i])
                                if self.checkgamelist(diag2list):
                                    winflag = True
                                    break
                            #print(diag2list)
                        else:
                            for rowNum in range(len(self.board.gameBoard)):
                                diag2list = []
                                for i in range(colNum + 1):
                                   if rowNum + i < len(self.board.gameBoard):
                                       diag2list.append(self.board.gameBoard[rowNum + i][-colNum + i])
                                if self.checkgamelist(diag2list):
                                    winflag = True
                                    break
                        #winflag = self.checkgamelist(diag2list)
                        if winflag:
                            winStr = player.name + " wins!"
                            break
            loopCheck = " "
#            while loopCheck not in "yn":
#                loopCheck = input("Would you like to play again? [y/n]")
            tkinter.Tk().withdraw()
            reset = tkinter.messagebox.askyesno(winStr, "Would you like to play again?")
            if reset == True:
                loopCheck = "y"
            elif reset == False:
                loopCheck = "n"
                pygame.quit()
            if loopCheck == "y":
                self.board.resetgameboard()
                self.screenrefresh()
                pygame.event.clear()
    
if __name__ == "__main__":
    #CFGame().mainloop()
    CFInit()
    
    
        


