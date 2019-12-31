def check_divisible_by_three(i,j):
    for i in range(i,j):
        if i % 3 == 0:
            print("{} is divisible by 3".format(i))
        else:
            print("{} is not divisible by 3".format(i))

check_divisible_by_three(37,399)
