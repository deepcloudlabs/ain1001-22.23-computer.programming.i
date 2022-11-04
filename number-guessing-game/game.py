from random import randint

tries = 0
max_tries = 7
secret = randint(1, 100)

while tries < max_tries:
    guess = int(input(f"[{tries + 1}] Enter an integer between 1 and 100: "))
    tries = tries + 1
    if secret == guess:
        print("You win game!")
        break
    if tries == max_tries:
        print(f"You lose the game. Secret was {secret}.")
        break
    if guess < secret:
        print("Pick larger one!")
    else:
        print("Pick smaller one!")
