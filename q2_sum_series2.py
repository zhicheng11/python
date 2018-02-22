def sum_series2(i):
    ala = i / (2*i + 1)

    if i == 1:
        return 1 / 3
    else:
        return ala + sum_series2(i-1)
    
    
i = int(input("Please Enter Number: "))
print("{0:.2f}".format(sum_series2(i)))
