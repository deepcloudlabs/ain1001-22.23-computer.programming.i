import random
from enum import Enum

from mastermind.utility import create_max_tries


class GameStatus(Enum):
    PLAYER_WINS_GAME = 1
    PLAYER_WINS_LEVEL = 2
    PLAYER_LOSES_LEVEL = 3
    PLAYER_CONTINUES_LEVEL = 4


def create_secret(level):
    lower = 1
    upper = 10 ** level
    return random.randint(lower, upper)


game_level = 2
game_status = GameStatus.PLAYER_CONTINUES_LEVEL
while game_status != GameStatus.PLAYER_WINS_GAME:
    secret = create_secret(game_level)
    tries = 0
    max_tries = create_max_tries(game_level)
    moves = []
    upper_bound = 10 ** game_level
    while game_status == GameStatus.PLAYER_CONTINUES_LEVEL:
        guess = int(input(f"[Level: {game_level}, Move: {tries} of {max_tries}] Enter you guess [1,{upper_bound}]: "))
        tries = tries + 1
        moves.append(guess)
        if guess == secret:
            game_level += 1
            if game_level == 5:
                game_status = GameStatus.PLAYER_WINS_GAME
            else:
                game_status = GameStatus.PLAYER_WINS_LEVEL

            break
        elif guess < secret:
            print("Pick larger one!")
        else:
            print("Pick smaller one!")
        if tries >= max_tries:
            game_status = GameStatus.PLAYER_LOSES_LEVEL
    if game_status == GameStatus.PLAYER_LOSES_LEVEL:
        print(f"You lose! Retry the level {game_level}")
        game_status = GameStatus.PLAYER_CONTINUES_LEVEL
    elif game_status == GameStatus.PLAYER_WINS_LEVEL:
        print(f"Great! Move to the next level {game_level}")
        print(moves)
        game_status = GameStatus.PLAYER_CONTINUES_LEVEL
print("You win the game!")
