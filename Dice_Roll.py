#Roll the Dice
import random

def rollDice() :
    a = random.randint(1,6)
    print(f"You got {a}")

print("Roll the dice ? (y/n)")

while True:
    
    choice = input().lower()
    
    if choice == 'y':
        rollDice()
    elif choice == 'n':
        print("Thanks for playing. ")
        break
    else :
        print("Invalid choice")