def find_num_uppercase(str):
    if len(str) == 0:
        return 0
    if str[0].istitle():
        return 1 + find_num_uppercase(str[1:])
    else:
        return find_num_uppercase(str[1:])

str = input("Enter Word: ")
print(find_num_uppercase(str))
