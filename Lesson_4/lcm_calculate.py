print("Enter two number: ")
print("x=",end='')
x= int(input())
print("y= ", end='')
y= int(input())

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    for i in range(greater, x*y+1):
        if(i % x ==0 and i % y ==0):
            lcm_result= i
            print("LCM(",x,",",y,") = ",lcm_result)
            break

lcm(x, y)



