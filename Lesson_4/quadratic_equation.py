from cv2 import sqrt


def quadratic(a, b, c):
    delta = b*b - (4*a*c)
    print("delta= ",delta)
    if delta > 0:
        x1 = (1/(2*a))*((-1*b) + sqrt(delta))
        x2 = (1/(2*a))*(-1*b - sqrt(delta))
        print("x1= ",x1[0])
        print("x2= ",x2[0])
    elif delta == 0:
        x = (1/(2*a))*(-1*b)
        print("x1= x2= ",x)
    elif delta < 0:
        print("The above equation does not have an answer in real numbers!")

print("Enter the parameters of the equation")
print("a= ",end='')
a= float(input())
print("b= ",end='')
b= float(input())
print("c= ",end='')
c= float(input())
print("f = ",a,"x^2+",b,"x+",c)
print("result:")
quadratic(a, b, c)



