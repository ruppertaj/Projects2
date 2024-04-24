import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0,top_of_range)
user_score = 0

while True:
    user_score += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    
    if user_guess == random_number:
        break
    elif user_guess > random_number:
        print(f"{user_guess} is incorrect. You were above the number.")     
    else:
        print(f"{user_guess} is incorrect. You were lower than the number.")
    print("Please try again.")
    
print(f"\n{user_guess} is correct! Well done! \nYou got it correct in {user_score} guesses.")