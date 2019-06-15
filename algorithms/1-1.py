import time
start_time = time.time()

def sum2(n):

    final_sum = (n*(n+1))/2
    print(final_sum)

sum2(1000)
print("My program took", time.time() - start_time, "to run")
