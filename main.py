import sys
from enum import Enum

class Sign(Enum):
    SCISSORS: int = 1
    PAPER: int = 2
    ROCK: int = 3
    LIZARD: int = 4
    SPOCK: int = 5

# List of possible hands
WINNERS = [
    { "hands": (Sign.SCISSORS, Sign.PAPER), "winner": Sign.SCISSORS }
    { "hands": (Sign.PAPER, Sign.ROCK), "winner": Sign.PAPER }
    { "hands": (Sign.ROCK, Sign.LIZARD), "winner": Sign.ROCK }
    { "hands": (Sign.LIZARD, Sign.SPOCK), "winner": Sign.LIZARD }
    { "hands": (Sign.SPOCK, Sign.SCISSORS), "winner": Sign.SPOCK }
    { "hands": (Sign.SCISSORS, Sign.LIZARD), "winner": Sign.SCISSORS }
    { "hands": (Sign.LIZARD, Sign.PAPER), "winner": Sign.LIZARD }
    { "hands": (Sign.PAPER, Sign.SPOCK), "winner": Sign.PAPER }
    { "hands": (Sign.SPOCK, Sign.ROCK), "winner": Sign.SPOCK }
    { "hands": (Sign.ROCK, Sign.SCISSORS), "winner": Sign.ROCK }
]

def test_data():
    # SCISSORS vs PAPER = SCISSORS WINNER
    # PAPER vs ROCK = PAPER WINNER
    # ROCK vs LIZARD = ROCK WINNER
    # LIZARD vs SPOCK = LIZARD WINNER
    # SPOCK vs SCISSORS = SPOCK WINNER
    # SCISSORS vs LIZARD = SCISSORS WINNER
    # LIZARD vs PAPER = LIZARD WINNER
    # PAPER vs SPOCK = PAPER WINNER
    # SPOCK vs ROCK = SPOCK WINNER
    # ROCK vs SCISSORS = ROCK WINNER

    # The structure is this { (Sign, Sign): Tuple<Sign, Sign>, Winner: Sign }


    return None


class Player: 

    def __init__(self, username: str = "DefaultPlayer"):
        self.__username = username
        if not self.__username:
            raise Exception("Username must not be empty !")

        if len(self.__username) < 4:
            raise Exception("Username must be greater than 4 characters !")

class Round: 

    def __init__(self, roundId):
        self.__roundId = roundId

class Game: 

    def __init__(self, first_player: Player, second_player: Player):
        self.__first_player = first_player
        self.__second_player = second_player

        if not self.__first_player or not self.__second_player: 
            raise Exception("Players must be initialized !")


    def play(self):
        # It's where the game is played !

        return None



if __name__ == "__main__":
    # Entrypoint here
    # Read input files here for test (with sys args)
    print("Welcome to Sheldon Game !")

    test_data()

    if len(sys.argv) < 3:
        raise Exception("Need to add arguments ! Exemple: python3 main.py <matches.csv> <players_infos.csv> <round.csv>")

    