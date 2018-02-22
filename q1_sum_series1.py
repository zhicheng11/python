def sum_series1(i):
    ala = 1 / i

    if i == 1:
        return 1
    else:
        return ala + sum_series1(i-1)
    
    
i = int(input("Please Enter Number: "))
print("{0:.2f}".format(sum_series1(i)))
