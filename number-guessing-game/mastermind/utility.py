import math
import random
from enum import Enum


class GameStatus(Enum):
    PLAYER_WINS_GAME = 1
    PLAYER_WINS_LEVEL = 2
    PLAYER_LOSES_LEVEL = 3
    PLAYER_CONTINUES_LEVEL = 4


def includes(elements, x):
    for element in elements:
        if x == element:
            return True
    return False


def create_secret(level):
    digits = [random.randint(1, 9)]
    while len(digits) < level:
        digit = random.randint(0, 9)
        if not includes(digits, digit):
            digits.append(digit)
    # digits = [5, 4, 0, 1, 2] -> 54012
    result = 0
    for digit in digits:
        result = 10 * result + digit  # 5 54 540 5401 54012
    print(result)
    return result


def evaluate_move(guess, secret, level):
    guess = str(guess)
    secret = str(secret)
    perfect_match = 0
    partial_match = 0
    for i in range(level):
        g = guess[i]
        for j in range(level):
            s = secret[j]
            if g == s:
                if i == j:
                    perfect_match += 1
                else:
                    partial_match += 1
    if perfect_match == 0 and partial_match == 0:
        return "No match"
    message = ""
    if perfect_match > 0:
        message += f"+{perfect_match}"
    if partial_match > 0:
        message += f"-{partial_match}"
    return message


def create_max_tries(game_level):
    return math.ceil(math.log2(10 ** game_level))
