def print_board(board): # Prints out the board via every position and adds a space
    for i in range(0, len(board)):
        print()
        for position in board[len(board)-i-1]:
            print(position, end = " ")


def initialize_board(num_rows, num_cols): # Creates board by appending - for every column and multiplying by # of rows
    board = []
    for i in range(0, num_rows):
        board.append(list(num_cols*"-"))
    return board


def insert_chip(board, col, chip_type): # Checks if the position is a -, then replaces with a chip
    row_num = 0
    for i, row in enumerate(board):
        row_num = i
        if row[col] == "-":
            row[col] = chip_type
            break
    return row_num, col


def check_if_winner(board, col, row, chip_type): # A little inefficient but I'm too tired to make it more efficient
    consecutive_Chips = 0
    if row >= 3: # Checks if the row is greater than 3 (4 row lengths) because it needs to be min. 4 for a player to win
        for i in range(0, 4):
            if board[row-i][col] == chip_type: # Goes through every row below the position and checks if the chip matches
                consecutive_Chips += 1
            else:
                break
        if consecutive_Chips >= 4: # If 4 chips match in a row then it works
            return True
    consecutive_Chips = 1 # Reset for horizontal checks


    for i in range(1, 4): # Essentially checks 3 spaces in the left and right, and adds to consecutive chips
        if col-i >= 0:
            if board[row][col-i] == chip_type:
                consecutive_Chips += 1
            else:
                break
        else:
            break
    for i in range(1, 4):
        if col+i <= len(board[row])-1:
            if board[row][col+i] == chip_type:
                consecutive_Chips += 1
            else:
                break
        else:
            break
    if consecutive_Chips >= 4:
        return True
    else:
        return False


if __name__  == "__main__":
    rows_Input = int(input("What would you like the height of the board to be? ")) # Inputs for size of board
    columns_Input = int(input("What would you like the length of the board to be? "))
    board = initialize_board(rows_Input, columns_Input)
    print_board(board)

    print()
    player1_Chip = "x"
    print("Player 1: x")
    player2_Chip = "o"
    print("Player 2: o")


    game_Over = False
    game_Tied = False
    current_Turn = "Player 1"

    while not game_Over and not game_Tied: # Loop to keep the game running between players 1 and 2.
        current_Turn = "Player 1"
        place1 = int(input("Player 1: Which column would you like to choose? "))
        row1, col1 = insert_chip(board, place1, player1_Chip)
        print_board(board)
        game_Over = check_if_winner(board, col1, row1, player1_Chip)

        if not "-" in board[len(board)-1]:
            game_Tied = True

        if not game_Over and not game_Tied:
            current_Turn = "Player 2"
            place2 = int(input("Player 2: Which column would you like to choose? "))
            row2, col2 = insert_chip(board, place2, player2_Chip)
            print_board(board)
            game_Over = check_if_winner(board, col2, row2, player2_Chip)

            if not "-" in board[len(board) - 1]:
                game_Tied = True

    if game_Over == True: # If the game is won or the game is tied
        print(current_Turn + " won the game!")
    if game_Tied == True and game_Over == False:
        print("Draw. Nobody wins.")