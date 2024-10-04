def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0
    
    for _ in range(9):
        print_board(board)
        player = players[turn]
        print(f"Player {player}'s turn")
        
        # Get row and column from player
        row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
        
        # Validate the move
        if board[row][col] != " ":
            print("Cell already taken, try again.")
            continue
        
        # Place player's move
        board[row][col] = player
        
        # Check for a winner
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return
        
        # Switch turn
        turn = 1 - turn
    
    print_board(board)
    print("It's a draw!")

# Start the game
tic_tac_toe()
