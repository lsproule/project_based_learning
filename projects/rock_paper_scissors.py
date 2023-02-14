from random import choice


def not_valid_input():
    print("Not valid input. Please try again. pick rock, paper, or scissors.")
    return get_input()


def get_input():
    player = input("Player 1, pick rock, paper, or scissors:[r/p/s] ").lower()
    player = "rock" if player == "r" else player
    player = "paper" if player == "p" else player
    player = "scissors" if player == "s" else player
    return player if player in ["rock", "paper", "scissors"] else not_valid_input()


def get_computer_choice():
    return choice(["rock", "paper", "scissors"])


def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("Player 1 wins!")
    elif player_choice == "rock" and computer_choice == "paper":
        print("Computer wins!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("Player 1 wins!")
    elif player_choice == "paper" and computer_choice == "scissors":
        print("Computer wins!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player 1 wins!")
    elif player_choice == "scissors" and computer_choice == "rock":
        print("Computer wins!")
    else:
        print("Something went wrong!")


def game_loop():
    while True:
        player_choice = get_input()
        computer_choice = get_computer_choice()
        print(f"{player_choice = }")
        print(f"{computer_choice = }")
        check_winner(player_choice, computer_choice)
        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() == "n":
            break


def main():
    game_loop()


if __name__ == "__main__":
    main()
