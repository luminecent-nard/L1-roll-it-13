
#initialise list to hold game history
game_history = []

#get data (base component does this already)


while True:
    rounds_played = input("round?: ")
    if rounds_played == "":
        break
    user_points = int(input("user points?"))
    bot_points = int(input("bot points?"))
    winner = input("who won")
    user_score = int(input("user score"))
    bot_score = int(input("bot score"))



    game_results = (f"rounds {rounds_played} user {user_points} bot {bot_points} winner {winner}"
                    f"{user_score}|{bot_score}")

    game_history.append(game_results)

print("game history")

for item in game_history:
    print(item)