print("Enter a number")
n = int(input())
print("Now enter the numbers in the array!")

list_nums=[]
for i in range(n):
    print("num ",i+1,":")
    list_nums.append(int(input()))

if sorted(list_nums) == list_nums:
    print("list_nums is sort!")
else:
    print("list_nums is not sort!")