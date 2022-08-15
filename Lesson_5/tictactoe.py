from colorama import init, Fore, Back, Style
from numpy import zeros, sum, where
import random
from datetime import datetime
init(autoreset=True)

player = 'X'  # default

# menu
print('Menu')
print('1- p1 VS p2')
print('2- p1 VS computer')
type_game = int(input('choose one number from menu: '))
print()
start_time = datetime.now()

def show_game_board():
        for i in range(3):
                print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.BLACK +'| ', end='')
                for j in range(3):
                        if j<2:
                                if game[i][j] == 'X':
                                        print(Style.DIM + Back.WHITE + Fore.RED +' '+ game[i][j]+  Fore.BLACK + '  | ', end='')
                                elif game[i][j] == 'O':
                                        print(Style.DIM + Back.LIGHTWHITE_EX + Fore.BLUE +' '+ game[i][j]+ Fore.BLACK + '  | ', end='')
                                else:
                                        print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.BLACK +' '+ game[i][j]+'  | ', end='')
                        else:
                                if game[i][j] == 'X':                                        
                                        print(Style.DIM + Back.WHITE + Fore.RED +' '+ game[i][j]+  Fore.BLACK + '  |', end='')
                                elif game[i][j] == 'O':
                                        print(Style.DIM + Back.LIGHTWHITE_EX + Fore.BLUE +' '+ game[i][j]+ Fore.BLACK + '  |', end='')
                                else:
                                        print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.BLACK +' '+ game[i][j]+'  |', end='')
                                
                print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.BLACK)
                print(Style.BRIGHT + Back.LIGHTWHITE_EX + Fore.BLACK +'+-----+-----+-----+')
def check_win(p):
        
        result= zeros((3, 3))
        result_d = zeros((3, 2))
        equal_game = zeros((3, 3))

        # print('res=',result)
        
        for i in range(3):
                for j in range(3):
                        if game[i][j] == p:
                                result[i][j]= 1
                        else:
                                result[i][j]= 0
                        if game[i][i] == p:
                                result_d[i][0]= 1
                        
                        if game[i][3-1-i] == p:
                                result_d[i][1]= 1
                        if game[i][j] != '_':
                                equal_game[i][j] = 1

        result_cols = sum(result,axis=0) 
        result_rows = sum(result,axis=1)  
        result_diagonal = sum(result_d, axis=0)
        result_equal = sum(sum(equal_game))

        # print('r1= ',result_cols)
        # print('r2= ',result_rows)
        # print('r3= ',result_diagonal)
        # print('r4= ',result_equal)

        if (3 in result_cols or 3 in result_rows or 3 in result_diagonal ):
                print('player ',p,' win!')
                end_time = datetime.now()
                print('Duration: {}'.format(end_time - start_time))
                print()
                exit()
        else: 
                if result_equal == 9:
                        print('The game is equal!')
                        end_time = datetime.now()
                        print('Duration: {}'.format(end_time - start_time))
                        print()
                        exit()
                

        

game = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]

show_game_board()
while True:
        print()
        print("player 1:")
        player = 'X'
        while True:
                print()
                row = int(input('please insert row: '))
                col = int(input("please insert col: "))
                print()
                if 0 <= row <= 2 and 0<= col <= 2:
                        if game[row][col]=='_':
                                game[row][col] = 'X'
                                break
                        else:
                                print('cell is not empty!')
                else:
                        print('index out of range, try again!')
        show_game_board()
        check_win(player)

        if(type_game==1):
                print()
                print("player 2:")
                player = 'O'
                while True:
                        print()
                        row = int(input('please insert row: '))
                        col = int(input("please insert col: "))
                        print()
                        if 0 <= row <= 2 and 0<= col <= 2:
                                if game[row][col]=='_':
                                        game[row][col] = 'O'
                                        break   
                                else:
                                        print('cell is not empty!')
                        else:
                                print('index out of range, try again!')
        elif(type_game==2):
                print()
                print("computer:")
                player = 'O'
                while True:                        
                        row = random.randint(0,3)
                        col = random.randint(0,3)                        
                        if 0 <= row <= 2 and 0<= col <= 2:
                                if game[row][col]=='_':
                                        game[row][col] = 'O'
                                        break   
                        

        show_game_board()
        check_win(player)
