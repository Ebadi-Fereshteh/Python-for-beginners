print("Enter snake length:")
len = int(input())
snake = ['O_']
if len>0:
    for i in range(1,len):
        if i%2 ==0:
            snake.append('#')
        else:
            snake.append('@')
print("n= ",len)
print(''.join(snake))