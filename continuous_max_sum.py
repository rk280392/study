def max_cont_sum(nums):
    max_global = num[0]
    max_current = num[0]

    for i in range(1, len(nums)):
        max_current = max(nums[i], nums[i]+max_current)
        max_global = max(max_current, max_global)

        if max_current > max_global:
            max_current = max_global

    return(max_global)

num = [1,-2,3,4,-5,8]
print(max_cont_sum(num))
