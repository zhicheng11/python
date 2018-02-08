def is_prime(n):
    prime = True
    if n > 1:
        for i in range(1,n-1):
            if n % (i+1) == 0:
                prime = False
    else:
        prime = False
    return prime
        
        
n = int(input("Please Enter Number: ")) 
print(is_prime(n))
        
