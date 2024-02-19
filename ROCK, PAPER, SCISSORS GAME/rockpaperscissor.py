import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "win"
    else:
        return "lose"

def print_result(user_choice, computer_choice, result):
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(f"Result: {result}")

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == 'yes'

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("Welcome to Rock, Paper, Scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, result)

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"Your Score: {user_score}, Computer's Score: {computer_score}")

        if not play_again():
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
