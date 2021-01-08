from cards import *

VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['♣', '♢', '♡', '♠']


def test_generate_deck_length():
    """Test if the correct length of deck is generated"""
    assert 52 == len(generate_deck())


def test_unique_cards__generate_deck():
    """Test if all the cards are unique when deck is generated"""
    deck = generate_deck()
    assert len(deck) == len(set(deck))


def test_suits_count__generate_deck():
    """Test if all suits occur exactly 13 times in a deck"""
    deck = generate_deck()
    suit_count = {suit: 0 for suit in SUITS}

    for card in deck:
        suit_count[card.suit] += 1

    assert all([13 == i for i in suit_count.values()])


def test_values_count__generate_deck():
    """Test if all the values occur exactly 4 times in a deck"""
    deck = generate_deck()
    value_count = {value: 0 for value in VALUES}

    for card in deck:
        value_count[card.value] += 1

    assert all([4 == i for i in value_count.values()])






