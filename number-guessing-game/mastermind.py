"""
Game Level : 3
Secret is 549
Player enters 123 -> No match
              456 -> -2
              574 -> +1-1
              594 -> +1-2
"""
from mastermind.utility import create_secret, evaluate_move, GameStatus

# region initialization
game_level = 3
secret = create_secret(game_level)
tries = 0
max_tries = 10
game_status = GameStatus.PLAYER_CONTINUES_LEVEL
# endregion

while game_status != GameStatus.PLAYER_WINS_GAME:
    guess = int(input(f"[Game Level: {game_level}][Move: {tries + 1} of {max_tries}] Enter you guess: "))
    tries = tries + 1
    if guess == secret:
        game_level = game_level + 1
        if game_level == 10:
            game_status = GameStatus.PLAYER_WINS_GAME
            print("Congratulations! You win the game!")
        else:
            tries = 0
            secret = create_secret(game_level)
            max_tries += 2
            print("Great! Move to the next level! Good luck!")
    elif tries > max_tries:
        print(f"""
            You lose the level {game_level}. 
            Secret was {secret}. 
            Continue with a new secret.
            Good luck!""")
        tries = 0
        secret = create_secret(game_level)
    else:
        message = evaluate_move(guess, secret, game_level)
        print(message)
