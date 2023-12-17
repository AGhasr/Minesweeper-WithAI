import pygame
from game import Game
from board import Board
from solver import Solver

# Set the size of the Minesweeper board and the number of mines
size = (20, 20)
minesNum = 30

# Create a Minesweeper board with the specified size and number of mines
board = Board(size, minesNum)

# Set the size of the game window
screenSize = (800, 800)

# Create a Minesweeper game instance with the created board and window size
game = Game(board, screenSize)

# Create an AI (Solver) instance for the Minesweeper board
ai_solver = Solver(board)

# Run the Minesweeper game, with the AI making decisions
game.run(use_solver=True)

# Quit Pygame after the game has finished
pygame.quit()
