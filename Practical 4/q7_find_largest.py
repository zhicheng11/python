def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    elif alist[0] < alist[1]:
        del alist[0]
        return find_largest(alist)
    elif alist[0] > alist[1]:
        del alist[1]
        return find_largest(alist)

alist = [3,4,9,7,25,4,7]
print(find_largest(alist))
