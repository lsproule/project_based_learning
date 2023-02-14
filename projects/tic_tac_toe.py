def get_input(player, board):
    while True:
        row = input(f"{player} pick a row: ")
        col = input(f"{player} pick a column: ")
        if not row.isdigit() or not col.isdigit():
            print("Please enter a number.")
            continue
        row = int(row)
        col = int(col)
        if row not in range(3) or col not in range(3):
            print("Please enter a number between 0 and 2.")
            continue
        if board[row][col] != " ":
            print("That space is already taken.")
            continue
        return row, col


def print_board(board):
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            print(f"{board[i][0]} wins!")
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            print(f"{board[0][i]} wins!")
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print(f"{board[0][0]} wins!")
        return True
    if board[2][0] == board[1][1] == board[0][2] != " ":
        print(f"{board[2][0]} wins!")
        return True
    return False
        
def game_loop():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    print_board(board)    
    player1 = "X"
    player2 = "O"
    winner = False
    while winner != True:
        row, col = get_input(player1, board)
        board[row][col] = player1
        print_board(board)
        winner = check_winner(board)
        if winner == True:
            break
        row, col = get_input(player2, board)
        board[row][col] = player2
        print_board(board)
        winner = check_winner(board)

def main():
    while True:
        game_loop()
        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() == "n":
            break

if __name__ == "__main__":
    main()