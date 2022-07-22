import random
print("Press the Enter button and roll the dice!!")
while True:    
    key = input()
    if key == '' :
        dice = random.randint(1, 6)
        print(dice)
        if dice == 6:
            print("Bonus! Roll the dice again")
        else:
            break
    else:
        print("Press Enter key!")
