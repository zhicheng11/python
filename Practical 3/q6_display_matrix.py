import random
#print(random.randint(0,1))
n = int(input("Enter Number: "))
    
def print_matrix(n):
    for i in range(n):
        for i in range(n):
            print(random.randint(0,1), end = ' ')
        print()

print_matrix(n)
