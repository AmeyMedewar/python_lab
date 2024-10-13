'''1st display the table:
display(size)

in initialization ask user for name and assign x and o to them 
in start game ask user for location then display the grid it should be updated 
after 5 attempts check the winner 
'''
import random
def display_grid(game_st):
    size = len(game_st)
    print('--'*size*2,sep='')
    for i in range(0,size):
        print('|',end='')
        for j in range(0,size):
            print(f' {game_st[i][j]} ',end='|')
        print('')
        print('--'*size*2,sep='')
      
      
def generate_game_state(size):
    row = [' ']*size
    arr=[]
    for i in range(size):
        arr.append(row.copy())
    return arr
    
    
def check_winner(game_st, player1, player2):
    # Check rows
    for row in game_st:
        if ' ' not in row:
            if len(set(row)) == 1:
                if row[0] == 'x':
                    return True, player1
                else:
                    return True, player2
    # Check columns
    for col in list(zip(*game_st)):
        if ' ' not in col:
            if len(set(col)) == 1:
                if col[0] == 'x':  
                    return True, player1
                else:
                    return True, player2

    main_diag = [game_st[i][i] for i in range(len(game_st))]
    if ' ' not in main_diag:
        if len(set(main_diag)) == 1:
            if main_diag[0] == 'x':
                return True, player1
            else:
                return True, player2

    anti_diag = [game_st[i][len(game_st)-1-i] for i in range(len(game_st))]
    if ' ' not in anti_diag:
        if len(set(anti_diag)) == 1:
            if anti_diag[0] == 'x':
                return True, player1
            else:
                return True, player2
    return False, 0


def xo_game():
    def initialization():
        print("This will be a 2 player game each player will get chance one by one the one who finishes the conditions first will win")
        player1 = eval(input("Enter name of first player "))
        player2 = eval(input("Enter name of second player "))
        mapping ={player1:'x',player2:'o'}
        print(f'{player1} your sign is :{mapping[player1]} \n{player2} your sign is {mapping[player2]}\n')
        
        size = eval(input("Enter the Size "))
        game_st = generate_game_state(size)
        print("\nLet's start the game\n")
        display_grid(game_st)
        return game_st, mapping, player1, player2
        
    def start_game(game_st, mapping, player1, player2):
        curr_player = random.choice([player1,player2])
        status = False
        size = len(game_st)
        for tries in range(size**2):
            print(f'{curr_player} enter your location')
            row = eval(input("Enter row number "))-1
            column =eval(input("Enter column number "))-1
            try:
                if game_st[row][column] not in ['x','o']:
                    game_st[row][column] = mapping[curr_player]
                else:
                    print('This location is already occupied')
            except:
                print("Invalid Location")
                
            display_grid(game_st)
            
            if curr_player == player1:
                curr_player = player2
            else:
                curr_player=player1
            if tries>(size*2)-1:
                status,winner = check_winner(game_st, player1, player2)
            if status:
                return winner
        status,winner = check_winner(game_st, player1, player2)
        if status:
                return winner
        else:
            return 0
    
    
    def stop_game(winner):
        if winner ==0:
            print("It's a draw")
        else:
            print(f'{winner} won the game!!!')


            
    game_st, mapping, player1, player2 = initialization()
    winner = start_game(game_st, mapping, player1, player2)
    stop_game(winner)
    
xo_game()
