import random
import time

#in the beginning bot and user points are both 0
bot_score = 0
user_score = 0
game_goal = int(input("game goal"))

#play multiple rounds until a winner has been found
while bot_score < game_goal and user_score < game_goal:

    #start of loop
    #for testing purposes, ask the user what the points are
    bot_points = int(input("enter computer points at end of round"))
    user_points = int(input("enter user points at the end of round"))
    #outside rounds loop - update score with round points
    bot_score += bot_points
    user_score += user_points

    #show overall scores (round loop)
    print("***game update***")
    print(f"user score: {user_score} | bot score {bot_score}")

#end of entire game ,output final results
print()
if user_score > bot_score:
    print("user win")
else:
    print("computer win ")