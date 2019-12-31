my_list = [1, 2, 3, 4, 5]

# Forward loop
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1


# Reverse loop
index = len(my_list) - 1
while index >= 0:
    print(my_list[index])
    index -= 1
    

# Get the last item for a list
def get_last_item(some_list):
    last_index = len(some_list) - 1
    return some_list[last_index]


print(get_last_item(my_list))
