# def compute():
from numpy import zeros

n = int(input(('Enter khayam number: ')))
nums = zeros(n+1)

s = n-1
nums[s] = 1
for i in range(n):
    print()
    for j in range(s):
        print(' ',end=' ')
    for j in range(i+1):
        temp = nums[s+j] + nums[s+j+1]
        print(int(temp),' ', end=' ')
        nums[s+j]= temp
    print()
    s = s-1

print()
