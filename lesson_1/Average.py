import statistics

flag = True

while flag:
    
    
    name = input('Enter your name : ')
    family = input('Enter your family : ')
    C1 = float(input('Enter math score : '))
    C2 = float(input('Enter science score : '))
    C3 = float(input('Enter English score : '))

    Average = statistics.mean([C1,C2,C3])
    
    if Average >= 17 :
        result = 'Grate'
    elif 12 <= Average < 17 :
        result = 'Normal'
    elif Average < 12 :
        result = 'Fail'
    
    print( name, ' ', family, ' status is ', result)

    answer = input('try again? (y/n)  ')

    if answer == 'n':
        flag = False
