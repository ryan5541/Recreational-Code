# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
#import random
import tkinter
from tkinter import messagebox
#import math
import sys


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
    #use pygame to create circles
    #specify the size of the circles
        #pygame.draw.circle()
    

# =============================================================================
# class blackChip(chip):
#     def __init__(self, name="Player 2"):
#         chip.__init__()
#         self.face = chip.CHIP_LIST[1]
#         self.color = chip.COLOR[1]
#         self.name = name
#     #color it black
#     #put name of player 1
#     
#     
# class redChip(chip):
#     def __init__(self, name="Player 1"):
#         chip.__init__()
#         self.face = chip.CHIP_LIST[0]
#         self.color = chip.COLOR_LIST[0]
#         self.name = name
#     #color it red
#     #put name of player 2
# =============================================================================
    
    
class board():
    #squares in columns
    #how many squares? size of squares?
    #pygame.rect()
    def __init__(self, width, height, background, screen):
        self.gameBoard = []
        self.squareBoard = {}
        self.area = pygame.Rect(0,0, (height//6)*7, height)
        self.area.centerx = width//2
        self.area.centery = height//2
        for row in range(6):
            self.gameBoard.append([])
            for col in range(7):
                self.gameBoard[row].append(" ")
                self.squareBoard[str(row)+"_"+str(col)] = square(row,col, self.area, background, screen)
            
    def boardReset(self):
        for row in self.gameBoard:
            for col in range(len(row)):
                row[col] = " "
        for i in self.squareBoard:
            self.squareBoard[i].filled = " "
            self.squareBoard[i].color = (255,255,255)
            self.squareBoard[i].updateSquare(self.squareBoard[i].color)
    

class square():
    #circle in the middle, same color as background
    #color it blue
    
    def __init__(self, row, col, boardRect, background, screen):
        self.row = row
        self.col = col
        self.filled = " "
        self.color = (255,255,255)
        self.screen = screen
        self.background = background
        self.boardRect = boardRect
        self.square = pygame.Rect(self.boardRect.left+self.col*self.boardRect.height//6,self.boardRect.top+row*self.boardRect.height//6,self.boardRect.height//6, self.boardRect.height//6)
        pygame.draw.rect(self.background, (0,0,255), self.square)
        pygame.draw.circle(self.background, self.color, self.square.center, self.square.width//2-5)
        self.screen.blit(self.background, self.square.center)
        # pygame.draw.circle(Surface, color, pos, radius, width=0) # from pygame documentation
        # draw blue filled circle on ball surface
   
    def updateSquare(self, color):
        self.color = color
        pygame.draw.circle(self.background, self.color, self.square.center, self.square.width//2-5)
        self.screen.blit(self.background, self.square.center)
        pygame.display.flip()
        #pygame.draw.rect()
        #pygame.draw.circle()
        
class CFinit():
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.player1 = player()
        self.player2 = player()
        pygame.init()
        pygame.display.set_caption("Connect Four - Genius Hour")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((255,255,255))
        self.screen.blit(self.background, (0,0))
        #starts the game
        CFgame(self.player1, self.player2, self.width, self.height, self.screen, self.background)
        

class CFgame():
    def __init__(self, player1, player2, width, height, screen, background):
        self.turnCount = 0
        #self.validFlag = False
        self.board = board(width, height, background, screen)
        self.winFlag = False     
        self.players = (player1, player2)
        #self.printGameBoard(self.board.gameBoard)
        self.reset = ""
        self.loopAgain = False
        self.font = pygame.font.SysFont('mono', 24, bold=True)
        self.winner = ""
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif events.type == pygame.MOUSEBUTTONDOWN and events.button == 1 and events.pos[0] >= self.board.area.left and events.pos[0] <= self.board.area.right and not self.winFlag:
                    for colNum in range(7):
                        if events.pos[0] >= self.board.area.left+(height//6)*colNum and events.pos[0] < self.board.area.left+(height//6)*(colNum+1):
                            #print(self.board.gameBoard[0][colNum])
                            break
                    if self.board.gameBoard[0][int(colNum)] == " ":
                        self.dropChip(self.board.gameBoard, self.updateTurn(), colNum + 1)
                elif self.winFlag:
                    self.resetGame(self.winner)         
                    
#            for square in board.squareBoard:
#                square.updateSquare(square.color)
            screen.blit(background, (0,0))
            pygame.display.flip()

        #while not self.winFlag:
            
        #self.resetGame()
#        """Initialize pygame, window, background, font,...
#        """
#        pygame.init()
#        pygame.display.set_caption("Press ESC to quit")
#        self.width = width
#        self.height = height
#        #self.height = width // 4
#        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
#        self.background = pygame.Surface(self.screen.get_size()).convert()
#        self.clock = pygame.time.Clock()
#        self.fps = fps
#        self.playtime = 0.0
#        self.font = pygame.font.SysFont('mono', 20, bold=True)
        

    #pygame.init()
    #background?
    #creates a surface to draw board and chips
    #pygame.Surface()
    #keep track of turn count
    def updateTurn(self):
        self.turnCount += 1
        if self.turnCount % 2 != 0:
            player = self.players[0]
        else:
            player = self.players[1]
        return player
            
    #what is a dropped chip?
    #stack chips
    #limit possible places for these chips   
    def dropChip(self, gameBoard, player, colNum):
# =============================================================================
#         validFlag=False
#         while not validFlag:
#             colNum = input(player.name + ", Place the Column Number\n")
#             if not colNum.isnumeric() and colNum != "q":
#                 colNum = print("Not a valid column!")
#             elif colNum =="q":
#                 sys.exit
#             elif int(colNum) not in range(1,8) or gameBoard[0][int(colNum)-1] !=" ":
#                 colNum = print("Not a valid column!")
#             else:
#                 validFlag = True 
# =============================================================================
        filled = 0
        for row in range(len(gameBoard)-1, 0, -1):
            if gameBoard[row][colNum-1] in player.CHIP_LIST:
                filled += 1
        gameBoard[len(gameBoard)-1-filled][colNum-1] = player.chip
        self.board.squareBoard[str(len(gameBoard)-1-filled)+"_"+str(colNum-1)].filled = player.chip
        #print(self.board.squareBoard[str(len(gameBoard)-1-filled)+"_"+str(colNum-1)].filled)
        self.board.squareBoard[str(len(gameBoard)-1-filled)+"_"+str(colNum-1)].updateSquare(player.color)
        #self.printGameBoard(gameBoard)
        self.checkForWinner(gameBoard, player)
        
    def printGameBoard(self, gameBoard):
        print("Turn Count:" + str(self.turnCount))
        for row in gameBoard:
            print(row)
            
    #window resolution
    #(optional) display FPS
    #make sure the board is not the same size as the window
    #connect 4 to win!
    #put win conditions
    #check for winner every time a chip is dropped
    def stringCheck(self, checkStr, player):
        if player.chip*4 in checkStr:
            #print(player.name + " wins!")
            self.winFlag = True
            self.winner = player.name
            #sys.exit()
            
    def checkForWinner(self, gameBoard, player):
        #check for row connect fours
        for row in gameBoard:
            rowStr = ""
            rowStr = rowStr.join(row)
            self.stringCheck(rowStr, player)
        #check for column connect fours
        for col in range(len(gameBoard[0])):
            colList = []
            colStr = ""
            for row in gameBoard:
                colList.append(row[col])
            colStr = colStr.join(colList)
            self.stringCheck(colStr, player)
        #check for diagonal connect fours   
        for col in range(len(gameBoard[0])):
            diag1List = []
            diag1Str = ""
            if col != len(gameBoard[0])-1:
                for i in range(col+1):
                    if i < len(gameBoard):
                        diag1List.append(gameBoard[i][col-i])
                diag1Str=diag1Str.join(diag1List)
                self.stringCheck(diag1Str, player)
            else:
                for row in range(len(gameBoard)):
                    diag1List = []
                    diag1Str = ""
                    for i in range(col+1):
                        if row+i < len(gameBoard):
                            diag1List.append(gameBoard[row+i][col-i])
                    diag1Str=diag1Str.join(diag1List)
                    self.stringCheck(diag1Str, player)          
        for col in range(len(gameBoard[0])):
            diag2List = []
            diag2Str = ""
            if col != 0:
                for i in range(col+1):
                    if i < len(gameBoard[0]):
                        if len(gameBoard[0])-col+i < len(gameBoard[0]):
                            diag2List.append(gameBoard[i][len(gameBoard[0])-col+i])
                diag2Str=diag2Str.join(diag2List)
                self.stringCheck(diag2Str, player)
            else:
                for row in range(len(gameBoard)):
                    diag2List = []
                    diag2Str = ""
                    for i in range(len(gameBoard[0])-col+1):
                        if row+i < len(gameBoard):
                            diag2List.append(gameBoard[row+i][col+i])
                    diag2Str=diag2Str.join(diag2List)
                    self.stringCheck(diag2Str, player)

    #reset mechanism
    def resetGame(self, winner):
#        reset = input("Would you like to play again? [y/n]\n")
#        while str(reset) not in "yn":
#            reset = input("Please enter a valid input! [y/n]\n")
#        if reset == "y":
        tkinter.Tk().withdraw()
        reset = tkinter.messagebox.askyesno(winner + " wins!", "Would you like to play again?")
        if reset == True:
            self.turnCount = 0
            self.board.boardReset()
            #self.printGameBoard(self.board.gameBoard)
            self.winner = ""
            self.winFlag = False
        else:
            pygame.quit()
            sys.exit
    #input player input() statement?
    
    #who goes first? possible random library?
    #(optional) player 1 wins!
    #tkinter.
    #(optional) bullet mode

if __name__ == "__main__":
    CFinit()

    