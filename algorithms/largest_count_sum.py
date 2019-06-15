def large_count_sum(arr):
    if len(arr) == 0:
        print("Array needs data")

    max_sum = curr_sum = arr[0]

    for num in arr[1:]:
        curr_sum = max(curr_sum+num, num)
        max_sum = max(curr_sum, max_sum)

    print(max_sum)

arr = [1,2,-1,3,4,10,10,-10,-1]

large_count_sum(arr)
