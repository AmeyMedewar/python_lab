import random
def guess_the_number():
    def initialization():
        difficulty = eval(input("Enter a difficulty level between 1 to 5"))
        ranges = [(1,3),(1,5),(1,10),(1,25),(1,50)]
        if difficulty>5 or difficulty<0:
            print("The Difficulty level is unavailable selecting a random difficulty for you")
            difficulty = random.randint(1,5)
        start = ranges[difficulty-1][0]
        end = ranges[difficulty-1][1]
        return random.randint(start,end),start,end

    
    
    def start_game(computer_generated_number, start, end):
        users_number = eval(input(f"You Have to guess a number between {start} to {end}\n"))
        return users_number == computer_generated_number
        
    def stop_game(status):
        if status:
            print("Congratulations you got it")
        else:
            print("You lose the game ")
    
    computer_generated_number,start,end = initialization()
    status = start_game(computer_generated_number, start,end)
    stop_game(status)

    
guess_the_number()
        
    
    
