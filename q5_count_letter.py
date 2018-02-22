def count_letter(str, ch):
    if len(str) == 0:
        return 0
    elif str[0] == ch:
            return 1 + count_letter(str[1:], ch)
    else:
        return count_letter(str[1:], ch)


str = str(input("Please Enter Word: "))
ch = input("Please Enter Letter: ")
print(count_letter(str,ch))

