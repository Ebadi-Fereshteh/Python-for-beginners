import math
flag = True
while flag:
    a = float(input('Input number a: '))
    operator = input('Input operator type between ( +, -, *, /, radical, sin, cos, tan, cot, factorial): ')

    if operator == '+' or operator == '-' or operator == '*' or operator == '/' :
        b = float(input('Input number b: '))
        
        if operator == '/':
            if b == '0':
                result = 'cannot divide by zero!'
            else:
                result = eval(str(a) + ' ' + operator + ' ' + str(b))
        else:
                result = eval(str(a) + ' ' + operator + ' ' + str(b))

    elif operator == 'radical':
        result = math.sqrt(a)

    elif operator == 'factorial':
        result = math.factorial(a)

    elif operator == 'sin' or operator == 'cos' or operator == 'tan':
        result = eval('math.' + operator + '(math.radians(' + str(a) + '))')
        result = round(result,2)
        if result == 1.633123935319537e+16:
            result = 'undefined'

    elif operator == 'cot':
        operator = 'tan'
        result = eval('math.' + operator + '(math.radians(' + str(a) + '))')
        result = round(result,2)
        if result == 1.633123935319537e+16:
            result = 0
        elif result == 0:
            result = 'undefined'
    else:
        result = 'invalid operator'

    print('result = ', result)

    answer = input('try again? (y/n)  ')

    if answer == 'n':
        flag = False
 

