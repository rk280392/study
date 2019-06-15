def pair_sum(arr,k):

    if len(arr) < 2:
        print("Please enter more values")

    seen = set()
    output = set()

    for i in arr:
        target = k-i
        print("target : {}".format(target))

        if target not in seen:
            seen.add(i)
            print("seen : {}".format(seen))

        else:
            print(min(i,target))
            print(max(i,target))
            output.add((min(i,target), (max(i,target))))
            print("output : {}".format(output))

    print("pairs :{}".format(len(output)))
    print('\n'.join(map(str, list(output))))

pair_sum([1,2,2,4,3], 4)
