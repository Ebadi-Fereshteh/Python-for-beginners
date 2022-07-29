def multi_gen(m, n):
    multi_list= [[0]*(m+1)]*(n+1)
    
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 and j==0):
                multi_list[i][j]="x"
                print("\x1b[6;30;43m X  | \x1b[0m",end='')

            elif(i==0 and j!=0):
                multi_list[i][j]=j

                if(j<10):
                    print("\x1b[6;30;43m",j,"  |\x1b[0m",end='')
                else:
                    print("\x1b[6;30;43m",j," | \x1b[0m",end='')

            elif(i!=0 and j==0):
                multi_list[i][j]=i

                if(i<10):
                    print("\x1b[6;30;43m",i," | \x1b[0m",end='')
                else:
                    print("\x1b[6;30;43m",i,"| \x1b[0m",end='')

            elif(i==j):
                multi_list[i][j] = i*j

                if(i*j < 10):
                    print("\x1b[6;30;43m",i*j,"  |\x1b[0m",end='')
                elif(i*j>99):
                    print("\x1b[6;30;43m",i*j,"|\x1b[0m",end='')
                else:
                    print("\x1b[6;30;43m",i*j," |\x1b[0m",end='')

            else:
                multi_list[i][j] = i*j

                if(i*j < 10):
                    print("\033[1;0m",i*j,"  |",end='')
                else:
                    print("\033[1;0m",i*j," |",end='')

        print('')
    

print("Set the table size:")
print("m=",end='')
m = int(input())
print("n=",end='')
n = int(input())
multi_gen(m,n)   
