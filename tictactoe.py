#As the game goes on I have to check a user if they try and put down an 'X' or an 'O' in a spot that is already taken up
#To go about this I need to have an if-statement that checks the position of 'slots_on_board' with the number that was entered by the user
#
#X goes first --- turn = 'X'

#This function will draw the board when called
def draw_board():
    print("-------------------")
    print("|     |     |     |")
    print(f"|  {slots_on_board[0]}  |  {slots_on_board[1]}  |  {slots_on_board[2]}  |")
    print("|     |     |     |")   
    print("-------------------")
    print("|     |     |     |")
    print(f"|  {slots_on_board[3]}  |  {slots_on_board[4]}  |  {slots_on_board[5]}  |")
    print("|     |     |     |")
    print("-------------------")
    print("|     |     |     |")
    print(f"|  {slots_on_board[6]}  |  {slots_on_board[7]}  |  {slots_on_board[8]}  |")
    print("|     |     |     |")
    print("-------------------")
    
    
#Very inefficient function. Need to find another solution for detecting a win    
def detect_win(array):
    if(array[0] == 'X' and array[3] == 'X' and array[6] == 'X'):
        print("Player 'X' has won!")
        draw_board()
        quit()
        
    if(array[1] == 'X' and array[4] == 'X' and array[7] == 'X'):
        print("Player 'X' has won!") 
        draw_board()
        quit()
        
    if(array[2] == 'X' and array[5] == 'X' and array[8] == 'X'):
        print("Player 'X' has won!") 
        draw_board()
        quit()                 
    
    if(array[0] == 'O' and array[3] == 'O' and array[6] == 'O'):
        print("Player 'O' has won!")
        draw_board()
        quit()
        
    if(array[1] == 'O' and array[4] == 'O' and array[7] == 'O'):
        print("Player 'O' has won!") 
        draw_board()
        quit()
        
    if(array[2] == 'O' and array[5] == 'O' and array[8] == 'O'):
        print("Player 'O' has won!")
        draw_board()
        quit()
#End of column wins        
        
    if(array[0] == 'X' and array[1] == 'X' and array[2] == 'X'):
        print("Player 'X' has won!")
        draw_board()
        quit()
        
    if(array[3] == 'X' and array[4] == 'X' and array[5] == 'X'):
        print("Player 'X' has won!") 
        draw_board()
        quit()
        
    if(array[6] == 'X' and array[7] == 'X' and array[8] == 'X'):
        print("Player 'X' has won!")   
        draw_board()
        quit()               
    
    if(array[0] == 'O' and array[1] == 'O' and array[2] == 'O'):
        print("Player 'O' has won!")
        draw_board()
        quit()
        
    if(array[3] == 'O' and array[4] == 'O' and array[5] == 'O'):
        print("Player 'O' has won!") 
        draw_board()
        quit()
        
    if(array[6] == 'O' and array[7] == 'O' and array[8] == 'O'):
        print("Player 'O' has won!")
        draw_board()
        quit()
#End of row wins    

    if(array[0] == 'X' and array[4] == 'X' and array[8] == 'X'):
        print("Player 'X' has won!")
        draw_board()
        quit()
        
    if(array[2] == 'X' and array[4] == 'X' and array[6] == 'X'):
        print("Player 'X' has won!") 
        draw_board()
        quit()
        
    if(array[0] == 'O' and array[4] == 'O' and array[8] == 'O'):
        print("Player 'O' has won!")  
        draw_board()
        quit()                
    
    if(array[2] == 'O' and array[4] == 'O' and array[6] == 'O'):
        print("Player 'O' has won!")
        draw_board()
        quit()
#End of diagonal wins           
    
#Variables declared underneath here
slots_on_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
turn = 'X'
did_win = False


print("Hello gamers, ready to play TIC TAC TOE?\n")
print("Choose a number 0-8 to put an 'X' or 'O' on the board.")
print("The top left spot correlates with the number 0 and the bottom right spot correlates with the number 8.")
for j in range(9):
    draw_board()
    
    if(turn == 'X'):
        print("Player 'X' GO: ")
        x = int(input())
   
#The for loop below will check if a spot on the game board is already taken up. 
#If it is then the user will be notified and asked to put another number in
#This also applies to the for loop underneath the player 'O' input      
        for k in range(100):
            if(slots_on_board[x] == 'X' or slots_on_board[x] == 'O'):
                print("This spot is already taken up silly goose. Try again: ")
                x = int(input())
            if(slots_on_board[x] == ' ' or slots_on_board[x] == ' '):
                break
            
        slots_on_board[x] = 'X'
        detect_win(slots_on_board)
        turn = 'O'
    else:
        print("Player 'O' GO: ")
        x = int(input())

        for m in range(100):
            if(slots_on_board[x] == 'X' or slots_on_board[x] == 'O'):
                print("This spot is already taken up silly goose. Try again: ")
                x = int(input())
            if(slots_on_board[x] == ' ' or slots_on_board[x] == ' '):
                break
                           
        slots_on_board[x] = 'O'
        detect_win(slots_on_board)
        turn = 'X'
        
    
draw_board()
print("Nobody won. Y'all kinda suck")
        
    