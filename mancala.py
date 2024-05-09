import random


def startgame():
    # index 0 is player 1s points and index 7 is player 2s points
    board = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
    return board

def displayboard(board):
    print("-----------------") 
    temp="| |"
    for i in range(12,6,-1):
        temp+=str(board[i])+"|"
    print(temp+" |")
    print("|"+str(board[13])+"-------------"+str(board[6])+"|")
    temp="| |"
    for i in range(0,6):
        temp+=str(board[i])+"|"
    print(temp+" |")
    print("-----------------") 

def playermove(board):
    selection = 10
    valid= [0,1,2,3,4,5]
    opposite = {0:12,1:11,2:10,3:9,4:8,5:7}

    while selection not in valid or board[selection] == 0: 
        selection = int(input("Give number between 1 and 6: "))-1
    
    landed = selection + board[selection]
    playerturn = landed == 6

    board = action(board, selection)

    if board[landed] == 1 and landed in opposite.keys() and board[opposite[landed]]!= 0: # square was empty beforehand 
        tokens = 1 + board[opposite[landed]]
        board[6] += tokens
        board[landed] = 0
        board[opposite[landed]] = 0
    return board, playerturn
    
def computermove(board):
    opposite = {12:0,11:1,10:2,9:3,8:4,7:5}
    selection = random.randint(7,12)
    while board[selection] == 0: selection = random.randint(7,12)

    landed = (selection + board[selection]) % 13
    if landed > 13: landed = landed - 14
    playerturn = selection + board[selection] != 13
    board = action(board,selection)

    if board[landed] == 1 and landed in opposite.keys() and board[opposite[landed]]!= 0: # square was empty beforehand 
        tokens = 1 + board[opposite[landed]]
        board[13] += tokens
        board[landed] = 0
        board[opposite[landed]] = 0

    return board, playerturn



def action(board, selection):
    tokens = board[selection]
    board[selection] = 0
    index = selection
    while tokens != 0:
        index += 1
        if index > 13: index = 0
        board[index] += 1
        tokens -= 1
    return board

        
def checkendgame(board):
    print(sum(board[0:6]))
    if sum(board[0:6])==0:
        print("player 1 has no more")
        board[13] = sum(board[7:13])
        board[7:13] = [0 for x in board[7:13]]
        return True, board
    print(sum(board[7:13]))
    if sum(board[7:13])==0:
        print("player 2 has no more")
        board[6] = sum(board[0:6])
        board[0:6] = [0 for x in board[0:6]]
        return True, board
    return False, board
        


def main():
    board = startgame()
    displayboard(board)
    playerturn = True
    endgame = False
    while not endgame:
        if playerturn:
            board, playerturn = playermove(board)
            print("player move")
            displayboard(board)
        else:
            board, playerturn = computermove(board)
            print("computer move")
            displayboard(board)
        endgame,board = checkendgame(board)
    displayboard(board)


main()


    
