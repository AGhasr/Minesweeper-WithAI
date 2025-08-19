# solver.py
class Solver:
    def __init__(self, board):
        # Initialize the solver with the game board
        self.board = board

    def move(self):
        # Implement the AI's move strategy
        moves_made = False

        for row in self.board.getBoard():
            for piece in row:
                if not piece.getClicked():
                    continue

                neighbors = piece.getNeighbors()
                bombsAround = piece.getNumAround()

                unclicked_neighbors = [n for n in neighbors if not n.getClicked()]
                flagged_neighbors = [n for n in neighbors if n.getFlagged()]
                unflagged_unclicked = [n for n in unclicked_neighbors if not n.getFlagged()]

                # Strategy 1: If we've flagged all bombs around this piece, open the rest
                if len(flagged_neighbors) == bombsAround:
                    for neighbor in unflagged_unclicked:
                        self.board.handleClick(neighbor, False)
                        moves_made = True

                # Strategy 2: If all remaining unclicked neighbors must be bombs, flag them
                elif len(unclicked_neighbors) == bombsAround:
                    for neighbor in unflagged_unclicked:
                        self.board.handleClick(neighbor, True)
                        moves_made = True

        # If no logical moves found, make a random safe guess
        if not moves_made:
            moves_made = self.makeRandomMove()

        return moves_made

    def makeRandomMove(self):
        # Make a random move when no logical move is available
        import random

        unclicked_pieces = []
        for row in self.board.getBoard():
            for piece in row:
                if not piece.getClicked() and not piece.getFlagged():
                    unclicked_pieces.append(piece)

        if unclicked_pieces:
            # Choose a random unclicked, unflagged piece
            random_piece = random.choice(unclicked_pieces)
            self.board.handleClick(random_piece, False)
            return True

        return False
