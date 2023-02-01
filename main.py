import sys
from enum import Enum

class Sign(Enum):
    SCISSORS: int = 1
    PAPER: int = 2
    ROCK: int = 3
    LIZARD: int = 4
    SPOCK: int = 5

# List of possible hands
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
WINNERS = [
    { "hands": (Sign.SCISSORS, Sign.PAPER), "winner": Sign.SCISSORS },
    { "hands": (Sign.PAPER, Sign.ROCK), "winner": Sign.PAPER },
    { "hands": (Sign.ROCK, Sign.LIZARD), "winner": Sign.ROCK },
    { "hands": (Sign.LIZARD, Sign.SPOCK), "winner": Sign.LIZARD },
    { "hands": (Sign.SPOCK, Sign.SCISSORS), "winner": Sign.SPOCK },
    { "hands": (Sign.SCISSORS, Sign.LIZARD), "winner": Sign.SCISSORS },
    { "hands": (Sign.LIZARD, Sign.PAPER), "winner": Sign.LIZARD },
    { "hands": (Sign.PAPER, Sign.SPOCK), "winner": Sign.PAPER },
    { "hands": (Sign.SPOCK, Sign.ROCK), "winner": Sign.SPOCK },
    { "hands": (Sign.ROCK, Sign.SCISSORS), "winner": Sign.ROCK },
]

class Player: 

    def __init__(self, username: str = "DefaultPlayer"):
        self.__username: str = username
        self.__hand: Sign = None
        if not self.__username:
            raise Exception("Username must not be empty !")

        if len(self.__username) < 3:
            raise Exception("Username must be greater than 3 characters !")

    @property
    def username(self):
        return self.__username

    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self, sign: Sign):
        self.__hand = sign

class Round: 

    def __init__(self, roundId: int, first_player: Player, second_player: Player):
        self.__roundId = roundId
        self.__first_player = first_player
        self.__second_player = second_player

        if not self.__first_player or not self.__second_player: 
            raise Exception("Players must be initialized !")

        print(f"Starting round {roundId} with players: {first_player.username} and {second_player.username}")

    def play(self, player: Player, sign: Sign):
        if not player:
            raise Exception("Unknown Player !")

        player.hand = sign

        print(f"Player: {player.username} is playing {sign} !")

        if not self.__first_player.hand or not self.__second_player.hand:
            return None
        
        print(f"All players played !")

        winner = None

        for element in WINNERS:
            if (self.__first_player.hand, self.__second_player.hand) == element["hands"] or (self.__second_player.hand, self.__first_player.hand) == element["hands"]:
                # Here we find the winner
                is_fp_winner = self.__first_player.hand == element["winner"]
                winner = self.__first_player if is_fp_winner else self.__second_player
                break
            
        if winner:
            print(f"Player: {winner.username} won the round !")
        else: 
            print("No one has won !")


        return None

    def get_result(self):

        return None

class Game: 

    def __init__(self):

        return None


def test_data():

    player1 = Player("Nahim")
    player2 = Player("Noé")

    myRound = Round(0, player1, player2)

    myRound.play(player1, Sign.ROCK)
    myRound.play(player2, Sign.SCISSORS)


    return None


if __name__ == "__main__":
    # Entrypoint here
    # Read input files here for test (with sys args)
    print("Welcome to Sheldon Game !")

    test_data()

    if len(sys.argv) < 3:
        raise Exception("Need to add arguments ! Exemple: python3 main.py <matches.csv> <players_infos.csv> <round.csv>")

    