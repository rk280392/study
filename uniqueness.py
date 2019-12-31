# following function will check if all elements in a list are unique or not

def unique(l):
    unique_list = set(l)
    print(unique_list)
    if len(l) == len(unique_list):
        print("Elements are unique")
    else:
        print("List has duplicates")










unique([1,1,2,3,4])
unique([1,2,3,4])
