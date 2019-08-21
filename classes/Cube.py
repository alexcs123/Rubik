from random import choice
from classes.Side import Side
from enums.States import States
from enums.Colours import Colours


class Cube:
    """Cube object"""
    def __init__(self, state=States.solved):
        """Constructs cube in given state"""
        self.up = Side(Colours.white)
        self.front = Side(Colours.red)
        self.right = Side(Colours.blue)
        self.back = Side(Colours.orange)
        self.left = Side(Colours.green)
        self.down = Side(Colours.yellow)

        self._sides = (self.up, self.front, self.right, self.back, self.left, self.down)
        self.shuffles = None
        self.time = None

        if state == States.scrambled:
            self.scramble()

    def state(self):
        """Returns state of cube"""
        for side in self._sides:
            for piece in side.pieces:
                if piece.colour != side.colour():
                    return States.scrambled

        return States.solved

    def scramble(self, shuffles=100):
        """Scrambles cube with given number of turns"""
        turns = ''

        for i in range(shuffles):
            turns += choice(['u ', 'f ', 'r ', 'b ', 'l ', 'd ', 'ui ', 'fi ', 'ri ', 'bi ', 'li ', 'di ', 'x ', 'y ', 'z ', 'xi ', 'yi ', 'zi '])

        self.shuffles = turns[:-1]
        self.turn(self.shuffles)

    def turn(self, turns):
        """Performs sequence of turns"""
        for turn in turns.split():
            if turn == 'u':
                self._turnup()
            elif turn == 'f':
                self._turnfront()
            elif turn == 'r':
                self._turnright()
            elif turn == 'b':
                self._turnback()
            elif turn == 'l':
                self._turnleft()
            elif turn == 'd':
                self._turndown()
            elif turn == 'x':
                self._turnx()
            elif turn == 'y':
                self._turny()
            elif turn == 'z':
                self._turnz()
            elif turn == 'ui':
                self._turnupinv()
            elif turn == 'fi':
                self._turnfrontinv()
            elif turn == 'ri':
                self._turnrightinv()
            elif turn == 'bi':
                self._turnbackinv()
            elif turn == 'li':
                self._turnleftinv()
            elif turn == 'di':
                self._turndowninv()
            elif turn == 'xi':
                self._turnxinv()
            elif turn == 'yi':
                self._turnyinv()
            elif turn == 'zi':
                self._turnzinv()
            elif turn == '2u':
                self._turn2up()
            elif turn == '2f':
                self._turn2front()
            elif turn == '2r':
                self._turn2right()
            elif turn == '2b':
                self._turn2back()
            elif turn == '2l':
                self._turn2left()
            elif turn == '2d':
                self._turn2down()
            elif turn == '2x':
                self._turn2x()
            elif turn == '2y':
                self._turn2y()
            elif turn == '2z':
                self._turn2z()

    def _turnup(self):
        """Performs an up turn"""
        buffer = self.up.topleft.colour
        self.up.topleft.colour = self.up.bottomleft.colour
        self.up.bottomleft.colour = self.up.bottomright.colour
        self.up.bottomright.colour = self.up.topright.colour
        self.up.topright.colour = buffer

        buffer = self.up.top.colour
        self.up.top.colour = self.up.left.colour
        self.up.left.colour = self.up.bottom.colour
        self.up.bottom.colour = self.up.right.colour
        self.up.right.colour = buffer

        buffer = self.front.topleft.colour
        self.front.topleft.colour = self.right.topleft.colour
        self.right.topleft.colour = self.back.topright.colour
        self.back.topright.colour = self.left.topleft.colour
        self.left.topleft.colour = buffer

        buffer = self.front.top.colour
        self.front.top.colour = self.right.top.colour
        self.right.top.colour = self.back.top.colour
        self.back.top.colour = self.left.top.colour
        self.left.top.colour = buffer

        buffer = self.front.topright.colour
        self.front.topright.colour = self.right.topright.colour
        self.right.topright.colour = self.back.topleft.colour
        self.back.topleft.colour = self.left.topright.colour
        self.left.topright.colour = buffer

    def _turnfront(self):
        """Performs a front turn"""
        buffer = self.front.topleft.colour
        self.front.topleft.colour = self.front.bottomleft.colour
        self.front.bottomleft.colour = self.front.bottomright.colour
        self.front.bottomright.colour = self.front.topright.colour
        self.front.topright.colour = buffer

        buffer = self.front.top.colour
        self.front.top.colour = self.front.left.colour
        self.front.left.colour = self.front.bottom.colour
        self.front.bottom.colour = self.front.right.colour
        self.front.right.colour = buffer

        buffer = self.up.bottomleft.colour
        self.up.bottomleft.colour = self.left.bottomright.colour
        self.left.bottomright.colour = self.down.bottomright.colour
        self.down.bottomright.colour = self.right.topleft.colour
        self.right.topleft.colour = buffer

        buffer = self.up.bottom.colour
        self.up.bottom.colour = self.left.right.colour
        self.left.right.colour = self.down.bottom.colour
        self.down.bottom.colour = self.right.left.colour
        self.right.left.colour = buffer

        buffer = self.up.bottomright.colour
        self.up.bottomright.colour = self.left.topright.colour
        self.left.topright.colour = self.down.bottomleft.colour
        self.down.bottomleft.colour = self.right.bottomleft.colour
        self.right.bottomleft.colour = buffer

    def _turnright(self):
        """Performs a right turn"""
        buffer = self.right.topleft.colour
        self.right.topleft.colour = self.right.bottomleft.colour
        self.right.bottomleft.colour = self.right.bottomright.colour
        self.right.bottomright.colour = self.right.topright.colour
        self.right.topright.colour = buffer

        buffer = self.right.top.colour
        self.right.top.colour = self.right.left.colour
        self.right.left.colour = self.right.bottom.colour
        self.right.bottom.colour = self.right.right.colour
        self.right.right.colour = buffer

        buffer = self.up.bottomright.colour
        self.up.bottomright.colour = self.front.bottomright.colour
        self.front.bottomright.colour = self.down.topright.colour
        self.down.topright.colour = self.back.topright.colour
        self.back.topright.colour = buffer

        buffer = self.up.right.colour
        self.up.right.colour = self.front.right.colour
        self.front.right.colour = self.down.right.colour
        self.down.right.colour = self.back.right.colour
        self.back.right.colour = buffer

        buffer = self.up.topright.colour
        self.up.topright.colour = self.front.topright.colour
        self.front.topright.colour = self.down.bottomright.colour
        self.down.bottomright.colour = self.back.bottomright.colour
        self.back.bottomright.colour = buffer

    def _turnback(self):
        """Performs a back turn"""
        buffer = self.back.topleft.colour
        self.back.topleft.colour = self.back.topright.colour
        self.back.topright.colour = self.back.bottomright.colour
        self.back.bottomright.colour = self.back.bottomleft.colour
        self.back.bottomleft.colour = buffer

        buffer = self.back.top.colour
        self.back.top.colour = self.back.right.colour
        self.back.right.colour = self.back.bottom.colour
        self.back.bottom.colour = self.back.left.colour
        self.back.left.colour = buffer

        buffer = self.up.topleft.colour
        self.up.topleft.colour = self.right.topright.colour
        self.right.topright.colour = self.down.topright.colour
        self.down.topright.colour = self.left.bottomleft.colour
        self.left.bottomleft.colour = buffer

        buffer = self.up.top.colour
        self.up.top.colour = self.right.right.colour
        self.right.right.colour = self.down.top.colour
        self.down.top.colour = self.left.left.colour
        self.left.left.colour = buffer

        buffer = self.up.topright.colour
        self.up.topright.colour = self.right.bottomright.colour
        self.right.bottomright.colour = self.down.topleft.colour
        self.down.topleft.colour = self.left.topleft.colour
        self.left.topleft.colour = buffer

    def _turnleft(self):
        """Performs a left turn"""
        buffer = self.left.topleft.colour
        self.left.topleft.colour = self.left.bottomleft.colour
        self.left.bottomleft.colour = self.left.bottomright.colour
        self.left.bottomright.colour = self.left.topright.colour
        self.left.topright.colour = buffer

        buffer = self.left.top.colour
        self.left.top.colour = self.left.left.colour
        self.left.left.colour = self.left.bottom.colour
        self.left.bottom.colour = self.left.right.colour
        self.left.right.colour = buffer

        buffer = self.up.topleft.colour
        self.up.topleft.colour = self.back.bottomleft.colour
        self.back.bottomleft.colour = self.down.bottomleft.colour
        self.down.bottomleft.colour = self.front.topleft.colour
        self.front.topleft.colour = buffer

        buffer = self.up.left.colour
        self.up.left.colour = self.back.left.colour
        self.back.left.colour = self.down.left.colour
        self.down.left.colour = self.front.left.colour
        self.front.left.colour = buffer

        buffer = self.up.bottomleft.colour
        self.up.bottomleft.colour = self.back.topleft.colour
        self.back.topleft.colour = self.down.topleft.colour
        self.down.topleft.colour = self.front.bottomleft.colour
        self.front.bottomleft.colour = buffer

    def _turndown(self):
        """Performs a down turn"""
        buffer = self.down.topleft.colour
        self.down.topleft.colour = self.down.topright.colour
        self.down.topright.colour = self.down.bottomright.colour
        self.down.bottomright.colour = self.down.bottomleft.colour
        self.down.bottomleft.colour = buffer

        buffer = self.down.top.colour
        self.down.top.colour = self.down.right.colour
        self.down.right.colour = self.down.bottom.colour
        self.down.bottom.colour = self.down.left.colour
        self.down.left.colour = buffer

        buffer = self.front.bottomleft.colour
        self.front.bottomleft.colour = self.left.bottomleft.colour
        self.left.bottomleft.colour = self.back.bottomright.colour
        self.back.bottomright.colour = self.right.bottomleft.colour
        self.right.bottomleft.colour = buffer

        buffer = self.front.bottom.colour
        self.front.bottom.colour = self.left.bottom.colour
        self.left.bottom.colour = self.back.bottom.colour
        self.back.bottom.colour = self.right.bottom.colour
        self.right.bottom.colour = buffer

        buffer = self.front.bottomright.colour
        self.front.bottomright.colour = self.left.bottomright.colour
        self.left.bottomright.colour = self.back.bottomleft.colour
        self.back.bottomleft.colour = self.right.bottomright.colour
        self.right.bottomright.colour = buffer

    def _turnx(self):
        """Performs an x rotation"""
        self._turnright()
        self._turnleftinv()

        buffer = self.up.top.colour
        self.up.top.colour = self.front.top.colour
        self.front.top.colour = self.down.bottom.colour
        self.down.bottom.colour = self.back.bottom.colour
        self.back.bottom.colour = buffer

        buffer = self.up.middle.colour
        self.up.middle.colour = self.front.middle.colour
        self.front.middle.colour = self.down.middle.colour
        self.down.middle.colour = self.back.middle.colour
        self.back.middle.colour = buffer

        buffer = self.up.bottom.colour
        self.up.bottom.colour = self.front.bottom.colour
        self.front.bottom.colour = self.down.top.colour
        self.down.top.colour = self.back.top.colour
        self.back.top.colour = buffer

    def _turny(self):
        """Performs a y rotation"""
        self._turnup()
        self._turndowninv()

        buffer = self.front.left.colour
        self.front.left.colour = self.right.left.colour
        self.right.left.colour = self.back.right.colour
        self.back.right.colour = self.left.left.colour
        self.left.left.colour = buffer

        buffer = self.front.middle.colour
        self.front.middle.colour = self.right.middle.colour
        self.right.middle.colour = self.back.middle.colour
        self.back.middle.colour = self.left.middle.colour
        self.left.middle.colour = buffer

        buffer = self.front.right.colour
        self.front.right.colour = self.right.right.colour
        self.right.right.colour = self.back.left.colour
        self.back.left.colour = self.left.right.colour
        self.left.right.colour = buffer

    def _turnz(self):
        """Performs a z rotation"""
        self._turnfront()
        self._turnbackinv()

        buffer = self.up.left.colour
        self.up.left.colour = self.left.bottom.colour
        self.left.bottom.colour = self.down.right.colour
        self.down.right.colour = self.right.top.colour
        self.right.top.colour = buffer

        buffer = self.up.middle.colour
        self.up.middle.colour = self.left.middle.colour
        self.left.middle.colour = self.down.middle.colour
        self.down.middle.colour = self.right.middle.colour
        self.right.middle.colour = buffer

        buffer = self.up.right.colour
        self.up.right.colour = self.left.top.colour
        self.left.top.colour = self.down.left.colour
        self.down.left.colour = self.right.bottom.colour
        self.right.bottom.colour = buffer

    def _turnupinv(self):
        """Performs an up inverted turn"""
        buffer = self.up.topleft.colour
        self.up.topleft.colour = self.up.topright.colour
        self.up.topright.colour = self.up.bottomright.colour
        self.up.bottomright.colour = self.up.bottomleft.colour
        self.up.bottomleft.colour = buffer

        buffer = self.up.top.colour
        self.up.top.colour = self.up.right.colour
        self.up.right.colour = self.up.bottom.colour
        self.up.bottom.colour = self.up.left.colour
        self.up.left.colour = buffer

        buffer = self.front.topleft.colour
        self.front.topleft.colour = self.left.topleft.colour
        self.left.topleft.colour = self.back.topright.colour
        self.back.topright.colour = self.right.topleft.colour
        self.right.topleft.colour = buffer

        buffer = self.front.top.colour
        self.front.top.colour = self.left.top.colour
        self.left.top.colour = self.back.top.colour
        self.back.top.colour = self.right.top.colour
        self.right.top.colour = buffer

        buffer = self.front.topright.colour
        self.front.topright.colour = self.left.topright.colour
        self.left.topright.colour = self.back.topleft.colour
        self.back.topleft.colour = self.right.topright.colour
        self.right.topright.colour = buffer

    def _turnfrontinv(self):
        """Performs a front inverted turn"""
        buffer = self.front.topleft.colour
        self.front.topleft.colour = self.front.topright.colour
        self.front.topright.colour = self.front.bottomright.colour
        self.front.bottomright.colour = self.front.bottomleft.colour
        self.front.bottomleft.colour = buffer

        buffer = self.front.top.colour
        self.front.top.colour = self.front.right.colour
        self.front.right.colour = self.front.bottom.colour
        self.front.bottom.colour = self.front.left.colour
        self.front.left.colour = buffer

        buffer = self.up.bottomleft.colour
        self.up.bottomleft.colour = self.right.topleft.colour
        self.right.topleft.colour = self.down.bottomright.colour
        self.down.bottomright.colour = self.left.bottomright.colour
        self.left.bottomright.colour = buffer

        buffer = self.up.bottom.colour
        self.up.bottom.colour = self.right.left.colour
        self.right.left.colour = self.down.bottom.colour
        self.down.bottom.colour = self.left.right.colour
        self.left.right.colour = buffer

        buffer = self.up.bottomright.colour
        self.up.bottomright.colour = self.right.bottomleft.colour
        self.right.bottomleft.colour = self.down.bottomleft.colour
        self.down.bottomleft.colour = self.left.topright.colour
        self.left.topright.colour = buffer

    def _turnrightinv(self):
        """Performs a right inverted turn"""
        buffer = self.right.topleft.colour
        self.right.topleft.colour = self.right.topright.colour
        self.right.topright.colour = self.right.bottomright.colour
        self.right.bottomright.colour = self.right.bottomleft.colour
        self.right.bottomleft.colour = buffer

        buffer = self.right.top.colour
        self.right.top.colour = self.right.right.colour
        self.right.right.colour = self.right.bottom.colour
        self.right.bottom.colour = self.right.left.colour
        self.right.left.colour = buffer

        buffer = self.up.bottomright.colour
        self.up.bottomright.colour = self.back.topright.colour
        self.back.topright.colour = self.down.topright.colour
        self.down.topright.colour = self.front.bottomright.colour
        self.front.bottomright.colour = buffer

        buffer = self.up.right.colour
        self.up.right.colour = self.back.right.colour
        self.back.right.colour = self.down.right.colour
        self.down.right.colour = self.front.right.colour
        self.front.right.colour = buffer

        buffer = self.up.topright.colour
        self.up.topright.colour = self.back.bottomright.colour
        self.back.bottomright.colour = self.down.bottomright.colour
        self.down.bottomright.colour = self.front.topright.colour
        self.front.topright.colour = buffer

    def _turnbackinv(self):
        """Performs a back inverted turn"""
        buffer = self.back.topleft.colour
        self.back.topleft.colour = self.back.bottomleft.colour
        self.back.bottomleft.colour = self.back.bottomright.colour
        self.back.bottomright.colour = self.back.topright.colour
        self.back.topright.colour = buffer

        buffer = self.back.top.colour
        self.back.top.colour = self.back.left.colour
        self.back.left.colour = self.back.bottom.colour
        self.back.bottom.colour = self.back.right.colour
        self.back.right.colour = buffer

        buffer = self.up.topleft.colour
        self.up.topleft.colour = self.left.bottomleft.colour
        self.left.bottomleft.colour = self.down.topright.colour
        self.down.topright.colour = self.right.topright.colour
        self.right.topright.colour = buffer

        buffer = self.up.top.colour
        self.up.top.colour = self.left.left.colour
        self.left.left.colour = self.down.top.colour
        self.down.top.colour = self.right.right.colour
        self.right.right.colour = buffer

        buffer = self.up.topright.colour
        self.up.topright.colour = self.left.topleft.colour
        self.left.topleft.colour = self.down.topleft.colour
        self.down.topleft.colour = self.right.bottomright.colour
        self.right.bottomright.colour = buffer

    def _turnleftinv(self):
        """Performs a left inverted turn"""
        buffer = self.left.topleft.colour
        self.left.topleft.colour = self.left.topright.colour
        self.left.topright.colour = self.left.bottomright.colour
        self.left.bottomright.colour = self.left.bottomleft.colour
        self.left.bottomleft.colour = buffer

        buffer = self.left.top.colour
        self.left.top.colour = self.left.right.colour
        self.left.right.colour = self.left.bottom.colour
        self.left.bottom.colour = self.left.left.colour
        self.left.left.colour = buffer

        buffer = self.up.topleft.colour
        self.up.topleft.colour = self.front.topleft.colour
        self.front.topleft.colour = self.down.bottomleft.colour
        self.down.bottomleft.colour = self.back.bottomleft.colour
        self.back.bottomleft.colour = buffer

        buffer = self.up.left.colour
        self.up.left.colour = self.front.left.colour
        self.front.left.colour = self.down.left.colour
        self.down.left.colour = self.back.left.colour
        self.back.left.colour = buffer

        buffer = self.up.bottomleft.colour
        self.up.bottomleft.colour = self.front.bottomleft.colour
        self.front.bottomleft.colour = self.down.topleft.colour
        self.down.topleft.colour = self.back.topleft.colour
        self.back.topleft.colour = buffer

    def _turndowninv(self):
        """Performs a down inverted turn"""
        buffer = self.down.topleft.colour
        self.down.topleft.colour = self.down.bottomleft.colour
        self.down.bottomleft.colour = self.down.bottomright.colour
        self.down.bottomright.colour = self.down.topright.colour
        self.down.topright.colour = buffer

        buffer = self.down.top.colour
        self.down.top.colour = self.down.left.colour
        self.down.left.colour = self.down.bottom.colour
        self.down.bottom.colour = self.down.right.colour
        self.down.right.colour = buffer

        buffer = self.front.bottomleft.colour
        self.front.bottomleft.colour = self.right.bottomleft.colour
        self.right.bottomleft.colour = self.back.bottomright.colour
        self.back.bottomright.colour = self.left.bottomleft.colour
        self.left.bottomleft.colour = buffer

        buffer = self.front.bottom.colour
        self.front.bottom.colour = self.right.bottom.colour
        self.right.bottom.colour = self.back.bottom.colour
        self.back.bottom.colour = self.left.bottom.colour
        self.left.bottom.colour = buffer

        buffer = self.front.bottomright.colour
        self.front.bottomright.colour = self.right.bottomright.colour
        self.right.bottomright.colour = self.back.bottomleft.colour
        self.back.bottomleft.colour = self.left.bottomright.colour
        self.left.bottomright.colour = buffer

    def _turnxinv(self):
        """Performs an x inverted rotation"""
        self._turnleft()
        self._turnrightinv()

        buffer = self.up.top.colour
        self.up.top.colour = self.back.bottom.colour
        self.back.bottom.colour = self.down.bottom.colour
        self.down.bottom.colour = self.front.top.colour
        self.front.top.colour = buffer

        buffer = self.up.middle.colour
        self.up.middle.colour = self.back.middle.colour
        self.back.middle.colour = self.down.middle.colour
        self.down.middle.colour = self.front.middle.colour
        self.front.middle.colour = buffer

        buffer = self.up.bottom.colour
        self.up.bottom.colour = self.back.top.colour
        self.back.top.colour = self.down.top.colour
        self.down.top.colour = self.front.bottom.colour
        self.front.bottom.colour = buffer

    def _turnyinv(self):
        """Performs a y inverted rotation"""
        self._turnupinv()
        self._turndown()

        buffer = self.front.left.colour
        self.front.left.colour = self.left.left.colour
        self.left.left.colour = self.back.right.colour
        self.back.right.colour = self.right.left.colour
        self.right.left.colour = buffer

        buffer = self.front.middle.colour
        self.front.middle.colour = self.left.middle.colour
        self.left.middle.colour = self.back.middle.colour
        self.back.middle.colour = self.right.middle.colour
        self.right.middle.colour = buffer

        buffer = self.front.right.colour
        self.front.right.colour = self.left.right.colour
        self.left.right.colour = self.back.left.colour
        self.back.left.colour = self.right.right.colour
        self.right.right.colour = buffer

    def _turnzinv(self):
        """Performs a z inverted rotation"""
        self._turnfrontinv()
        self._turnback()

        buffer = self.up.left.colour
        self.up.left.colour = self.right.top.colour
        self.right.top.colour = self.down.right.colour
        self.down.right.colour = self.left.bottom.colour
        self.left.bottom.colour = buffer

        buffer = self.up.middle.colour
        self.up.middle.colour = self.right.middle.colour
        self.right.middle.colour = self.down.middle.colour
        self.down.middle.colour = self.left.middle.colour
        self.left.middle.colour = buffer

        buffer = self.up.right.colour
        self.up.right.colour = self.right.bottom.colour
        self.right.bottom.colour = self.down.left.colour
        self.down.left.colour = self.left.top.colour
        self.left.top.colour = buffer

    def _turn2up(self):
        """Performs 2 up turns"""
        buffer = self.up.topleft.colour
        self.up.topleft.colour = self.up.bottomright.colour
        self.up.bottomright.colour = buffer

        buffer = self.up.top.colour
        self.up.top.colour = self.up.bottom.colour
        self.up.bottom.colour = buffer

        buffer = self.up.topright.colour
        self.up.topright.colour = self.up.bottomleft.colour
        self.up.bottomleft.colour = buffer

        buffer = self.up.right.colour
        self.up.right.colour = self.up.left.colour
        self.up.left.colour = buffer

        buffer = self.front.topleft.colour
        self.front.topleft.colour = self.back.topright.colour
        self.back.topright.colour = buffer

        buffer = self.front.top.colour
        self.front.top.colour = self.back.top.colour
        self.back.top.colour = buffer

        buffer = self.front.topright.colour
        self.front.topright.colour = self.back.topleft.colour
        self.back.topleft.colour = buffer

        buffer = self.right.topleft.colour
        self.right.topleft.colour = self.left.topleft.colour
        self.left.topleft.colour = buffer

        buffer = self.right.top.colour
        self.right.top.colour = self.left.top.colour
        self.left.top.colour = buffer

        buffer = self.right.topright.colour
        self.right.topright.colour = self.left.topright.colour
        self.left.topright.colour = buffer

    def _turn2front(self):
        """Performs 2 front turns"""
        buffer = self.front.topleft.colour
        self.front.topleft.colour = self.front.bottomright.colour
        self.front.bottomright.colour = buffer

        buffer = self.front.top.colour
        self.front.top.colour = self.front.bottom.colour
        self.front.bottom.colour = buffer

        buffer = self.front.topright.colour
        self.front.topright.colour = self.front.bottomleft.colour
        self.front.bottomleft.colour = buffer

        buffer = self.front.right.colour
        self.front.right.colour = self.front.left.colour
        self.front.left.colour = buffer

        buffer = self.up.bottomleft.colour
        self.up.bottomleft.colour = self.down.bottomright.colour
        self.down.bottomright.colour = buffer

        buffer = self.up.bottom.colour
        self.up.bottom.colour = self.down.bottom.colour
        self.down.bottom.colour = buffer

        buffer = self.up.bottomright.colour
        self.up.bottomright.colour = self.down.bottomleft.colour
        self.down.bottomleft.colour = buffer

        buffer = self.right.topleft.colour
        self.right.topleft.colour = self.left.bottomright.colour
        self.left.bottomright.colour = buffer

        buffer = self.right.left.colour
        self.right.left.colour = self.left.right.colour
        self.left.right.colour = buffer

        buffer = self.right.bottomleft.colour
        self.right.bottomleft.colour = self.left.topright.colour
        self.left.topright.colour = buffer

    def _turn2right(self):
        """Performs 2 right turns"""
        buffer = self.right.topleft.colour
        self.right.topleft.colour = self.right.bottomright.colour
        self.right.bottomright.colour = buffer

        buffer = self.right.top.colour
        self.right.top.colour = self.right.bottom.colour
        self.right.bottom.colour = buffer

        buffer = self.right.topright.colour
        self.right.topright.colour = self.right.bottomleft.colour
        self.right.bottomleft.colour = buffer

        buffer = self.right.right.colour
        self.right.right.colour = self.right.left.colour
        self.right.left.colour = buffer

        buffer = self.up.topright.colour
        self.up.topright.colour = self.down.bottomright.colour
        self.down.bottomright.colour = buffer

        buffer = self.up.right.colour
        self.up.right.colour = self.down.right.colour
        self.down.right.colour = buffer

        buffer = self.up.bottomright.colour
        self.up.bottomright.colour = self.down.topright.colour
        self.down.topright.colour = buffer

        buffer = self.front.topright.colour
        self.front.topright.colour = self.back.bottomright.colour
        self.back.bottomright.colour = buffer

        buffer = self.front.right.colour
        self.front.right.colour = self.back.right.colour
        self.back.right.colour = buffer

        buffer = self.front.bottomright.colour
        self.front.bottomright.colour = self.back.topright.colour
        self.back.topright.colour = buffer

    def _turn2back(self):
        """Performs 2 back turns"""
        buffer = self.back.topleft.colour
        self.back.topleft.colour = self.back.bottomright.colour
        self.back.bottomright.colour = buffer

        buffer = self.back.top.colour
        self.back.top.colour = self.back.bottom.colour
        self.back.bottom.colour = buffer

        buffer = self.back.topright.colour
        self.back.topright.colour = self.back.bottomleft.colour
        self.back.bottomleft.colour = buffer

        buffer = self.back.right.colour
        self.back.right.colour = self.back.left.colour
        self.back.left.colour = buffer

        buffer = self.up.topleft.colour
        self.up.topleft.colour = self.down.topright.colour
        self.down.topright.colour = buffer

        buffer = self.up.top.colour
        self.up.top.colour = self.down.top.colour
        self.down.top.colour = buffer

        buffer = self.up.topright.colour
        self.up.topright.colour = self.down.topleft.colour
        self.down.topleft.colour = buffer

        buffer = self.right.topright.colour
        self.right.topright.colour = self.left.bottomleft.colour
        self.left.bottomleft.colour = buffer

        buffer = self.right.right.colour
        self.right.right.colour = self.left.left.colour
        self.left.left.colour = buffer

        buffer = self.right.bottomright.colour
        self.right.bottomright.colour = self.left.topleft.colour
        self.left.topleft.colour = buffer

    def _turn2left(self):
        """Performs 2 left turns"""
        buffer = self.left.topleft.colour
        self.left.topleft.colour = self.left.bottomright.colour
        self.left.bottomright.colour = buffer

        buffer = self.left.top.colour
        self.left.top.colour = self.left.bottom.colour
        self.left.bottom.colour = buffer

        buffer = self.left.topright.colour
        self.left.topright.colour = self.left.bottomleft.colour
        self.left.bottomleft.colour = buffer

        buffer = self.left.right.colour
        self.left.right.colour = self.left.left.colour
        self.left.left.colour = buffer

        buffer = self.up.topleft.colour
        self.up.topleft.colour = self.down.bottomleft.colour
        self.down.bottomleft.colour = buffer

        buffer = self.up.left.colour
        self.up.left.colour = self.down.left.colour
        self.down.left.colour = buffer

        buffer = self.up.bottomleft.colour
        self.up.bottomleft.colour = self.down.topleft.colour
        self.down.topleft.colour = buffer

        buffer = self.front.topleft.colour
        self.front.topleft.colour = self.back.bottomleft.colour
        self.back.bottomleft.colour = buffer

        buffer = self.front.left.colour
        self.front.left.colour = self.back.left.colour
        self.back.left.colour = buffer

        buffer = self.front.bottomleft.colour
        self.front.bottomleft.colour = self.back.topleft.colour
        self.back.topleft.colour = buffer

    def _turn2down(self):
        """Performs 2 down turns"""
        buffer = self.down.topleft.colour
        self.down.topleft.colour = self.down.bottomright.colour
        self.down.bottomright.colour = buffer

        buffer = self.down.top.colour
        self.down.top.colour = self.down.bottom.colour
        self.down.bottom.colour = buffer

        buffer = self.down.topright.colour
        self.down.topright.colour = self.down.bottomleft.colour
        self.down.bottomleft.colour = buffer

        buffer = self.down.right.colour
        self.down.right.colour = self.down.left.colour
        self.down.left.colour = buffer

        buffer = self.front.bottomleft.colour
        self.front.bottomleft.colour = self.back.bottomright.colour
        self.back.bottomright.colour = buffer

        buffer = self.front.bottom.colour
        self.front.bottom.colour = self.back.bottom.colour
        self.back.bottom.colour = buffer

        buffer = self.front.bottomright.colour
        self.front.bottomright.colour = self.back.bottomleft.colour
        self.back.bottomleft.colour = buffer

        buffer = self.right.bottomleft.colour
        self.right.bottomleft.colour = self.left.bottomleft.colour
        self.left.bottomleft.colour = buffer

        buffer = self.right.bottom.colour
        self.right.bottom.colour = self.left.bottom.colour
        self.left.bottom.colour = buffer

        buffer = self.right.bottomright.colour
        self.right.bottomright.colour = self.left.bottomright.colour
        self.left.bottomright.colour = buffer

    def _turn2x(self):
        """Performs 2 x rotations"""
        self._turn2right()
        self._turn2left()

        buffer = self.up.top.colour
        self.up.top.colour = self.down.bottom.colour
        self.down.bottom.colour = buffer

        buffer = self.up.middle.colour
        self.up.middle.colour = self.down.middle.colour
        self.down.middle.colour = buffer

        buffer = self.up.bottom.colour
        self.up.bottom.colour = self.down.top.colour
        self.down.top.colour = buffer

        buffer = self.front.top.colour
        self.front.top.colour = self.back.bottom.colour
        self.back.bottom.colour = buffer

        buffer = self.front.middle.colour
        self.front.middle.colour = self.back.middle.colour
        self.back.middle.colour = buffer

        buffer = self.front.bottom.colour
        self.front.bottom.colour = self.back.top.colour
        self.back.top.colour = buffer

    def _turn2y(self):
        """Performs 2 y rotations"""
        self._turn2up()
        self._turn2down()

        buffer = self.front.left.colour
        self.front.left.colour = self.back.right.colour
        self.back.right.colour = buffer

        buffer = self.front.middle.colour
        self.front.middle.colour = self.back.middle.colour
        self.back.middle.colour = buffer

        buffer = self.front.right.colour
        self.front.right.colour = self.back.left.colour
        self.back.left.colour = buffer

        buffer = self.right.left.colour
        self.right.left.colour = self.left.left.colour
        self.left.left.colour = buffer

        buffer = self.right.middle.colour
        self.right.middle.colour = self.left.middle.colour
        self.left.middle.colour = buffer

        buffer = self.right.right.colour
        self.right.right.colour = self.left.right.colour
        self.left.right.colour = buffer

    def _turn2z(self):
        """Performs 2 z rotations"""
        self._turn2front()
        self._turn2back()

        buffer = self.up.left.colour
        self.up.left.colour = self.down.right.colour
        self.down.right.colour = buffer

        buffer = self.up.middle.colour
        self.up.middle.colour = self.down.middle.colour
        self.down.middle.colour = buffer

        buffer = self.up.right.colour
        self.up.right.colour = self.down.left.colour
        self.down.left.colour = buffer

        buffer = self.right.top.colour
        self.right.top.colour = self.left.bottom.colour
        self.left.bottom.colour = buffer

        buffer = self.right.middle.colour
        self.right.middle.colour = self.left.middle.colour
        self.left.middle.colour = buffer

        buffer = self.right.bottom.colour
        self.right.bottom.colour = self.left.top.colour
        self.left.top.colour = buffer
