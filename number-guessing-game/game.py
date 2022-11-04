from random import randint

tries = 0
max_tries = 7
secret = randint(1, 100)

while tries < max_tries:
    guess = int(input("Enter an integer between 1 and 100 [" + str(tries + 1) + "]: "))
    if secret == guess:
        print("You win game!")
        break
    tries = tries + 1
    if tries == max_tries:
        print(f"You lose the game!")
        print(secret)
        break
    if guess < secret:
        print("Pick larger one!")
    else:
        print("Pick smaller one!")
