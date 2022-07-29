def Checker_board(m, n):
    for i in range(m):
        for j in range(n):
            if i%2 ==0:
                print("*", end='')
                print("#", end='')
            else:
                print("#", end='')
                print("*", end='')

        print('')

print("Set the board size: ")
print("Width= ", end='')
m = int(input())
print("Height= ", end='')
n = int(input())
print('')
print("checkerboard:")
print('')
Checker_board(m, n)