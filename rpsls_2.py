import random

# Define available choices
choices = ["rock", "paper", "scissors", "lizard", "spock"]

# Define winning combinations (key beats value)
win_combos = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"],
}


def get_player_choice():
    """
    Gets the player's choice for the game.
    """
    
    while True:
        player_choice = input("Choose rock, paper, scissors, lizard, or spock, Q to quit: ").lower()
        if player_choice == "q":
            quit()
        if player_choice in choices:
            return player_choice
        else:
            continue


def get_computer_choice():
    """
    Generates a random choice for the computer.
    """
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    """
    Determines the winner based on player and computer choices.
    """
    if player_choice == computer_choice:
        return "Tie"
    elif computer_choice in win_combos[player_choice]:
        return "You Win!"
    else:
        return "You Lose."


def play_game():
    """
    Runs a single round of the game.
    """
    global user_score, comp_score  # Access global variables
    while True:
        
        player_choice = get_player_choice()
        
        computer_choice = get_computer_choice()
        print(f"You chose {player_choice.capitalize()}, computer chose {computer_choice.capitalize()}.")

        winner = determine_winner(player_choice, computer_choice)

        if winner == "Tie":
            pass
        elif winner == "You Win!":
            user_score += 1
        else:
            comp_score += 1

        print(winner)
        print(f"Current Score: You - {user_score}, Computer - {comp_score}")


user_score = 0
comp_score = 0

# Start the game
play_game()
