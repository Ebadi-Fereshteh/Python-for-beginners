dictionary = []
def load():
    try:
        #open dictionary file
        dict_file = open('translate/dic.txt', 'r')

        # read from dict_file
        myData = dict_file.read().split('\n')
        
        for i in range(len(myData)):
            info = myData[i].split(',')
            dictionary.append({'English': info[0], 'persian': info[1]})

        print('------------------------ simple translate ------------------------')
        flag_load = True
    except:
        flag_load = False
        print('can\'t found dictionary file') 
    
    while flag_load:
        show_menu()
        choice = int(input('please select from menu:  '))
        if choice == 1:
            add_word()
        elif choice == 2:
            En2fa()
        elif choice == 3:
            fa2En()
        elif choice == 4:
            exit()
           

def show_menu():
    print('1- add new word')
    print('2- translation english2persian')
    print('3- translation persian2english')
    print('4- exit')


def add_word():    
    english_word = input('Enter an english word: ') 
    for i in range(len(dictionary)):
        if(dictionary[i]['English']== english_word):
            result = input('This word is in the dictionary, try again? (y/n): ')
            if result == 'y':
                add_word()
            else:
                flag = False
                break
        else:
            if (i == len(dictionary)-1):
                persian_word = input('Enter its persian translation: ')
                dictionary.append({'English': english_word, 'persian': persian_word})
                print('----------------- add word successfull -----------------')
                out = input('Do you want to add another word? (y/n) : ')
                if out == 'y':
                    add_word()
                else:
                    save_file()
                    exit
def save_file():
    f = open('translate/dic.txt','w')
    # data = f.read()
    # print(data)
    for k in range(len(dictionary)):
        row = dictionary[k]['English']+ ','+ dictionary[k]['persian']+'\n'
        # print(row)
        # last line write whithout \n
        if k == len(dictionary)-1:
            row = row.strip()
        f.write(row)
        f.flush()            
    f.close

def En2fa():
    print('----------------- translate english 2 persian  -----------------')
    stm = input('Enter your english sentence: ')
    stm_split = stm.split(' ')
    translate_fa = stm_split
    for i in range(len(stm_split)):
        for j in range(len(dictionary)):
            if(stm_split[i]== dictionary[j]['English']):
                translate_fa[i] = dictionary[j]['persian']
                break
            elif(stm_split[i]== dictionary[j]['English']+'.'):
                translate_fa[i] = dictionary[j]['persian']+'.'
                break            
    print(*translate_fa, sep=' ')
    result = input('try again? (y/n): ')
    if result== 'y':
        En2fa()
    
def fa2En():
    print('----------------- translate persian 2 english -----------------')
    stm = input('Enter your persian sentence: ')
    stm_split = stm.split(' ')
    translate_en = stm_split
    for i in range(len(stm_split)):
        for j in range(len(dictionary)):
            if(stm_split[i]== dictionary[j]['persian']):
                translate_en[i] = dictionary[j]['English']
                break            
    print(*translate_en, sep=' ')
    result = input('try again? (y/n): ')
    if result== 'y':
        fa2En()

load()