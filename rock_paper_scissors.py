# Not case sensitive
# comp_choices are rock, paper, or scissors
import random as r # For the computer to randomly choose a choice

choices = ["rock", "paper", "scissors"] # List of choices for the computer to choose from

def user_input():
    user_choice = None
    while user_choice is None:
        user_choice = input("Choose: Rock, Paper, or Scissors? ").lower()
        if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':
            return user_choice # Return if the user enter a valid input
        else:
            print("Invalid Input.")
            user_choice = None

def play_again(): # Ask if the user wanna play again
    while True:
        again = input("Wanna play again? ").lower() # Not case sensitive
        if again == "yes" or again == 'y':
            return True
        elif again == 'no' or again == 'n':
            return False
        else:
            print("Answer must be yes, no, y, or n.")

def main():
    while True:
        print("==================================\n") # For dividing- visual
        user_choice = user_input()
        comp_choice = r.choice(choices)

        # Compare the user input and the computer choice
        if user_choice == comp_choice:
            print(f"You choose {user_choice} and the computer choose {comp_choice}. You tie!")
        elif comp_choice == 'rock':
            if user_choice == 'scissors':
                print(f"You choose {user_choice} and the computer choose {comp_choice}. You lose...\n")
            else:
                print(f"You choose {user_choice} and the computer choose {comp_choice}. You win!\n")
        elif comp_choice == 'paper':
            if user_choice == 'rock':
                print(f"You choose {user_choice} and the computer choose {comp_choice}. You lose...\n")
            else:
                print(f"You choose {user_choice} and the computer choose {comp_choice}. You win!\n")
        elif comp_choice == 'scissors':
            if user_choice == 'paper':
                print(f"You choose {user_choice} and the computer choose {comp_choice}. You lose...\n")
            else:
                print(f"You choose {user_choice} and the computer choose {comp_choice}. You win!\n") 
        
        again = play_again() # If the user wanna play again or not
        print("")
        if again == False:
            print("Thank you for playing!")
            print("==================================\n")
            break

main()