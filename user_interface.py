#!/usr/bin/env python3


def say_welcome():
    """print welcome information"""
    print_message("Welcome to Switch v1.1")


def print_game_menu():
    """tell user of the menu options"""
    print("\nPlease select from one of the following options: [1-2]")
    print("1 - New Game")
    print("2 - Exit")


def print_player_info(player, top_card, hands):
    """Prints the info of the current players turn such as his/her hand

    --Parameters:
        Current player, the top card of the discard pile, each players hands sizes

    """
    print("\nHANDS: " + str(hands))
    print("PLAYER: " + player.name)
    if not player.is_ai:
        print('HAND: ' + ', '.join(str(card) for card in player.hand))
    print('TOP CARD: ' + str(top_card))


def print_discard_result(discarded, card):
    """This outputs the information of which card was discarded and allow them to track the games history

    Parameters:
        Boolean if the card was able to be discarded
        The card being discarded
        """
    if discarded:
        print("Discarded: " + str(card) + "\n")
    else:
        print("Unable to discard card: " + str(card))


def print_winner_of_game(player):
    """print winner information

    --Parameters
            Winning player

    """
    print_message('\n'+80*'-')
    print_message("Woohoo!!! Winner of the game is: " + player.name)
    print_message(80*'-')


def say_goodbye():
    """say goodbye to my little friend"""
    print_message("Goodbye!")


def print_message(msg):
    """takes an argument and outputs it

    Parameters:
        Any printable object to be output to the Player.
    """
    print(msg)


# helper method for get_int_input method
def convert_to_int(string):
    """converts string to int

    --parameters: takes a string

    --returns the given string if possible as an integer or -1 to represent failure to do so
    """
    result = -1
    try:
        result = int(string)
    except Exception:
        pass
    return result


# methods get information from user
def get_int_input(min, max):
    """get int value from user

    --parameters: takes a minimum integer and a maximum integer

    if the given value is not less than maximum and greater than minimum or is not an integer we ask for an int again.

    --returns:
      the given integer value the user gives

    """
    choice = -1
    while choice < min or choice > max:
        print("> ", end="")
        choice = convert_to_int(input())
        if choice < min or choice > max:
            print(f"Try again: Input should be an integer between [{min:d}-{max:d}]")
    return choice


def get_string_input():
    """get word from user

    --returns:
     the string a user gives"""
    print("> ", end="")
    s = input()
    return s


def get_player_information(MAX_PLAYERS):
    """get player information

    Parameters:
        Max platers the game can take
    Returns:
        A list of player names

    """
    import random
    from players import Player, SimpleAI, SmartAI

    # create players list
    players = []
    # how many human players?
    print("\nHow many human players [1-4]:")
    no_of_players = get_int_input(1, MAX_PLAYERS)
    # for each player, get name
    for i in range(no_of_players):
        print("Please enter the name of player " + str(i + 1) + ":")
        players.append(Player(get_string_input()))

    ai_names = ['Angela', 'Bart', 'Charly', 'Dorothy']

    # how many AI players? ensure there are at least 2 players
    min = 1 if (len(players) == 1) else 0
    max = MAX_PLAYERS - no_of_players
    if not no_of_players==MAX_PLAYERS:
        print(f"\nHow many ai players [{min:d}-{max:d}]:")
        no_of_players = get_int_input(min, max)
        # for each ai player, get name
        for name in ai_names[:no_of_players]:
            if random.choice([True, False]):
                players.append(SimpleAI(name))
            else:
                players.append(SmartAI("Smart "+name))

    return players


def select_card(cards):
    """select card from hand

    parameters:
    A list of cards the player is able to discard to fit the top card.

    Returns:
        A the card the user has chosen to discard

    """
    print(f"Please select from one of the following cards: [1-{len(cards):d}]")
    for i, card in enumerate(cards, 1):
        print(str(i) + " - " + str(card))

    # get choice
    choice = get_int_input(0, len(cards))
    # get card
    if choice == 0:
        return None
    return cards[choice - 1]


def select_player(players):
    """select other player

    Parameters:
        The players in the game
    Returns:
        The chosen player

    """
    print(f"Please select from one of the following players: [1-{len(players):d}]")
    # print out for each player in players
    for i in range(len(players)):
        p = players[i]
        print(f"{i + 1:d} - {p.name}={len(p.hand):d}")

    # get choice
    choice = get_int_input(1, len(players))
    # get player
    return players[choice - 1]
