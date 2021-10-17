"""Card object for the switch game"""
from collections import namedtuple


class Card(namedtuple('CardData', ['suit', 'value'])):
    """A switch card

    A Card is a namedtuple with the fields 'suit' and 'value'.

    suits -- possible suits for a card
    values -- possible values for a card
    """
    suits = '♣ ♢ ♡ ♠'.split()
    values = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __new__(cls, suit, value):
        assert suit in cls.suits    # check if suit is valid
        assert value in cls.values  # check if value is valid
        return super().__new__(cls, suit, value)    # construct object with valid suit and value

    def __str__(self):
        return '{} {}'.format(self.suit, self.value)


def generate_deck():
    """Deck - set of cards

    Generate deck with 52 unique cards
    """
    return [Card(suit, value)
            for suit in Card.suits for value in Card.values]
