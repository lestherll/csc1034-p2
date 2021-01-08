"""command line interfacce for the switch game"""
import random


def print_message(msg):
    """print a generic message"""
    print(msg)


def say_welcome():
    """print welcome information"""
    print_message("Welcome to Switch v1.1")


def print_game_menu():
    """display game menu"""
    print("\nPlease select from one of the following options: [1-2]")
    print("1 - New Game")
    print("2 - Exit")


def print_player_info(player, top_card, hands):
    """display player information and public game state"""
    print(f"\nHANDS: {hands}")
    print(f"PLAYER: {player.name}")
    if not player.is_ai:
        print("HAND: " + ", ".join(str(card) for card in player.hand))
    print(f"TOP CARD: {top_card}")


def print_discard_result(discarded, card):
    """display a discard message"""
    if discarded:
        print(f"Discarded: {card}\n")
    else:
        print(f"Unable to discard card: {card}")


def print_winner_of_game(player):
    """display winner information"""
    print_message('\n'+80*'-')
    print_message(f"Woohoo!!! Winner of the game is: {player.name}")
    print_message(80*'-')


def say_goodbye():
    """say goodbye to my little friend"""
    print_message("Goodbye!")


def convert_to_int(string):
    """converts string to int"""
    result = -1
    try:
        result = int(string)
    except ValueError:
        pass
    return result


def get_int_input(min_val, max_val):
    """get int value from user"""
    choice = -1
    while choice < min_val or choice > max_val:
        print("> ", end="")
        choice = convert_to_int(input())
        if choice < min_val or choice > max_val:
            print(f"Try again: Input should be an integer between [{min_val:d}-{max_val:d}]")
    return choice


def get_string_input():
    """get word from user"""
    print("> ", end="")
    return input()


def get_player_information(max_players):
    """get required information to set up a round"""

    # create players list
    player_info = []
    # how many human players?
    print("\nHow many human players [1-4]:")
    no_of_players = get_int_input(1, max_players)

    # for each player, get name
    for i in range(no_of_players):
        print(f"Please enter the name of player {i+1}:")
        player_info.append(('human', get_string_input()))

    ai_names = ['Angela', 'Bart', 'Charly', 'Dorothy']

    # how many AI players? ensure there are at least 2 players
    min_val = 1 if (len(player_info) == 0) else 0
    max_val = max_players - no_of_players

    if max_val != 0:
        print(f"\nHow many ai players [{min_val:d}-{max_val:d}]:")
        no_of_players = get_int_input(min_val, max_val)

    # randomly assign a simple or smart AI for each computer strategy
    for name in ai_names[:no_of_players]:
        if random.choice([True, False]):
            player_info.append(('simple', name))
        else:
            player_info.append(('smart', f"Smart {name}"))

    return player_info


def select_card(cards):
    """select card from hand"""
    print(f"Please select from one of the following cards: [1-{len(cards):d}]")
    for i in range(len(cards)):
        card = cards[i]
        print(f"{i+1} - {card}")

    # get choice
    choice = get_int_input(1, len(cards))
    # get card
    return cards[choice-1] if choice else None


def select_player(players):
    """select other player"""
    print(f"Please select from one of the following players: [1-{len(players):d}]")
    # print out for each player in players
    for idx, player in enumerate(players):
        print(f"{idx + 1:d} - {player.name} = {len(player.hand):d}")

    # get choice
    choice = get_int_input(1, len(players))
    # get player
    return players[choice - 1]
