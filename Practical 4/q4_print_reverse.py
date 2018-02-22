def reverse_int(n):
    if len(str(n)) == 1:
        print(n)
    else:
        print(n % 10, end = '')
        return reverse_int(n // 10)

n = int(input("Enter number: "))
reverse_int(n)
        
    
        
