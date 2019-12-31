number_to_count_by = 4
number_to_start_with = 11
current_number = number_to_start_with
sum_of_all_numbers = 0

while True:
    if current_number % number_to_count_by != 0:
        current_number += 1
#        print("loop1 {}".format(current_number))
        continue
    sum_of_all_numbers += current_number
    current_number += 1
    print("loop2 {}".format(current_number))
    if current_number >= 100:
        break
