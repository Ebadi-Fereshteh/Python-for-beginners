import random
flag = True
while flag:
    print("Enter the number: ")
    n = int(input())
    # rand_list = []
    rand_num = random.sample(range(n*2),n)
    print(rand_num[:])
    print("try again?(Y/N)")
    while True:
        result = input()
        if result.lower() =='y':
            flag= True
            break
        elif result.lower() =='n':
            flag= False
            break
        else:
            print("try again?(Y/N)") 

    

