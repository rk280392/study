my_list = [1,2,3,4,5]

start_index = 0
end_index = len(my_list) -1

while end_index > start_index:
    my_list[start_index], my_list[end_index] = my_list[end_index], my_list[start_index]
    start_index += 1
    end_index -= 1
print(my_list)

