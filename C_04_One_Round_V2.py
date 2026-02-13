import random
import time

def initial_points(which_player):
    """roll dice twice and return total / if double points apply"""



    double = "no"
    # Roll the dice for the user and note if they got double
    roll_one = random.randint(1, 6)
    roll_two = random.randint(1, 6)
    if roll_one == roll_two:
        double = "yes"

    total = roll_two + roll_one
    print(f"{which_player} \t-Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total}")
    return total, double

def make_statement(statement, decoration):
    """adds emoji/decoration to headings"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")
#main starts here

#roll the dice for the user
initial_user = initial_points("user")
initial_bot = initial_points("bot")

#reteieve user points
user_points = initial_user[0]
bot_points = initial_bot[0]


double_user = initial_user[1]
#double?
if double_user == "yes":
    print()
    print("you will get double points if you win!")
#assume user goes first
first = "User"
second = "Bot"
player_1_points = user_points
player_2_points = bot_points

#if user has lower points they start
if user_points < bot_points:
    print("you start because your initial roll was less\n")

#if both int are equal
elif user_points == bot_points:
    print("both rolls were equal, user goes first")

#if bot has lower points
else:
    player_1_points, player_2_points = player_2_points, player_1_points
    first, second = second, first

#loop till win
while player_1_points < 13 and player_2_points < 13:
    print()
    input("press <enter> to continue this round\n")

    #first player rolls the dice and score is updated
    print("rolling p1...")
    print()
    time.sleep(0.7)
    print("rolling p2...")
    print()
    time.sleep(0.7)
    player_1_roll = random.randint(1, 6)
    player_1_points += player_1_roll
    print(f"{first}:\trolled a {player_1_roll} - has {player_1_points} points")

    #if player ones score is over 13 end round
    if player_1_points >= 13:
        break

    #player 2 turn and score update

    player_2_roll = random.randint(1, 6)
    player_2_points += player_2_roll

    print(f"{second}:\trolled a {player_2_roll} - has {player_2_points} points")

#end of round

# associate player points with either the user r the computer
user_points = player_1_points
bot_points = player_2_points

#switch user and bot if they are swapped
if first == "Bot":
    user_points, bot_points = bot_points, user_points

#who won?
if user_points > bot_points:
    winner = "User"
else:
    winner = "Bot"
round_feedback = f"{winner} wins!!"

#double points if apropriate
if winner == "user" and double_user == "yes":
    user_points = user_points * 2

#output results
make_statement("Round results", "=")
print(f"user points: {user_points} | Bot points {bot_points}")
time.sleep(0.7)
print(round_feedback)
print()
