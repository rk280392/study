my_list_string = []
my_list_number = []
x = input("please enter value : ")
def type_conversion(x):
    i = 1
    while i <= 2:
        if x.isdigit() is True:
            my_list_number.append(x)
        elif x.lstrip('-').isdigit():
            my_list_number.append(x)
        else:
            my_list_string.append(x)
        i += 1
        x = input("please enter value : ")

type_conversion(x)
print(f"list of numbers {my_list_number}")
print(f"list of strings {my_list_string}")

