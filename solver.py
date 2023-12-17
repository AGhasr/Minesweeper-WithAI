class Solver:
    def __init__(self, board):
        # Initialize the solver with the game board
        self.board = board

    def move(self):
        # Implement the AI's move strategy
        for row in self.board.getBoard():
            for piece in row:
                if not piece.getClicked():
                    continue
                neighbors = piece.getNeighbors()
                bombAround = piece.getNumAround()
                notOpen = 0
                flagged = 0
                for neighbor in neighbors:
                    if neighbor.getFlagged():
                        flagged += 1
                    if not neighbor.getClicked():
                        notOpen += 1
                if flagged == bombAround:
                    self.openTheRest(neighbors)
                if notOpen == bombAround:
                    self.flagTheRest(neighbors)

    def openTheRest(self, neighbors):
        # Open the remaining unclicked neighbors
        for neighbor in neighbors:
            if not neighbor.getFlagged():
                self.board.handleClick(neighbor, False)

    def flagTheRest(self, neighbors):
        # Flag the remaining unflagged neighbors
        for neighbor in neighbors:
            if not neighbor.getFlagged():
                self.board.handleClick(neighbor, True)
