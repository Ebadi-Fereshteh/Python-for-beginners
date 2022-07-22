fib = [0, 1]
print("Enter the number of Fibonacci series: ")
count = int(input())
if count == 1:
    print("fib= ",fib[0])
elif count == 2:
    print("fib= ",fib[:])
else:
    for j in range(2, count):
        f = fib[j-1]+fib[j-2]
        fib.append(f)
    print("fib= ",fib[:])
    
