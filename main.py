from classes.Cube import Cube, States


def solve(c):
    """Solves given cube"""
    up = c.up.colour()

    while c.up.top.colour != up or c.up.right.colour != up or c.up.bottom.colour != up or c.up.left.colour != up or c.front.top.colour != c.front.colour() or c.right.top.colour != c.right.colour() or c.back.top.colour != c.back.colour() or c.left.top.colour != c.left.colour():
        check = c.up.bottom.colour
        match = c.front.top.colour

        if check == up and match == c.right.colour():
            c.turn('2f d 2r')
        elif check == up and match == c.back.colour():
            c.turn('2f 2d 2b')
        elif check == up and match == c.left.colour():
            c.turn('2f di 2l')

        check = c.front.top.colour
        match = c.up.bottom.colour

        if check == up and match == c.front.colour():
            c.turn('f ri di r 2f')
        elif check == up and match == c.right.colour():
            c.turn('f r')
        elif check == up and match == c.back.colour():
            c.turn('f ri d r 2b')
        elif check == up and match == c.left.colour():
            c.turn('fi l')

        check = c.front.right.colour
        match = c.right.left.colour

        if check == up and match == c.front.colour():
            c.turn('ri di r 2f')
        elif check == up and match == c.right.colour():
            c.turn('r')
        elif check == up and match == c.back.colour():
            c.turn('ri d r 2b')
        elif check == up and match == c.left.colour():
            c.turn('ri 2d 2l')

        check = c.right.left.colour
        match = c.front.right.colour

        if check == up and match == c.front.colour():
            c.turn('fi')
        elif check == up and match == c.right.colour():
            c.turn('f d fi 2r')
        elif check == up and match == c.back.colour():
            c.turn('f 2d fi 2b')
        elif check == up and match == c.left.colour():
            c.turn('f di fi 2l')

        check = c.front.bottom.colour
        match = c.down.bottom.colour

        if check == up and match == c.front.colour():
            c.turn('ri d r fi')
        elif check == up and match == c.right.colour():
            c.turn('fi r f')
        elif check == up and match == c.back.colour():
            c.turn('d ri b r')
        elif check == up and match == c.left.colour():
            c.turn('f li fi')

        check = c.down.bottom.colour
        match = c.front.bottom.colour

        if check == up and match == c.front.colour():
            c.turn('2f')
        elif check == up and match == c.right.colour():
            c.turn('d 2r')
        elif check == up and match == c.back.colour():
            c.turn('2d 2b')
        elif check == up and match == c.left.colour():
            c.turn('di 2l')

        c.turn('y')

    while c.up.topleft.colour != up or c.up.topright.colour != up or c.up.bottomright.colour != up or c.up.bottomleft.colour != up or c.front.topright.colour != c.front.colour() or c.right.topright.colour != c.right.colour() or c.back.topleft.colour != c.back.colour() or c.left.topright.colour != c.left.colour():
        check = c.up.bottomright.colour
        match = c.front.topright.colour

        if check == up and match == c.right.colour():
            c.turn('ri di r d bi di b')
        elif check == up and match == c.back.colour():
            c.turn('ri di r 2d li di l')
        elif check == up and match == c.left.colour():
            c.turn('ri di r di fi di f')

        check = c.front.topright.colour
        match = c.right.topleft.colour

        if check == up and match == c.front.colour():
            c.turn('ri d r di ri d r')
        elif check == up and match == c.right.colour():
            c.turn('ri d r bi d b')
        elif check == up and match == c.back.colour():
            c.turn('ri d r d li d l')
        elif check == up and match == c.left.colour():
            c.turn('ri d r 2d fi d f')

        check = c.front.bottomright.colour
        match = c.down.bottomright.colour

        if check == up and match == c.front.colour():
            c.turn('di ri d r')
        elif check == up and match == c.right.colour():
            c.turn('bi d b')
        elif check == up and match == c.back.colour():
            c.turn('d li d l')
        elif check == up and match == c.left.colour():
            c.turn('2d fi d f')

        check = c.right.topleft.colour
        match = c.up.bottomright.colour

        if check == up and match == c.front.colour():
            c.turn('ri di r d ri di r')
        elif check == up and match == c.right.colour():
            c.turn('ri di r 2d bi di b')
        elif check == up and match == c.back.colour():
            c.turn('ri di r di li di l')
        elif check == up and match == c.left.colour():
            c.turn('ri di r fi di f')

        check = c.right.bottomleft.colour
        match = c.front.bottomright.colour

        if check == up and match == c.front.colour():
            c.turn('ri di r')
        elif check == up and match == c.right.colour():
            c.turn('d bi di b')
        elif check == up and match == c.back.colour():
            c.turn('2d li di l')
        elif check == up and match == c.left.colour():
            c.turn('di fi di f')

        check = c.down.bottomright.colour
        match = c.right.bottomleft.colour

        if check == up and match == c.front.colour():
            c.turn('ri 2d r d ri di r')
        elif check == up and match == c.right.colour():
            c.turn('d bi 2d b d bi di b')
        elif check == up and match == c.back.colour():
            c.turn('2d li 2d l d li di l')
        elif check == up and match == c.left.colour():
            c.turn('di fi 2d f d fi di f')

        c.turn('y')

    c.turn('2x')

    while c.front.left.colour != c.front.colour() or c.front.right.colour != c.front.colour() or c.right.left.colour != c.right.colour() or c.right.right.colour != c.right.colour() or c.back.left.colour != c.back.colour() or c.back.right.colour != c.back.colour() or c.left.left.colour != c.left.colour() or c.left.right.colour != c.left.colour():
        one = c.up.bottom.colour
        two = c.front.top.colour

        if one == c.left.colour() and two == c.front.colour():
            c.turn('ui li u l u f ui fi')
        elif one == c.front.colour() and two == c.left.colour():
            c.turn('2u f ui fi ui li u l')
        elif one == c.front.colour() and two == c.right.colour():
            c.turn('2u fi u f u r ui ri')
        elif one == c.right.colour() and two == c.front.colour():
            c.turn('u r ui ri ui fi u f')
        elif one == c.right.colour() and two == c.back.colour():
            c.turn('u ri u r u b ui bi')
        elif one == c.back.colour() and two == c.right.colour():
            c.turn('b ui bi ui ri u r')
        elif one == c.back.colour() and two == c.left.colour():
            c.turn('bi u b u l ui li')
        elif one == c.left.colour() and two == c.back.colour():
            c.turn('ui l ui li ui bi u b')

        one = c.front.right.colour
        two = c.right.left.colour

        if one == c.left.colour() and two == c.front.colour():
            c.turn('u r ui ri ui fi u f u li u l u f ui fi')
        elif one == c.front.colour() and two == c.left.colour():
            c.turn('u r ui ri ui fi u 2f ui fi ui li u l')
        elif one == c.right.colour() and two == c.front.colour():
            c.turn('u r ui ri ui fi u f ui r ui ri ui fi u f')
        elif one == c.right.colour() and two == c.back.colour():
            c.turn('u r ui ri ui fi u f ui ri u r u b ui bi')
        elif one == c.back.colour() and two == c.right.colour():
            c.turn('u r ui ri ui fi u f 2u b ui bi ui ri u r')
        elif one == c.back.colour() and two == c.left.colour():
            c.turn('u r ui ri ui fi u f 2u bi u b u l ui li')
        elif one == c.left.colour() and two == c.back.colour():
            c.turn('u r ui ri ui fi u 2f ui fi ui li u l')

        c.turn('y')

    up = c.up.colour()

    if c.up.top.colour == up and c.up.right.colour == up and c.up.bottom.colour == up:
        pass
    elif c.up.top.colour != up and c.up.right.colour != up and c.up.bottom.colour != up:
        c.turn('f r u ri ui fi 2y f r u ri ui r u ri ui fi')
    elif c.up.left.colour == up and c.up.right.colour == up:
        c.turn('f r u ri ui fi')
    elif c.up.top.colour == up and c.up.bottom.colour == up:
        c.turn('y f r u ri ui fi')
    else:
        if c.up.left.colour == up and c.up.top.colour == up:
            c.turn('f r u ri ui r u ri ui fi')
        elif c.up.top.colour == up and c.up.right.colour == up:
            c.turn('yi f r u ri ui r u ri ui fi')
        elif c.up.right.colour == up and c.up.bottom.colour == up:
            c.turn('2y f r u ri ui r u ri ui fi')
        elif c.up.bottom.colour == up and c.up.left.colour == up:
            c.turn('y f r u ri ui r u ri ui fi')

    while c.front.top.colour != c.front.colour() or c.right.top.colour != c.right.colour() or c.back.top.colour != c.back.colour() or c.left.top.colour != c.left.colour():
        if c.front.top.colour == c.front.colour() and c.right.top.colour == c.right.colour():
            c.turn('yi r u ri u r 2u ri u')
        elif c.right.top.colour == c.right.colour() and c.back.top.colour == c.back.colour():
            c.turn('r u ri u r 2u ri u')
        elif c.back.top.colour == c.back.colour() and c.left.top.colour == c.left.colour():
            c.turn('y r u ri u r 2u ri u')
        elif c.left.top.colour == c.left.colour() and c.front.top.colour == c.front.colour():
            c.turn('2y r u ri u r 2u ri u')
        elif c.front.top.colour == c.front.colour() and c.back.top.colour == c.back.colour():
            c.turn('r u ri u r 2u ri yi r u ri u r 2u ri u')
        elif c.left.top.colour == c.left.colour() and c.right.top.colour == c.right.colour():
            c.turn('y r u ri u r 2u ri yi r u ri u r 2u ri u')

        c.turn('u')

    while not ((c.left.topright.colour == c.left.colour() and c.front.topleft.colour == c.front.colour() or c.up.bottomleft.colour == c.left.colour() and c.left.topright.colour == c.front.colour() or c.front.topleft.colour == c.left.colour() and c.up.bottomleft.colour == c.front.colour()) and (c.front.topright.colour == c.front.colour() and c.right.topleft.colour == c.right.colour() or c.up.bottomright.colour == c.front.colour() and c.front.topright.colour == c.right.colour() or c.right.topleft.colour == c.front.colour() and c.up.bottomright.colour == c.right.colour())):
        for i in range(4):
            if c.front.topright.colour == c.front.colour() and c.right.topleft.colour == c.right.colour() or c.up.bottomright.colour == c.front.colour() and c.front.topright.colour == c.right.colour() or c.right.topleft.colour == c.front.colour() and c.up.bottomright.colour == c.right.colour():
                break

            c.turn('y')

        c.turn('u r ui li u ri ui l')

    while c.state() != States.solved:
        while c.up.bottomright.colour != c.up.colour():
            c.turn('ri di r d')

        c.turn('ui')

    return c


def repeats(turns):
    """Returns number of times a sequence must be repeated to return to original state"""
    c = Cube()
    c.turn(turns)
    repeats = 1

    while c.state() != States.solved:
        c.turn(turns)
        repeats += 1

    return repeats


if __name__ == '__main__':
    print(solve(Cube(States.scrambled)).state().name)

    print(repeats('u z'))
