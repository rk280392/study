def finder(arr1,arr2):
    result = 0
    for num in arr1+arr2:
        print(arr1+arr2)
        result^=num
        print(result)
    print(result)


arr1 = [7,5, 5,7]
arr2 = [5,7,7]
finder(arr1,arr2)
