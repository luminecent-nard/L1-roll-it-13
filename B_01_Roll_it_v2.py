import random
import time
#functions

def yes_no(question):
    """checks user response to a question that is yes / no (y/n), returns 'yes' or 'no' """

    while True:
        #yes or no
        response = input(question).lower()
        #identify yes or no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("nuh uh")

def instructions():
    """prints instructions"""

    print("""
*** Instructions ***

1. whoever rolls the lowest first, goes first
2. on your initial roll if you roll double, your round points will be doubled
3. write game goal below
 
    """)

def integer_checker():
    """checks that the integer is more than 13"""

    error = "Please enter an integer more that / equal to 13."
    while True:
        try:
            response = int(input("what is the game goal? "))

            if response < 13:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

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


#main routine
make_statement("welcome to the roll it 13 game", "<>")
print()

want_instructions = yes_no("do you want the instructions?: ")

#display instructions if the user wants to see
if want_instructions == "yes":
    instructions()

#in the beginning bot and user points are both 0
bot_score = 0
user_score = 0
rounds_played = 0
game_history = []
error = "Please enter an integer over 13."
while True:
    try:
        game_goal = int(input("what is the game goal? "))

        if game_goal < 13:
            print(error)
        else:
            print(f"game goal: {game_goal}")
            break
    except ValueError:
        print(error)



#play multiple rounds until a winner has been found
while bot_score < game_goal and user_score < game_goal:

    rounds_played += 1
    #start of loop
    make_statement(f"round {rounds_played}","+++")
    # roll the dice for the user

    initial_user = initial_points("user")
    initial_bot = initial_points("bot")

    # reteieve user points
    user_points = initial_user[0]
    bot_points = initial_bot[0]

    double_user = initial_user[1]
    # double?
    if double_user == "yes":
        print()
        print("you will get double points if you win!")
    # assume user goes first
    first = "User"
    second = "Bot"
    player_1_points = user_points
    player_2_points = bot_points

    # if user has lower points they start
    if user_points < bot_points:
        print("you start because your initial roll was less\n")

    # if both int are equal
    elif user_points == bot_points:
        print("both rolls were equal, user goes first")

    # if bot has lower points
    else:
        player_1_points, player_2_points = player_2_points, player_1_points
        first, second = second, first
        print("the bot rolled lower, you go second")

    # loop till win
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("press <enter> to continue this round\n")

        # first player rolls the dice and score is updated
        print(f"rolling {first}...")
        print()
        time.sleep(0.7)
        print(f"rolling {second}...")
        print()
        time.sleep(0.7)
        player_1_roll = random.randint(1, 6)
        player_1_points += player_1_roll
        print(f"{first}:\trolled a {player_1_roll} - has {player_1_points} points")

        # if player ones score is over 13 end round
        if player_1_points >= 13:
            break

        # player 2 turn and score update

        player_2_roll = random.randint(1, 6)
        player_2_points += player_2_roll

        print(f"{second}:\trolled a {player_2_roll} - has {player_2_points} points")

    # end of round

    # associate player points with either the user r the computer
    user_points = player_1_points
    bot_points = player_2_points

    # switch user and bot if they are swapped
    if first == "Bot":
        user_points, bot_points = bot_points, user_points

    # who won?
    if user_points > bot_points:
        winner = "User"
    else:
        winner = "Bot"
    round_feedback = f"{winner} wins!!"

    # work out who won and set the loser points to 0
    if user_points > bot_points:
        winner = "user"
        loser = "bot"
        bot_points = 0
    else:
        winner = "bot"
        loser = "user"
        user_points = 0
    round_feedback = f"the {winner} won.  the {loser}'s points have been reset to 0"

    # double points if apropriate
    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    # output results
    make_statement("Round results", "=")
    print(f"user points: {user_points} | Bot points {bot_points}")

    print(round_feedback)
    print()

    #outside rounds loop - update score with round points
    bot_score += bot_points
    user_score += user_points
    #generate a list
    game_results = (f"Round: {rounds_played} | user points: {user_points} | bot points: {bot_points} | winner: {winner}"
                    f"\nscore: {user_score}|{bot_score}")
    game_history.append(game_results)

    #show overall scores (round loop)
    make_statement("score update","*")
    print(f"user score: {user_score} | bot score {bot_score}")
    print()

#end of entire game ,output final results
make_statement("Game over","---")
print()
if user_score > bot_score:
    make_statement("You win!", "+")
else:
    make_statement("the computer won!", "-")
#display history
make_statement("game history", "-*-")

for item in game_history:
    print(item)






