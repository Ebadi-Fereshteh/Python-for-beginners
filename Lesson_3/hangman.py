import random

words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']

word = random.choice(words) 
# print(word)
life = 7

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
      ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

guess_str = ['_ ']* len(word)
print(guess_str[:])

while life > 0:   
    
    print("Guess a letter (",(7-life)+1,")")
    user_character = input().lower() # s
    
    if user_character in word:
        print('yes! your guess is correct!')
        for pos, char in enumerate(word):
            if(char== user_character):
                guess_str[pos]= user_character
        print(guess_str[:])
        if '_ ' in guess_str:
            continue
        else:
            print("Congratulations! You Win!")
            exit()
    else:
        print('oops! your guess is wrong!')
        print(HANGMAN_PICS[(7-life)])
        if life == 1:
            print("Oops! Yuo Loss!")
            exit()
        else:
            life = life - 1
        print("--------------------------------")
