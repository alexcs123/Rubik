# Rubik

Create a new cube by calling ```Cube()```, and optioanlly specify its starting
state with either ```States.scrambled``` or ```States.solved``` (default).
Call ```state()``` to check the current state of a cube, and ```scramble``` to
scramble the cube, optionally specifying the number of turns to perform the
scramble (default is 100). Perform turns on the cube by calling ```turn()```,
and providing your turns as a space delimited string. Allowed turns are:

* ```u``` - Perfrom an 'up' turn
* ```d``` - Perform a 'down' turn
* ```f``` - Perform a 'front' turn
* ```b``` - Perform a 'back' turn
* ```l``` - Perform a 'left' turn
* ```r``` - Perform a 'right' turn
* ```x``` - Rotate the entire cube around the x axis
* ```y``` - Rotate the entire cube around the y axis
* ```z``` - Rotate the entire cube around the z axis

Additionally, 'inverted' (counter-clockwise) turns can be performed by adding an
```i``` after the turn notation (e.g. ```ri```, ```di```, ```yi```). A double
turn can also be performed by adding a ```2``` before the turn notation (e.g
```2u```, ```2f```, ```2x```). Cubes have six sides:

* ```up```
* ```down```
* ```front```
* ```back```
* ```left```
* ```right```

Each side has 9 pieces:

* ```top```
* ```topleft```
* ```topright```
* ```middle```
* ```left```
* ```right```
* ```bottom```
* ```bottomleft```
* ```bottomright```

The colour of a particular piece can be found by returning its ```colour```
variable (e.g. ```cube.front.topright.colour```). The colour of a side, as
designated by the colour of the middle piece, can be found by calling
```colour()``` on that side (e.g. ```cube.up.colour()```). When a cube has
been scrambled, the string of turns performed during the scramble can be
found by returning its ```shuffles``` variable. There is also a ```time```
variable, which can be used to store the solve time of a cube by the user.

As well as a ```solve()``` algorithm, ```main.py``` contains a ```repeat```
algorithm that, given a string of turns, will return the number of times that
string of turns must be performed in order for the cube to return to its
initial state. For example, the string of turns ```'ri di r d'``` must be
repeated ```6``` times for the cube to return to the state it assumed before
any turns were made.
