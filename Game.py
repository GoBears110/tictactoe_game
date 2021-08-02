from Board import Board
from Player import Player
import os
os.system("clear")

checkerBoard = Board(3)
playerOne = Player('X')
playerTwo = Player('O')
totalMoves = 0

def makeMove(player):
    playerChoice = int(input('\n%s) Choose a number 1-9:' % player.getPiece()))
    row = playerChoice // 3
    col = playerChoice % 3 - 1
    if playerChoice % 3 == 0:
        row -= 1
        col = 2
    checkerBoard.changePiece(row, col, player.getPiece())
    checkerBoard.display()


while True:
    checkerBoard.display()
    makeMove(playerOne)
    totalMoves += 1
    if totalMoves >= 9:
        break
    makeMove(playerTwo)
    totalMoves += 1
    if totalMoves > 9:
        break