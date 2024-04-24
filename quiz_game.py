print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()
score = 0
questions = 0

if playing != "yes":
    quit()
    
print("Okay! Lets play :)")

answer_1 = input("What does CPU stand for? ")
questions += 1
if answer_1.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print(f"{answer_1} is incorrect. The answer is Central Processing Unit.")
    
answer_2 = input("What does GPU stand for? ")
questions += 1
if answer_2.lower() == 'graphics processing unit':
    print("Correct!")
    score += 1
else:
    print(f"{answer_2} is incorrct. The answer is Graphics Processing Unit.")

# and on and on and on...

print(f"Thanks for playing! You got {score} correct!")
print("You got " + str((score / questions) * 100) + "%.")