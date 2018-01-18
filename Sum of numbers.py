# input number
number = int(input("Please enter number: "))

# adding all the numbers
sumofnumber = ((number % 10) + ((number % 100) // 10) + (number // 100))

# printing the final number
if 0 < number < 1000:
    print("The sum of your number = {0}".format(sumofnumber))
else:
    print("Sorry your number is not accepted!")
