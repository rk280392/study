import collections
def finder(arr1,arr2):
    d = collections.defaultdict(int)
    print("d1 {}".format(d))
    for num in arr2:
        print("d2-1 {}".format(d))
        d[num] += 1
        print("d2 {}".format(d))
    for num in arr1:
        print("d3-1 {}".format(num))
        if d[num] == 0:
            print("d3 {}".format(num))
            print(num)
        else:
            print("d4 {}".format(num))
            d[num] -=1
            print("d4-2 {}".format(num))
arr1 = [5,3,2,7]
arr2 = [5,2,7]
finder(arr1,arr2)
