import random

def roll_dice(dice):
    if dice == 1:
        return random.randint(1, 6)
    elif dice == 2:
        return random.randint(1, 6)
    elif dice == 3:
        roll = random.randint(1, 100)
        if roll <= 90:
            return 3
        else:
            return random.randint(1, 6)
    elif dice == 4:
        roll = random.randint(1, 100)
        if roll <= 25:
            return 4
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

        player1_sum += player1_roll
        player2_sum += player2_roll

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
        player1_sum += player1_roll
        player2_sum += player2_roll
        print(f"{player1_name} total score: {player1_sum}")
        print(f"{player2_name} total score: {player2_sum}")
        print()
        
    if player1_sum > player2_sum:
        print(f"{player1_name} wins!")
    else:
        print(f"{player2_name} wins!")

num_rolls = int(input("Enter the number of rolls: "))
play_game(num_rolls)
