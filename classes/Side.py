from classes.Piece import Piece


class Side:
    def __init__(self, colour):
        self.topleft = Piece(colour)
        self.top = Piece(colour)
        self.topright = Piece(colour)
        self.left = Piece(colour)
        self.middle = Piece(colour)
        self.right = Piece(colour)
        self.bottomleft = Piece(colour)
        self.bottom = Piece(colour)
        self.bottomright = Piece(colour)

        self.pieces = (self.topleft, self.top, self.topright, self.left, self.middle, self.right, self.bottomleft, self.bottom, self.bottomright)

    def colour(self):
        return self.middle.colour
