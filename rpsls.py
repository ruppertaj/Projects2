import random

user_score = 0
comp_score = 0

game_variables = ["rock","paper","scisscors","lizard","spock"]
### rock = 0, paper = 1, scissors = 2, lizard = 3, spock = 4

win_combos = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["lizard", "paper"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"],
}

while True:
    user_input = input("Type Rock/Paper/Scissors/Lizard/Spock, or Q to quit. ").lower()
    if user_input == "q":
        break
        
    if user_input not in game_variables:
        continue
    
    random_number = random.randint(0,4)

    comp_pick = game_variables[random_number]
    print (f"Computer picked {comp_pick}.")
    
    if user_input == comp_pick:
        print("You tied.")
    
    elif comp_pick in win_combos[user_input]:
        print("You won!")
        user_score += 1
    
    else:
        print("You lost!")
        comp_score += 1
    
print(f"You won {user_score} times, computer won {comp_score} times.")
print("Goodbye!")