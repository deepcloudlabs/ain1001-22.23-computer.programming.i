from random import randint

player1 = 0
player2 = 1

game_board = [
    {
        "wins": False,
        "position": 0,
        "penalty": -1,
        "reward": -1
    },
    {
        "wins": False,
        "position": 0,
        "penalty": -1,
        "reward": -1
    }
]

next_move = {
    "penalty": -10,
    "reward": 10
}

for each_player in [player1, player2]:
    print(f"For Player #{each_player + 1}")
    for bifurcation in ["penalty", "reward"]:
        valid_input = False
        while not valid_input:
            box_number = int(input(f"Please enter your {bifurcation} square number: "))
            if 0 < box_number <= 100:
                valid_input = True
            for player in [player1, player2]:
                for pr in ["penalty", "reward"]:
                    if box_number == game_board[player][pr]:
                        print(f"Error: You, Player #{each_player + 1}, pick the Player #{player +1}'s {pr} box!")
                        valid_input = False
                        break
        game_board[each_player][bifurcation] = box_number

while not game_board[player1]["wins"] and not game_board[player2]["wins"]:
    for each_player in [player1, player2]:
        input(f"Player #{each_player + 1}, press Enter to throw the dice.")
        dice = randint(1, 6)
        print(f"Dice is {dice}.")
        position = game_board[each_player]["position"] + dice
        for player in [player1, player2]:
            for bifurcation in ["penalty", "reward"]:
                if position == game_board[each_player][bifurcation]:
                    position += next_move[bifurcation]
                    print(f"Player #{each_player + 1} hits the {bifurcation} box.")
                    break
        if position > 100:
            game_board[player1]["wins"] = True
        if position < 0:
            position = 0
        game_board[each_player]["position"] = position
        print(f"Player #{each_player +1}'s current position is now {position}.")
if game_board[player1]["wins"] and game_board[player2]["wins"]:
    print("The game is a tie.")
elif game_board[player1]["wins"]:
    print("Player #1 wins the game.")
else:
    print("Player #2 wins the game.")
