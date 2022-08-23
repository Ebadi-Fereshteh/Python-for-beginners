from asyncio.windows_events import NULL
from itertools import product
import qrcode
from tabulate import tabulate as tbl

def show_menu():
    print('1- Add product')
    print('2- Edit product')
    print('3- Delete Product')
    print('4- Search')
    print('5- Show list')
    print('6- Qrcode')
    print('7- Buy')
    

def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])

def load(flag):
    if flag:
          print('Loading...')
    
    # read data from file
    mydata = open('fereshtehStore/database.txt','r')
    data = mydata.read()

    # split eack line from file
    product_list = data.split('\n')
    # print(product_list)
    for i in range(len(product_list)):
        #split each column from 
        product_info = product_list[i].split(',')
        # print(product_info)
        
        #create dictionary
        mydict = {}
        mydict['id'] = product_info[0]
        mydict['name'] = product_info[1]
        mydict['price'] = product_info[2]
        mydict['count'] = product_info[3]

        #create list of dictionary
        PRODUCTS.append(mydict)
    if flag:
        print('Welcome')

def add_product():
    print('--------------------- Enter the new product information ---------------------')
    print()
    flag = True
    id = int(input('id: '))
    for i in range(len(PRODUCTS)):
      if PRODUCTS[i]['id']==str(id) or PRODUCTS[i]['id']== id :
        print('The id must be unique, please check it!')
        add_product()
        flag=False
        break
        
    if flag:
        name = input('name: ')
        price = float(input('price: '))
        count = int(input('count: '))
        mydata = open('fereshtehStore/database.txt','a+')
        mydata.write('\n{}'.format(id))
        mydata.write(',{}'.format(name))
        mydata.write(',{}'.format(price))
        mydata.write(',{}'.format(count))
        print('\n -----------------------------  successful --------------------------------')

def edit_product():
        print('--------------------- Edit the products ---------------------')
        print()
        id = int(input('Enter the product ID: '))
        for i in range(len(PRODUCTS)):
            if PRODUCTS[i]['id']== str(id):
                
                print(PRODUCTS[i],'\n') 
                print('Edit or press Enter for each field')    
                new_name = input('name: ')
                new_price = input('price: ')
                new_count = input('count: ')
                
                # with is like your try .. finally block in this case
                with open('fereshtehStore/database.txt', 'r') as file:
                    # read a list of lines into data
                    mydata = file.readlines()
                # now change the 2nd line, note that you have to add a newline
                newStr = PRODUCTS[i]['id']
                # and write everything back
                with open('fereshtehStore/database.txt', 'w') as file:
                    
                    if new_name == "": 
                        newStr = newStr + ','+ PRODUCTS[i]['name']
                    else:
                        newStr = newStr + ','+ new_name
                        
                
                    if new_price=="":
                        newStr = newStr + ','+ PRODUCTS[i]['price']
                    else:
                        newStr = newStr + ','+ new_price
                        
                    
                    if new_count=="":
                        newStr = newStr + ','+ PRODUCTS[i]['count']
                    else:
                        newStr = newStr + ','+ new_count

                    
                    mydata[i] = newStr+'\n'

                    file.writelines(mydata)
                    print('\n -----------------------------  successful --------------------------------')
                break

            else:
                if i == len(PRODUCTS) -1:
                    print('This product dose not exist!')
                    edit_product()
                    break

def search_product():
    print('\n -----------------------------  search product --------------------------------')
    key = input('Enter the name of product or part of it: ')
    flag = True
    for i in range(len(PRODUCTS)):
        if key in PRODUCTS[i]['name']:
            print('\n These products were found: \n')
            print(PRODUCTS[i])
            flag = False
        if i == (len(PRODUCTS) - 1) and flag:
            print('No products found!')

    print('\n -------------------------------------------------------------')

def create_qrcode():
    pid = int(input('Enter the product id: '))
    for i in range(len(PRODUCTS)):
        if str(pid) == PRODUCTS[i]['id']:
            img = qrcode.make(PRODUCTS[i])
            img.save(str(PRODUCTS[i]['name'])+'.png')
            print('\n ----------------create qrcode: '+str(PRODUCTS[i]['name'])+'.png-------------------')
            break
        else:
            if i == (len(PRODUCTS)-1):
                print('No ID found!')
    
def delete_product():
    print('--------------------- Delete the product ---------------------')
    print()
    id = int(input('Enter the product ID: '))
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id']== str(id):            
            print(PRODUCTS[i],'\n') 
            sure = input('Are you sure to delete this product? (y/n) :  ')    
            if sure == 'y':            
                # with is like your try .. finally block in this case
                with open('fereshtehStore/database.txt', 'r') as file:
                    # read a list of lines into data
                    mydata = file.readlines()
                # now change the 2nd line, note that you have to add a newline
                newStr = PRODUCTS[i]['id']
                # and write everything back
                with open('fereshtehStore/database.txt', 'w') as file:
                    if i == len(PRODUCTS)-1:
                        s = mydata[0:i-1]
                        print(s)
                        s2 = mydata[i-1:i]
                        print(s2)
                        # [for '\n' in iterable if condition]
                        # s2 = [for s2 in mydatas2.replace('\n','')
                        new_s2=[]
                        for i in s2:
                          new_i = i.replace('\n', '')
                          
                          # Modify old string
                          new_s2.append(new_i)
                          print(new_s2)
                        s3 = s + new_s2
                        print(s3)
                    elif i == 0:
                        s2 = mydata[i+1:len(mydata)]
                        s3 = s2
                    else:
                        s = mydata[0:i]
                        s2 = mydata[i+1:len(mydata)]
                        s3 = s + s2
                    #  mydata[i] = s + s2
                    file.writelines(s3)
                    print('\n -----------------------------  successful --------------------------------')
                break

        else:
            if i == len(PRODUCTS) -1:
                print('This product dose not exist!')
                delete_product()
                break
def print_factor():
    total=0
    print('--------------------- Order Total ---------------------')
    print()
    col =  ['number','name', 'quantity', 'unit price', 'total price']
    factor=[]
    # print(tbl([(user_cart[:]['name'], str(user_cart[:]['count']),user_cart[:]['price'], ((float(user_cart[:]['count']) * float(user_cart[:]['price']))))], tablefmt="pipe"))
    # print(tbl((), headers=col, tablefmt="pipe"))
    for i in range(len(user_cart)):
        sum = (float(user_cart[i]['count']) * float(user_cart[i]['price']))
        total = total + sum
        factor.append([str(i+1),user_cart[i]['name'], str(user_cart[i]['count']), user_cart[i]['price'], str(sum)])
    factor.append(['','Total','','',str(total)])   
    print(tbl(factor, headers=col, tablefmt="fancy_grid" ))    
    print()
    user_factor = open('fereshtehStore/cart_factor.txt','w')
    
    for i in range(len(factor)):
        user_factor.write(','.join(factor[i][:])+'\n')
    
    # convert list of dictionary to list
    data_list = []
    for i in range(len(PRODUCTS)):
        get_listVal = list(PRODUCTS[i].values())
        data_list.append(get_listVal)
    
    
    mydata = open('fereshtehStore/database.txt','w')
    for i in range(len(data_list)):
        mydata.write(','.join(data_list[i][:])+'\n')

    print('------------------------------- Save data successful----------------------------------')

def shopping():
    print('--------------------- shopping ---------------------')
    print()
    id = int(input('Enter the product ID: '))
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['id']== str(id):            
            print(PRODUCTS[i],'\n') 
            num = int(input('Quantity? '))  
            if num <= int(PRODUCTS[i]['count']):
                PRODUCTS[i]['count'] = str(int(PRODUCTS[i]['count']) - num)
                temp = PRODUCTS[i].copy()
                user_cart.append(temp)
                user_cart[len(user_cart)-1]['count'] = num 

                next_p = input('Do you have another purchase? (y/n) > ')
                if next_p == 'y':
                    shopping()
                else:
                    print_factor()
                    break

                
            else:
                print('Not enough stock') 
                next_p = input('Do you have another purchase? (y/n) > ')
                if next_p == 'y':
                    shopping()
            
            break

        else:
            if i == len(PRODUCTS) -1:
                print('This product dose not exist!')
                shopping()
                break

user_cart=[]
PRODUCTS = []
flag=True
load(flag)

#pyfiglet
from pyfiglet import Figlet
#shop logo!
f = Figlet(font= 'standard')
print(f.renderText('Fereshteh Shop'))



show_menu()







choice = int(input('please choose a number: '))
# choice= 7

if choice ==1:
    add_product()
    flag = False
    load(flag)
    
elif choice == 2:
    edit_product()
    flag = False
    load(flag)

elif choice == 3:
    delete_product()

elif choice == 4:
    search_product()

elif choice == 5:    
    show_list()

elif choice == 6:
    create_qrcode()
    
elif choice == 7:
    shopping()

# 1001,Doogh,14000,6
# 1002,chips,10000,10
# 1003,pofak,3000,2
# 1004,bastani,15000,8