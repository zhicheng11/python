def gcd(m,n):
    if m % n == 0:
        print("GCD = {0}".format(n))
    else:
         return gcd(n,m % n)
    

m = int(input("Enter First Number: "))
n = int(input("Enter second Number: "))
gcd(m,n)


    
    
