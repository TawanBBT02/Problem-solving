import random
print("***Welcome to the Number Gressing Game!***\nI'm thinking of a number between 1 and 100. Can you guess it?")
ran = random.randint(1,100)
attempts = 0
while(True):
    answer = int(input("Enter your guess : "))
    attempts += 1
    if answer<ran:
        print("Too low! Try again.")
        
    elif answer>ran:
        print("Too high! Try again.")
        
    elif answer==ran:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
