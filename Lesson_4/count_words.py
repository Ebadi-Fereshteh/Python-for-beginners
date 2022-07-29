print("Type your favorite statement!!")
str = input()

# You have to work hard to succeed
def countWords(str):
    count=1
    for pos, char in enumerate(str):
        if(char==' '):
            count= count+1
    print("The number of words is equal to: ")
    print(count)

countWords(str)

