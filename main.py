import sys
from enum import Enum
from collections import defaultdict
import csv
import numpy as np


class Sign(Enum):
    SCISSORS: str = "SCISSORS"
    PAPER: str = "PAPER"
    ROCK: str = "ROCK"
    LIZARD: str = "LIZARD"
    SPOCK: str = "SPOCK"

    def __str__(self) -> str:
        return self.name


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
    {"hands": (Sign.SCISSORS, Sign.PAPER), "winner": Sign.SCISSORS},
    {"hands": (Sign.PAPER, Sign.ROCK), "winner": Sign.PAPER},
    {"hands": (Sign.ROCK, Sign.LIZARD), "winner": Sign.ROCK},
    {"hands": (Sign.LIZARD, Sign.SPOCK), "winner": Sign.LIZARD},
    {"hands": (Sign.SPOCK, Sign.SCISSORS), "winner": Sign.SPOCK},
    {"hands": (Sign.SCISSORS, Sign.LIZARD), "winner": Sign.SCISSORS},
    {"hands": (Sign.LIZARD, Sign.PAPER), "winner": Sign.LIZARD},
    {"hands": (Sign.PAPER, Sign.SPOCK), "winner": Sign.PAPER},
    {"hands": (Sign.SPOCK, Sign.ROCK), "winner": Sign.SPOCK},
    {"hands": (Sign.ROCK, Sign.SCISSORS), "winner": Sign.ROCK},
]


class Player:

    def __init__(self, username: str = "DefaultPlayer"):
        self.__username: str = username
        self.__hand: Sign = None
        if not self.__username:
            raise ValueError("Username must not be empty !")

        if len(self.__username) < 3:
            raise ValueError(
                f"Username must be greater than 3 characters ! {self.__username}")

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

    def play(self, player: Player, sign: Sign):
        if not player:
            raise Exception("Unknown Player !")

        player.hand = sign

        if not self.__first_player.hand or not self.__second_player.hand:
            return None

        winner = None

        for element in WINNERS:
            if (self.__first_player.hand == self.__second_player.hand):
                ply1Username = self.__first_player.username
                ply2Username = self.__second_player.username
                winner = self.__first_player if ply1Username < ply2Username else self.__second_player
                break
            if (self.__first_player.hand, self.__second_player.hand) == element["hands"] or (self.__second_player.hand, self.__first_player.hand) == element["hands"]:
                # Here we find the winner
                is_fp_winner = self.__first_player.hand == element["winner"]
                winner = self.__first_player if is_fp_winner else self.__second_player
                break

        return [self.__roundId, winner.username, self.__first_player.username, self.__first_player.hand, self.__second_player.username, self.__second_player.hand, winner.hand]

    def get_result(self):

        return None


class Game:

    def __init__(self):

        return None


def test_data(players_info, rounds):
    rounds_array = np.genfromtxt(
        rounds, encoding=None, skip_header=0, names=True, delimiter=',', dtype=None)
    ply_info_array = defaultdict(list)

    max_round = 0

    with open(players_info, "r") as inputfile:
        reader = csv.reader(inputfile)
        next(reader, None)

        for name, roundV, sign in reader:
            if max_round < int(roundV): max_round = int(roundV)
            ply_info_array[name].append(Sign(sign))

    # Sort the data with max_round instead of foreaching (match only the first row to know which player it is)
    # Create your round filter all names from "Name" includes ply1 or ply2 username
    # Iterate through rounds

    def zipper(iterable):
        a = iter(iterable)
        return zip(a, a)

    with open("matches.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Round", "Winner", "Player 1 name", "Player 1 sign",
                                "Player 2 name", "Player 2 sign"], delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        winners = []

        # First round based on round_0 file
        for players in rounds_array:
            player1 = Player(players[0])  # rounds_array[i]["Player 1"]
            player2 = Player(players[1])  # rounds_array[i]["Player 2"]

            ply1Signs = ply_info_array[player1.username]
            ply2Signs = ply_info_array[player2.username]

            myRound = Round(0, player1, player2)

            myRound.play(player1, Sign(ply1Signs[0]))
            matcht = myRound.play(player2, Sign(ply2Signs[0]))
            if matcht:
                winners.append(matcht[1])
                writer.writerow({"Round": matcht[0], "Winner": matcht[1], "Player 1 name": matcht[2],
                                "Player 1 sign": matcht[3], "Player 2 name": matcht[4], "Player 2 sign": matcht[5]})

        if (len(winners) < 2): 
          print(f"TOURNAMENT WINNER : {winners[0]}")
          return None

        def unique(sequence):
            seen = set()
            return [x for x in sequence if not (x in seen or seen.add(x))]

        winners = list(zipper(unique(winners)))

        # Play tournaments
        def matcher(winners, round):
            result = []

            for ply1Info, ply2Info in winners:
                player1 = Player(ply1Info)
                player2 = Player(ply2Info)

                ply1Signs = ply_info_array[player1.username]
                ply2Signs = ply_info_array[player2.username]

                myRound = Round(round, player1, player2)
                myRound.play(player1, Sign(ply1Signs[round]))
                winner = myRound.play(player2, Sign(ply2Signs[round]))

                if winner:
                    result.append(winner[1])
                    writer.writerow({"Round": winner[0], "Winner": winner[1], "Player 1 name": winner[2],
                                    "Player 1 sign": winner[3], "Player 2 name": winner[4], "Player 2 sign": winner[5]})

            if len(result) == 1:
                return result[0]
            else:
                return matcher(list(zipper(result)), round + 1)

        print(f"TOURNAMENT WINNER: {matcher(winners, 1)}")


    return None


if __name__ == "__main__":
    # Entrypoint here
    # Read input files here for test (with sys args)

    if len(sys.argv) < 3:
        raise Exception(
            "Need to add arguments ! Exemple: python3 main.py <players_infos.csv> <round.csv>")

    test_data(sys.argv[1], sys.argv[2])

