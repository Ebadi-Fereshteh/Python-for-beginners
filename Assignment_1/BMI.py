
flag = True

while flag:

    weight = float(input(' please Enter your weight (kg):  '))
    Height = float(input(' please Enter your height (m):  '))

    BMI = round ((weight / Height ** Height), 1)

    print ('BMI = ', BMI)

    if BMI < 18.5 :
        result = 'Underweight'
    elif 18.5 <= BMI <= 24.9 :
        result = 'Normal'
    elif 25 <= BMI <= 29.9 :
        result = 'Overweight'
    elif 30 <= BMI <= 34.9 :
        result = 'Obese'
    elif BMI > 35 :
        result = 'Extremely obese'

    print(result)

    answer = input('try again? (y/n)  ')

    if answer == 'n':
        flag = False