#!/usr/bin/python3

"""
Part 1:
Sort this list by the length of the string, then alphabetical order (case-
insensitive).  For example, a correctly sorted list might be:
    a
    D
    z
    vb
    afd
"""
import functools

data = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipisicing', 'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore', 'et']

def sortedData():
    def compare(a, b):
        #TODO: Fill in this function
        return -1 if a < b else 1 if a > b else 0

    return sorted(data, key=functools.cmp_to_key(compare))


"""
Part 2: Write a small, reasonably efficient class that takes strings as input, and calls
a callback method whenever a newline ('\n') is reached, passing in the previous line's
text.  The class should discard old data when possible to save memory.

Hint: This should not take more than about 15-50 lines of code.
"""
class Parser:

    def __init__(self, callback):
        self.callback = callback

    def read(self, data):
        #TODO: Fill in this function
        self.callback(data)


"""
Part 3: Implement the following game.

This game is played on a rectangular grid. At the beginning of the game, each space on
the board is filled in with a random piece, chosen from a predefined set of possible
types of pieces. The player selects a location on the board where there are at least
two of the same type of piece adjacent to each other (vertically or horizontally), and
the selected piece and all connected pieces of the same type are removed from the board,
at which time pieces above them (if any) fall down to take their place.

For example, if the user selected the middle space of the following board:

x o x
o o o
x x x

the result would be this

x   x
x x x

since all the connected o's were removed. The user could then select any of the x's, and
the entire board would be cleared, since the x's are all connected.

On the following board, there are no legal moves, since there are no connected pieces of
the same type. At this point, the game is over:

o x o
x o x

The user gets points based on how many pieces he removes at a time. Each piece removed in
a single move is worth one more point than the last piece. So for example,

1 piece = 1 point
2 pieces = 1 + 2 = 3 points
3 pieces = 1 + 2 + 3 = 6 points

and so on. When there are no longer any legal moves, you deduct points for remaining pieces:

1 piece left = -1 point
2 pieces left = -1 - 2 = -3 points
3 pieces left = -1 - 2 - 3 = -6 points

and so on. When the game is over, you should display the final score to the user and exit.

A skeleton class for the game is already prepared for you. The board is a simple rectangular
array of integers indexing into the pieceTypes array, with 0 representing a blank space.
The play() function currently loops forever, asking the user for a move (it guarantees the
space entered is on the board), clearing the space they entered, and re-drawing the board.
You should replace this logic with the correct logic described above.

Time permitting, you may write an AI that plays the game automatically, trying to get the
highest possible score.
"""
import random

class Game:

    def __init__(self):
        self.pieceTypes = [' ', 'o', 'x', '$']
        self.width = 8
        self.height = 8
        self.board = [[random.randrange(1, len(self.pieceTypes)) for _ in range(self.width)] for _ in range(self.height)]
        self.score = 0

    def getMoveInput(self):
        try:
            a, b = input()
        except ValueError:
            print('Move format should be like: b4')
            return self.getMoveInput()
        else:
            x = max(min(ord(a) - ord('a'), self.width-1), 0)
            y = max(min(ord(b) - ord('1'), self.height-1), 0)
            return x, y

    def render(self):
        print('  ' + ' '.join(chr(ord('a') + i) for i in range(self.width)))
        for j in range(self.height):
            print(str(j+1) + ' ' + ' '.join(self.pieceTypes[self.board[i][j]] for i in range(self.width)))
        print('Current score: {}\n'.format(self.score))

    def play(self):
        while True:
            self.render()

            x, y = self.getMoveInput()
            self.board[x][y] = 0


if __name__ == '__main__':
    print('Part 1:')
    for s in sortedData():
        print(s)
    print('\n')

    print('Part 2:')
    def print_(str):
        print(str.replace('\n', ' '))
    parser = Parser(print_)
    parser.read('This is t')
    parser.read('he first l')
    parser.read('ine.\nAnd this is the second.\n')
    parser.read('And this is the third.\nAnd the')
    parser.read(' fourth.\n')
    print('\n')

    print('Part 3:')
    Game().play()
