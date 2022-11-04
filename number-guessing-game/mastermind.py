from mastermind.utility import create_secret

game_level = 3
secret = create_secret(game_level)
tries = 0
max_tries = 10

while game_level < 10:
    print(f"Game level: {game_level}")
    guess = int(input(f"Enter an {game_level}-digit integer: "))
    tries = tries + 1
    if guess == secret:
        game_level = game_level + 1
        tries = 0
        secret = create_secret(game_level)
    else:
        message = evaluate_move(secret,guess)
        print(message)
