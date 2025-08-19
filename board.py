from piece import Piece
from random import randint


class Board:
    def __init__(self, size, minesNum):
        # Initialize board properties
        self.board = None
        self.lost = False
        self.won = False
        self.numClicked = 0
        self.numNonBombs = size[0] * size[1] - minesNum
        self.size = size
        self.minesNum = minesNum
        self.originalMinesNum = minesNum  # Keep track of original number for display

        self.setBoard()
        self.first = True

    def setBoard(self):
        # Create an empty game board
        self.board = []
        for row in range(self.size[0]):
            board_row = []
            for col in range(self.size[1]):
                piece = Piece()
                board_row.append(piece)
            self.board.append(board_row)

    def setNeighbors(self):
        # Set the neighbors for each piece on the board
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row, col))
                piece.setNeighbors(neighbors)

    def getListOfNeighbors(self, index):
        # Get a list of neighboring pieces for a given piece index
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                outOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if outOfBounds or same:
                    continue
                neighbors.append(self.getPiece((row, col)))
        return neighbors

    def getSize(self):
        return self.size

    def getPiece(self, index):
        return self.board[index[0]][index[1]]

    def handleClick(self, piece, flag):
        # Handle a click on a game piece
        # First click should never be a bomb, so we initialize the bombs after the first click
        if self.first:
            self.initializeBoard(piece)
            self.first = False

        if self.lost or self.won:
            return

        # If the piece was already clicked, or we wanted to open while it's flagged, we don't do anything
        if piece.getClicked() or (not flag and piece.getFlagged()):
            return

        if flag:
            if piece.getFlagged():
                self.minesNum += 1
            else:
                self.minesNum -= 1
            piece.toggleFlag()
            return

        piece.click()

        if piece.getHasBomb():
            self.lost = True
            return

        self.numClicked += 1

        # Auto-reveal neighboring empty cells
        if piece.getNumAround() == 0:
            for neighbor in piece.getNeighbors():
                if (not neighbor.getHasBomb()) and (not neighbor.getClicked()):
                    self.handleClick(neighbor, False)

    def getWon(self):
        # Check if the game is won
        if self.first:
            return False
        return self.numNonBombs == self.numClicked

    def getLost(self):
        return self.lost

    def initializeBoard(self, clickedPiece):
        # Initialize the game board with mines, ensuring first click is safe
        minesCount = self.originalMinesNum
        placedMines = 0
        attempts = 0
        max_attempts = self.size[0] * self.size[1] * 10  # Prevent infinite loop

        while placedMines < minesCount and attempts < max_attempts:
            random_row = randint(0, self.size[0] - 1)
            random_col = randint(0, self.size[1] - 1)
            potential_piece = self.board[random_row][random_col]

            # Don't place mine on clicked piece or if already has mine
            if potential_piece != clickedPiece and not potential_piece.getHasBomb():
                potential_piece.hasBomb = True
                placedMines += 1

            attempts += 1

        self.setNeighbors()

    def getBoard(self):
        return self.board

    def getMinesNum(self):
        return self.minesNum
