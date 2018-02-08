# Printing pattern

num = int(input("Please enter number: "))
for i in range(1,num+1):
    for x in range(i,num):
        if i < num:
            print('',end = '  ')
        
    for x in range(i,0,-1):
        print(x, end = ' ')
        
    print()

        
 

          
