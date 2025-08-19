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

    def run(self, use_solver=False, solver_delay=0.5):
        # Set up the Pygame screen
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption("Minesweeper")
        running = True
        solver = Solver(self.board) if use_solver else None

        clock = pygame.time.Clock()

        # Main game loop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and not use_solver:
                    pos = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(pos, rightClick)
                # Allow manual first click even in AI mode
                elif event.type == pygame.MOUSEBUTTONDOWN and use_solver and self.board.first:
                    pos = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(pos, rightClick)

            # If using the solver and the game is not over, let the solver make a move
            if use_solver and solver and not self.board.getWon() and not self.board.getLost() and not self.board.first:
                moves_made = solver.move()
                if moves_made:
                    self.draw(self.board.getLost())
                    pygame.display.flip()
                    sleep(solver_delay)

            # Draw the board only if game is still active
            if not self.board.getLost() and not self.board.getWon():
                self.draw(self.board.getLost())
                self.drawUI()
                pygame.display.flip()

            # Check for game end conditions
            if self.board.getLost():
                self.playLoseSound()
                self.draw(True)  # Draw with lost=True to show all bombs
                self.drawUI()
                self.displayLoseMessage()
                pygame.display.flip()
                sleep(3)
                running = False
            elif self.board.getWon():
                self.playWinSound()
                self.displayWinMessage()
                sleep(3)
                running = False

            clock.tick(60)  # Limit to 60 FPS

        # Quit Pygame when the game loop exits
        pygame.quit()

    def draw(self, lost):
        # Draw the game board
        self.screen.fill((192, 192, 192))  # Light gray background
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece, lost)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]

    def drawUI(self):
        # Draw UI elements like bomb counter
        bombs_text = self.font.render(f"Bombs: {self.board.getMinesNum()}", True, (0, 0, 0))
        # Position at top of screen with some padding
        self.screen.blit(bombs_text, (10, 10))

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
        if pos[1] < 0 or pos[0] < 0:  # Prevent negative indices
            return

        row = pos[1] // self.pieceSize[1]
        col = pos[0] // self.pieceSize[0]

        # Check bounds
        if row >= self.board.getSize()[0] or col >= self.board.getSize()[1]:
            return

        piece = self.board.getPiece((row, col))
        self.board.handleClick(piece, rightClick)

    def displayWinMessage(self):
        # Display a message on the screen after winning
        overlay = pygame.Surface(self.screenSize)
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        font = pygame.font.Font(None, 74)
        text = font.render("You Won!", True, (0, 255, 0))
        text_rect = text.get_rect(center=(self.screenSize[0] // 2, self.screenSize[1] // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def displayLoseMessage(self):
        # Display a message on the screen after losing
        overlay = pygame.Surface(self.screenSize)
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        font = pygame.font.Font(None, 74)
        text = font.render("Game Over!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.screenSize[0] // 2, self.screenSize[1] // 2))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def playWinSound(self):
        # Play win sound
        sound = pygame.mixer.Sound("sounds/win.wav")
        sound.play()

    def playLoseSound(self):
        # Play lose sound
        sound = pygame.mixer.Sound("sounds/lose.wav")
        sound.play()
