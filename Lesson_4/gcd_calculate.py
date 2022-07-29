def gcd(x, y):
    if x < y:
        smaller = x
    else:
        smaller = y
    
    for i in range(1, smaller+1):
        if(x % i == 0 and y % i ==0):
            gcd_result= i
    print("GCD(",x,",",y,") = " ,gcd_result)

print("Enter two number: ")
print("x=",end='')
x= int(input())
print("y= ", end='')
y= int(input())
gcd(x, y)


