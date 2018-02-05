# validating triangles and computing perimeter

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if (a+b) > c and (a+c) > b and (b+c) > a:
    p = (a+b+c)
    print("Perimeter =",p)
else:
    print("Invalid triangle!")
