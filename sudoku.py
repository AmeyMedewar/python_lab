import random
import copy
def display_sudoku(game_st):
    size = len(game_st)
    print('--' * size * 2, sep='')
    for i in range(size):
        print('|', end='')
        for j in range(size):
            if game_st[i][j] == ' ':
                print('   ', end='|')
            else:
                print(f' {game_st[i][j]} ', end='|')
        print('')
        print('--' * size * 2, sep='')



import random

def generate_game_state(size, difficulty):
    def generate_row(arr): 
        ret = []
        
        # Check how many rows we have already in arr
        current_size = len(arr)
        
        for i in range(size):
            col = list(range(1, size + 1))  # Start with all possible values for the column

            # Only remove elements already in the column if the column exists (i.e., current_size > 0)
            if current_size > 0:
                new_mat = list(zip(*arr))  # Transpose to get columns
                
                if i < len(new_mat):  # Ensure we don't try to access a column that doesn't exist yet
                    for ele in new_mat[i]:  # Remove elements already in the column
                        if ele in col:
                            col.remove(ele)

            # Remove elements already in the row (ret) to avoid duplicates in the same row
            for ele in ret:
                if ele in col:
                    col.remove(ele)

            # If there are no valid numbers left in the column, skip or retry
            if not col:
                return None  # Returning None indicates failure to generate a valid row

            # Randomly choose from remaining valid numbers
            ret.append(random.choice(col))  

        return ret
    
    arr = []
    for i in range(size):
        l = None
        while l is None:  # Retry generating a valid row until successful
            l = generate_row(arr)
        arr.append(l)
    
    solution_state = copy.deepcopy(arr)  # Solution state generated
    
    # Difficulty mapping: how much of the grid to remove
    difficulty_mapping = {1: 20, 2: 35, 3: 50}  # The higher the difficulty, the more elements are removed
    loss = int(size * size * difficulty_mapping[difficulty] * 0.01)  # Percentage of cells to be removed
    if loss==0:
        loss=1
    # Randomly remove values to create the puzzle from solution
    for _ in range(loss):
        row = random.choice(list(range(size)))  # Random row
        column = random.choice(list(range(size)))  # Random column
        arr[row][column] = ' '  # Empty the cell
    
    return arr, solution_state

def check_answer(game_st):
    size = len(game_st)
    
    # Check rows and columns
    for i in range(size):
        row = [x for x in game_st[i] if x != ' ']
        col = [x for x in list(zip(*game_st))[i] if x != ' ']
        if len(set(row)) != len(row) or len(set(col)) != len(col):
            return False
    
    return True

def sudoku_game():
    def initialization():
        print("Welcome to the sudoku game")
        size = int(input("Enter the Size (typically 9 for standard Sudoku): "))
        print("Please select a difficulty level\n1 : Easy\n2: Medium\n3 : Difficult")
        difficulty = int(input())
        game_st, solution = generate_game_state(size, difficulty)       
        return game_st, solution
        
    def start_game(game_st):
        print("Let's start the game")
        display_sudoku(game_st)
        
        for row in range(len(game_st)):
            for col in range(len(game_st[row])):
                if game_st[row][col] == ' ':  # Only allow input on empty cells
                    try:
                        value = int(input(f"Enter the value for [{row+1}][{col+1}] location (1-{len(game_st)}): "))
                        if value not in range(1, len(game_st) + 1):
                            print(f"Invalid input. Please enter a number between 1 and {len(game_st)}.")
                        else:
                            game_st[row][col] = value
                            display_sudoku(game_st)
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
        
        print("Let's see the result...")
        win = check_answer(game_st)
        return win
        
    def stop_game(win, solution):
        if win:
            print("Congrats, the answer is correct!!!")
        else:
            print("Sorry, you lose the game.")
            print("Correct answer:")
            display_sudoku(solution)
    
    # Start the game loop
    game_st, solution = initialization()
    win = start_game(game_st)
    stop_game(win, solution)
    
sudoku_game()

