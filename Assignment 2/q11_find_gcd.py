# Computing the greatest common divisor

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

d = min(n1,n2)

while (n1 % d == 0 and n2 % d == 0) is False:
    d -= 1
print("The greatest common divisor is: ",d)


