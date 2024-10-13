import random

def guess_the_number_win_prizes():
    def initialization():
        print("\nWelcome to the game: Guess the Number and Win Prizes!\n")
        print("Game Rules:")
        print("1. You must invest an amount greater than zero.")
        print("2. You will have 5 chances to guess the number between 1 and 10.")
        print("3. Depending on how many attempts it takes to guess the number, you will get the following return:")
        print("    - Guess 1: 5x your investment")
        print("    - Guess 2: 3x your investment")
        print("    - Guess 3: 2x your investment")
        print("    - Guess 4: 1.5x your investment")
        print("    - Guess 5: 1x your investment\n")

        computer_generated_number = random.randint(1, 10)
        rewards = {1: 5, 2: 3, 3: 2, 4: 1.5, 5: 1}

        while True:
            try:
                entry_fee = int(input("Enter the amount you want to invest: "))
                if entry_fee > 0:
                    break
                else:
                    print("The amount must be greater than zero. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid amount in rupees.")

        return computer_generated_number, entry_fee, rewards

    def start_game(computer_generated_number, rewards):
        print("\nLet's start the game!")
        print("You have to guess the number between 1 and 10.\n")

        for attempt in range(1, 6):
            try:
                users_number = int(input(f"Attempt {attempt}: Enter your guess: "))
                if users_number < 1 or users_number > 10:
                    print(f"Your guess must be between 1 and 10. {5-attempt} attempt(s) remaining.\n")
                    continue
            except ValueError:
                print(f"Invalid input. {5-attempt} attempt(s) remaining.\n")
                continue

            if computer_generated_number == users_number:
                return True, rewards[attempt]
            elif computer_generated_number < users_number:
                print(f"Your guess was incorrect. Hint: Try a smaller number. {5-attempt} attempt(s) remaining.\n")
            else:
                print(f"Your guess was incorrect. Hint: Try a larger number. {5-attempt} attempt(s) remaining.\n")

        return False, 0

    def stop_game(status, multiplier, amount):
        if status:
            print(f"Congratulations! You won {amount * multiplier} rupees!")
        else:
            print("Sorry, you lost the game. Better luck next time!")

    # Game initialization
    computer_generated_number, amount_invested, rewards = initialization()

    # Start the game
    status, multiplier = start_game(computer_generated_number, rewards)

    # End the game
    stop_game(status, multiplier, amount_invested)

# Run the game
guess_the_number_win_prizes()

