#n = int(input("Please enter number of elements : "))
a = list(map(int,input("\nEnter the numbers : ").strip().split()))
#print(len(a))
#print("\nList is - ", a)
second_input = input("please enter value to compare: " )

def pair_sum(arr,k):
    count = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) == int(k):
                count +=1
    return count

print("Count of pairs is", pair_sum(a, second_input))
