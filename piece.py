class Piece:
    def __init__(self):
        # Initialize piece properties
        self.numAround = None
        self.neighbors = None
        self.hasBomb = False
        self.clicked = False
        self.flagged = False

    def getHasBomb(self):
        return self.hasBomb

    def getClicked(self):
        return self.clicked

    def setNeighbors(self, neighbors):
        # Set the neighbors for the piece
        self.neighbors = neighbors
        self.setNumAround()

    def setNumAround(self):
        # Count the number of bombs around the piece
        self.numAround = 0
        for piece in self.neighbors:
            if piece.hasBomb:
                self.numAround += 1

    def getNumAround(self):
        return self.numAround

    def getFlagged(self):
        return self.flagged

    def toggleFlag(self):
        # Toggle the flagged status of the piece
        self.flagged = not self.flagged

    def click(self):
        # Set the piece as clicked
        self.clicked = True

    def getNeighbors(self):
        return self.neighbors
