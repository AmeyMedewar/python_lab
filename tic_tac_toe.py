import random

def display_grid(game_st):
    size = len(game_st)
    print('--'*size*2)
    for i in range(size):
        print('|', end='')
        for j in range(size):
            print(f' {game_st[i][j]} ', end='|')
        print('')
        print('--'*size*2)

def generate_game_state(size):
    row = [' ']*size
    arr = []
    for i in range(size):
        arr.append(row.copy())
    return arr

def check_winner(game_st, player1, player2):
    # Check rows
    for row in game_st:
        if ' ' not in row and len(set(row)) == 1:
            return True, player1 if row[0] == 'x' else player2

    # Check columns
    for col in list(zip(*game_st)):
        if ' ' not in col and len(set(col)) == 1:
            return True, player1 if col[0] == 'x' else player2

    # Check main diagonal
    main_diag = [game_st[i][i] for i in range(len(game_st))]
    if ' ' not in main_diag and len(set(main_diag)) == 1:
        return True, player1 if main_diag[0] == 'x' else player2

    # Check anti-diagonal
    anti_diag = [game_st[i][len(game_st)-1-i] for i in range(len(game_st))]
    if ' ' not in anti_diag and len(set(anti_diag)) == 1:
        return True, player1 if anti_diag[0] == 'x' else player2

    return False, None

def xo_game():
    def initialization():
        print("This is a 2-player game. Each player will take turns. The first player to meet the winning condition will win.")
        player1 = input("Enter the name of the first player: ")
        player2 = input("Enter the name of the second player: ")

        mapping = {player1: 'x', player2: 'o'}
        print(f'{player1}, your sign is: {mapping[player1]}\n{player2}, your sign is: {mapping[player2]}')

        size = int(input("Enter the size of the grid: "))
        game_st = generate_game_state(size)
        print("\nLet's start the game!\n")
        display_grid(game_st)
        return game_st, mapping, player1, player2

    def start_game(game_st, mapping, player1, player2):
        curr_player = random.choice([player1, player2])
        size = len(game_st)
        total_moves = size ** 2
        for turn in range(total_moves):
            print(f"\n{curr_player}'s turn:")
            
            while True:
                try:
                    row = int(input("Enter row number: ")) - 1
                    col = int(input("Enter column number: ")) - 1

                    if 0 <= row < size and 0 <= col < size:
                        if game_st[row][col] == ' ':
                            game_st[row][col] = mapping[curr_player]
                            break
                        else:
                            print("That location is already occupied, please choose a different spot.")
                    else:
                        print("Invalid row or column, please enter a number between 1 and", size)
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            display_grid(game_st)

            # Check for a winner after 5 moves have been made
            if turn >= (size * 2) - 1:
                status, winner = check_winner(game_st, player1, player2)
                if status:
                    return winner

            # Switch players
            curr_player = player2 if curr_player == player1 else player1

        # If no winner, it's a draw
        return None

    def stop_game(winner):
        if winner:
            print(f"\nCongratulations {winner}! You won the game!")
        else:
            print("\nIt's a draw!")

    # Start the game process
    game_st, mapping, player1, player2 = initialization()
    winner = start_game(game_st, mapping, player1, player2)
    stop_game(winner)

# Run the game
xo_game()

