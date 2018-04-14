from asciimatics.screen import Screen
from random import shuffle
from math import floor

from cards import *

RED = Screen.COLOUR_RED
BLACK = Screen.COLOUR_BLACK
WHITE = Screen.COLOUR_WHITE
GREEN = Screen.COLOUR_GREEN

KEY_MAP = {ord('a'): (1, 0),
           ord('s'): (1, 1),
           ord('d'): (1, 2),
           ord('f'): (1, 3),
           ord('j'): (1, 4),
           ord('k'): (1, 5),
           ord('l'): (1, 6),
           ord(';'): (1, 7),
           ord('q'): (0, 0),
           ord('w'): (0, 1),
           ord('e'): (0, 2),
           ord('r'): (0, 3),
           ord('u'): (0, 4),
           ord('i'): (0, 5),
           ord('o'): (0, 6),
           ord('p'): (0, 7)}

selected = None


def print_horizontal_divider(screen, row):
    screen.print_at(
            '+---' * 8 + '+',
            0, row, 
            colour=GREEN, bg=BLACK)


def print_divider(screen, row, col):
    screen.print_at(
        '|', col, row,
        colour=GREEN, bg=BLACK)


def print_card(screen, card, row, col):
    if card is not None:
        screen.print_at(
            str(card),
            col + 1, row,
            colour=get_color(card), bg=BLACK)
    else:
        screen.print_at(
                '   ',
                col + 1, row,
                colour=WHITE, bg=BLACK)


def get_color(card):
    return RED if card.color == 'red' else WHITE


def handle_move(board, position):
    global selected
    if selected is not None:
        if position[0] == 0:
            board.move(selected[0], selected[1], position[0], position[1])
        else:
            board.move(selected[0], selected[1], board.first_empty_row(position[1]), position[1])
        selected = None
    else:
        if board.is_freecell(position[0], position[1]):
            selected = position
        else:
            selected = (board.last_row_with_card(position[1]), position[1])


def display(screen):
    while True:
        print_horizontal_divider(screen, 0)

        for col in range(8):
            print_card(screen, matrix.card_at(0, col), 1, col * 4)
            print_divider(screen, 1, col * 4)

        print_horizontal_divider(screen, 2)


        for row in range(1,20):
            for col in range(8):
                print_card(screen, matrix.card_at(row, col), row + 2, col * 4)
                print_divider(screen, row + 2, col * 4)
            print_divider(screen, row + 2, 8 * 4)

        if selected is not None:
            if selected[0] == 0:
                row = 1
            else:
                row = selected[0] + 2
            screen.print_at('   ', selected[1] * 4 + 1, row, colour=BLACK, bg=WHITE)

        print_divider(screen, 1, 8 * 4)

        print_horizontal_divider(screen, 22)

        ev = screen.get_key()

        if ev in KEY_MAP:
            handle_move(matrix, KEY_MAP[ev])

        screen.refresh()

                        
if __name__ == '__main__':
    matrix = FreeCellBoard()
    Screen.wrapper(display)
