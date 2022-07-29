def checkFactorial(num):
    f= 2
    fact=1
    while True:
        fact = fact * f
        if num > fact:
            f = f + 1
        elif num == fact:
            print("Yes")
            exit()
        elif num < fact:
            print("No")
            exit()

print("Enter a positive integer")
num = int(input())
print("Is this a factorial number?")
checkFactorial(num)
