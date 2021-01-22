from unittest.mock import patch

import user_interface
from user_interface import *
from cards import Card
from players import *


def test_convert_to_int():
    """Test if a string is converted to int if it is valid"""
    assert -1 == convert_to_int("a")
    assert 1 == convert_to_int("1")


def test_get_int_input():
    """Test if a string input is converted to int if it is valid"""
    choice = "1"
    assert choice.isdigit()
    assert not isinstance(choice, int)
    with patch("builtins.input", return_value=choice):
        assert get_int_input(0, 4) != choice
        assert get_int_input(0, 4) == convert_to_int(choice)


def test_get_string_input():
    """Test if a string input is of string type"""
    return_value = "1"
    assert isinstance(return_value, str)
    with patch("builtins.input", return_value=return_value):
        assert get_string_input() == return_value


def player_info_input_helper(func_input):
    """Helper function that returns player_info based on iterable input"""
    with patch("builtins.input", side_effect=func_input):
        player_info = get_player_information(4)

    return player_info


def test_get_player_information():
    """Test if get player information returns correct player type and name"""

    # Determine final name of AI based on type
    def get_smart_name(typ, name):
        if typ == "smart":
            return f"Smart {name}"
        else:
            return name

    # Build all possible AI names
    ai_names = ['Angela', 'Bart', 'Charly', 'Dorothy']
    ai_possible_players = [(typ, get_smart_name(typ, name)) for typ in ("smart", "simple") for name in ai_names]

    # Generate player_info list with 1 human player and 1 AI
    func_input = [1, "Joe", 1]
    player_info = player_info_input_helper(func_input)
    assert player_info[0] == ("human", "Joe")

    # test if AI info is valid
    for i in range(func_input[0], func_input[-1] + 1):
        assert player_info[i] in ai_possible_players

    # Generate player_info list with 2 human players and 1 AI
    func_input = [2, "Joe", "Eli", 1]
    player_info = player_info_input_helper(func_input)
    assert player_info[0] == ("human", "Joe")
    assert player_info[1] == ("human", "Eli")

    # test if AI info is valid
    for i in range(2, func_input[-1] + 1):
        assert player_info[i] in ai_possible_players


def test_select_card():
    """Test if input returns correct card from select card"""
    deck = [Card("♢", "A"), Card("♢", "K")]
    choice = 1
    with patch("user_interface.get_int_input", return_value=choice):
        assert select_card(deck) == deck[choice-1]

    # Check if player can draw voluntarily and that it returns None
    deck = []
    choice = 1
    with patch("user_interface.get_int_input", return_value=choice):
        assert not select_card(deck)


def test_select_player():
    """Test if input returns correct player in select_player"""
    players = [Player("Joe"), SimpleAI("Angela"), SmartAI("Bart")]
    choice = 2
    with patch("user_interface.get_int_input", return_value=choice):
        assert select_player(players) == players[choice-1]
