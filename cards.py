from random import shuffle
from math import floor


class Card:

    def __init__(self, number):
        ranks = ['A ', '2 ', '3 ', '4 ', '5 ', '6 ', 
                 '7 ', '8 ', '9 ', '10', 'J ', 'Q ', 'K ']
        suits = ['s', 'c', 'h', 'd']

        self._rank = (number - 1) % 13 + 1
        self._suit = suits[floor((number - 1)/ 13)]
        self._str = ranks[self._rank - 1] + self._suit
        self._color = 'red' if number > 26 else 'black'


    def __str__(self):
        return self._str


    @property
    def rank(self):
        return self._rank


    @property
    def suit(self):
        return self._suit

    
    @property
    def color(self):
        return self._color


class FreeCellBoard:

    def __init__(self):
        self._matrix = [[None for x in range(8)] for y in range(20)]
        cards = [Card(n + 1) for n in range(52)]
        shuffle(cards)
        for i in range(52):
            self._matrix[floor(i / 8) + 1][i % 8] = cards[i]


    def card_at(self, row, col):
        return self._matrix[row][col]


    def has_card(self, row, col):
        return self._matrix[row][col] is not None
    

    def last_row_with_card(self, col):
        row = 19

        while self._matrix[row][col] is None and row > 0:
            row -= 1
        
        return row


    def first_empty_row(self, col):
        result = self.last_row_with_card(col) + 1
        return result if result < 20 else 19


    def is_freecell(self, row, col):
        return row == 0 and col < 4


    def is_rank_pile(self, row, col):
        return row == 0 and col >= 4


    def can_move_from(self, row, col):
        return (self.has_card(row, col) and 
                (self.is_freecell(row, col) or self.last_row_with_card(col) == row))


    def can_move_to(self, card, dest_row, dest_col):

        if self.is_freecell(dest_row, dest_col):
            return not self.has_card(dest_row, dest_col)

        if self.is_rank_pile(dest_row, dest_col):
            if not self.has_card(dest_row, dest_col):
                return card.rank == 1
            dest_card = self._matrix[dest_row][dest_col]
            return card.rank == dest_card.rank + 1 and card.suit == dest_card.suit

        if self.last_row_with_card(dest_col) == dest_row - 1:
            if dest_row == 1:
                return True
            dest_card = self._matrix[dest_row - 1][dest_col]
            return dest_card.rank == card.rank + 1 and dest_card.color != card.color

        return False


    def move(self, src_row, src_col, dest_row, dest_col):
        if (self.can_move_from(src_row, src_col) and 
                self.can_move_to(self._matrix[src_row][src_col], dest_row, dest_col)):
            self._matrix[dest_row][dest_col] = self._matrix[src_row][src_col]
            self._matrix[src_row][src_col] = None
