def dice_roller():
    import random
    return random.randint(1, 6)
dice_roller()

def play_game():
    print("Welcome to the dice roller game!")
    print("You rolled a", dice_roller())
    print("Do you want to roll again? (yes/no)")
    answer = input()
    if answer == "yes":
        play_game()
    else:
        print("Goodbye!")
        play_game()
