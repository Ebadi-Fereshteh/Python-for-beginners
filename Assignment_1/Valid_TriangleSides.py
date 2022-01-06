flag = True

while flag:
    
    
    a = float(input('Enter value a : '))
    b = float(input('Enter value b : '))
    c = float(input('Enter value c : '))

    if a < b + c : 
        validation = 'a is valid \n'
        if b < a + c :
            validation = validation + 'b is valid \n'
            if c < a + b :
                validation = validation + 'c is valid \n'
                result = 'result = draw your triangle!!'
            else:
                result = 'result = Invalid value c !! try again'
        else:
            result = 'result = Invalid value b !! try again'
    else:
        result = 'result = Invalid value a !! try again'
    
    print(validation)
    print(result)

    answer = input('try again? (y/n)  ')

    if answer == 'n':
        flag = False