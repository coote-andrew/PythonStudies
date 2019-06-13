#Tic-Tac-Toe

#top-L, top-M, top-R
#mid-L, mid-M, mid-R
#low-L, low-M, low-R
import pprint
import time

theBoard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' ',}

reset = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' ',}

score = {'X':0, 'O':0}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def solutions(board):
    #Horizontal
    if board['top-L'] == board['top-M'] and board['top-L'] == board['top-R'] and board['top-L'] != ' ':
        return True
    elif board['mid-L'] == board['mid-M'] and board['mid-L'] == board['mid-R'] and board['mid-L'] != ' ':
        return True
    elif board['low-L'] == board['low-M'] and board['low-L'] == board['low-R'] and board['low-L'] != ' ':
        return True
    #Vertical
    elif board['top-L'] == board['mid-L'] and board['top-L'] == board['low-L'] and board['top-L'] != ' ':
        return True
    elif board['top-M'] == board['mid-M'] and board['top-M'] == board['low-M'] and board['top-M'] != ' ':
        return True
    elif board['top-R'] == board['mid-R'] and board['top-R'] == board['low-R'] and board['top-R'] != ' ':
        return True
    #Diagonal
    elif board['top-L'] == board['mid-M'] and board['top-L'] == board['low-R'] and board['top-L'] != ' ':
        return True
    elif board['top-R'] == board['mid-M'] and board['top-R'] == board['low-L'] and board['top-R'] != ' ':
        return True
    else:
        return False



    
turn = 'X'
while True:
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    if move == '':
        break
    elif move == 'score':
        print('The current scores are:')
        print('X: ' + str(score['X']) + ' to O: ' + str(score['O']))
    else:
        try:
            if theBoard[move] != ' ':
                print('That position is already taken, try another!')
            else:
                theBoard[move] = turn
                if solutions(theBoard):
                    print('Congratulations ' + turn + ', you won!')
                    score[turn] = str(score[turn] + 1)
                    print('The current scores are:')
                    print('X: ' + str(score['X']) + ' to O: ' + str(score['O']))
                    print()
                    print()
                    print()
                    print('play again!')
                    theBoard = reset
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
        except KeyError:
            print()
            print('that is not a valid position, sorry! Try again!')
            print('the options for rows are: top, mid, low')
            print('the options for columns are: L, M, R')
            print('and are separated with a dash. eg. top-L')
            print()
            print('Your go again!')
            time.sleep(1)
            continue
    
printBoard(theBoard)



