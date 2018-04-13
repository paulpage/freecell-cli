from asciimatics.screen import Screen
from random import shuffle
from math import floor

def get_new_matrix():
    matrix = [[0 for x in range(8)] for y in range(20)]
    cards = [x + 1 for x in range(52)]
    shuffle(cards)
    for i in range(52):
        matrix[floor(i / 8) + 1][i % 8] = cards[i]
    return matrix


def get_string(card_number):
    if card_number == 0:
        return '   '
    ranks = ['A ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', 'J ', 'Q ', 'K ']
    suits = ['S', 'C', 'H', 'D']

    rank = ranks[(card_number - 1) % 13]
    suit = suits[floor((card_number - 1)/ 13)]

    return rank + suit

def get_colour(card_number):
    return Screen.COLOUR_RED if card_number > 26 else Screen.COLOUR_BLACK


def display(screen):
    while True:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                screen.print_at(get_string(matrix[row][col]),
                        col * 4, row, 
                        #colour=get_colour(matrix[x][y]),
                        colour=Screen.COLOUR_GREEN,
                        bg=Screen.COLOUR_WHITE)
        screen.refresh()

                        
matrix = get_new_matrix()

Screen.wrapper(display)
