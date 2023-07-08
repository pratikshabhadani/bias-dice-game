import random

def roll_dice(dice):
    if dice == 1:
        return random.randint(1, 6)
    elif dice == 2:
        return random.randint(1, 6)
    elif dice == 3:
        roll = random.randint(1, 100)
        if roll <= 30:
            return 3
        else:
            return random.randint(1, 6)
    elif dice == 4:
        roll = random.randint(1, 100)
        if roll <= 25:
            return 4
        else:
            return random.randint(1, 6)
    elif dice == 5:
        roll = random.randint(1, 100)
        if roll <= 50:
            return 6
        else:
            return random.randint(1, 6)
    elif dice == 6:
        roll = random.randint(1, 100)
        if roll <= 50:
            return 1
        else:
            return random.randint(1, 6)
    
def play_game(num_rolls):
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")
    player1_sum = 0
    player2_sum = 0

    for throw in range(1, num_rolls+1):
        print(f"Throw {throw}:")
        player1_dice = int(input(f"{player1_name}, choose a dice (1-4): "))
        player2_dice = int(input(f"{player2_name}, choose a dice (1-4): "))

        player1_roll = roll_dice(player1_dice)
        player2_roll = roll_dice(player2_dice)

        print(f"{player1_name} rolled a {player1_roll} with dice {player1_dice}")
        print(f"{player2_name} rolled a {player2_roll} with dice {player2_dice}")

        player1_sum += player1_roll # type: ignore
        player2_sum += player2_roll # type: ignore

        print()

    print(f"{player1_name} total score: {player1_sum}")
    print(f"{player2_name} total score: {player2_sum}")

    while player1_sum == player2_sum:
        print("It's a tie! Rolling again...")
        num_rolls += 1
        player1_dice = int(input(f"{player1_name}, choose a dice (1-4): "))
        player2_dice = int(input(f"{player2_name}, choose a dice (1-4): "))
        player1_roll = roll_dice(player1_dice)
        player2_roll = roll_dice(player2_dice)
        print(f"{player1_name} rolled a {player1_roll} with dice {player1_dice}")
        print(f"{player2_name} rolled a {player2_roll} with dice {player2_dice}")
        player1_sum += player1_roll # type: ignore
        player2_sum += player2_roll # type: ignore
        print(f"{player1_name} total score: {player1_sum}")
        print(f"{player2_name} total score: {player2_sum}")
        print()
           
    if player1_sum > player2_sum:
        x= player1_name
        y= player2_name
    else:
        x= player2_name
        y= player1_name
    
    g= int(input(f"{x}, do you want to gamble?(enter 0 for no 1 for yes): "))
    if(g==0): print(f"{x} wins! \nTotal amount won: Rs.1,000")
    else:
        x_dice= int(input(f"{x}, choose a dice (5 or 6): "))
        x_roll= roll_dice(x_dice)
        if(x_roll==1):
            print()
            print(f"{x} looses the gamble! \n{y} wins Rs.750")
        elif(x_roll==6): 
            print()
            print(f"{x} wins the gamble! \nTotal amount won: Rs.2,000")
        else:
            print()
            print(f"{x} wins! \nTotal amount won: Rs.750!")

num_rolls = int(input("Enter the number of rolls: "))
play_game(num_rolls)
