def sum_digits(n):

    if len(str(n)) == 1:
        return n

    elif len(str(n)) > 1 and n > 1:
        sum = (n % 10) + sum_digits(n // 10)
        return sum
    else:
        a = "Invalid Number!"
        return a

n = int(input("Enter number: "))
print(sum_digits(n))
    
