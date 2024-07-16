import random

def provide_feedback(secret, guess):
    correct_position = 0
    correct_digit = 0
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            correct_position += 1
        elif guess[i] in secret:
            correct_digit += 1
    return correct_position, correct_digit

def play_round(secret_number, player_name):
    attempts = 0
    while True:
        guess = input(f"{player_name}, enter your guess: ")
        attempts += 1
        correct_position, correct_digit = provide_feedback(secret_number, guess)
        if correct_position == len(secret_number):
            print(f"Correct! {player_name} guessed the number in {attempts} attempts.")
            break
        else:
            print(f"Feedback: {correct_position} digits in the correct position, {correct_digit} correct digits in the wrong position.")
    return attempts

def main():
    num_digits = int(input("Enter the number of digits for the secret number: "))

    # Player 1 sets the number
    player1_number = input("Player 1, enter the number for Player 2 to guess: ")

    # Player 2 guesses Player 1's number
    print("Player 2's turn to guess.")
    player2_attempts = play_round(player1_number, "Player 2")

    # Player 2 sets the number
    player2_number = input("Player 2, enter the number for Player 1 to guess: ")

    # Player 1 guesses Player 2's number
    print("Player 1's turn to guess.")
    player1_attempts = play_round(player2_number, "Player 1")

    # Determine the winner
    if player1_attempts < player2_attempts:
        print("Player 1 wins and is crowned Mastermind!")
    elif player2_attempts < player1_attempts:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
