import pygame
from time import sleep
import os
from solver import Solver

# Initialize Pygame
pygame.init()


class Game:
    def __init__(self, board, screenSize):
        # Initialize game properties
        self.images = None
        self.screen = None
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = (
            self.screenSize[0] // self.board.getSize()[1],
            self.screenSize[1] // self.board.getSize()[0],
        )

        self.font = pygame.font.Font(None, 36)
        self.loadImages()
        self.bombsLeft = self.board.getMinesNum()

    def run(self, use_solver=False, solver_delay=1):
        # Set up the Pygame screen
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        solver = Solver(self.board)

        # Main game loop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(pos, rightClick)

            # If using the solver and the game is not over, let the solver make a move
            if use_solver and not self.board.getWon() and not self.board.getLost():
                solver.move()
                self.draw(self.board.getLost())
                pygame.display.flip()
                sleep(solver_delay)
            else:
                # Draw the board without solver
                self.draw(self.board.getLost())
                pygame.display.flip()

            # Check for win condition
            if self.board.getWon():
                sound = pygame.mixer.Sound("win.wav")
                sound.play()
                self.displayWinMessage()
                sleep(2)
                running = False

        # Quit Pygame when the game loop exits
        pygame.quit()

    def draw(self, lost):
        # Draw the game board
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece, lost)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]

    # Add comments for the loadImages and getImage methods

    def loadImages(self):
        # Load and scale images for different game pieces
        self.images = {}
        for fileName in os.listdir("images"):
            if not fileName.endswith(".png"):
                continue
            image = pygame.image.load(r"images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

    def getImage(self, piece, lost):
        # Get the appropriate image for a given game piece
        if piece.getClicked():
            string = "bomb-at-clicked-block" if piece.getHasBomb() else str(piece.getNumAround())
        elif piece.getFlagged() and not lost:
            string = "flag"
        else:
            if piece.getFlagged() and not piece.getHasBomb():
                string = "wrong-flag"
            elif lost and piece.getHasBomb():
                string = "unclicked-bomb"
            else:
                string = "empty-block"

        return self.images[string]

    def handleClick(self, pos, rightClick):
        # Handle mouse clicks on the game board(pieces)
        index = pos[1] // self.pieceSize[1], pos[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)

    def displayWinMessage(self):
        # Display a message on the screen after winning
        font = pygame.font.Font(None, 74)
        text = font.render("You Won!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.screenSize[0] // 2, self.screenSize[1] // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
