import time

start_time = time.time()
def sum(n):
    final_sum = 0
    for x in range(n+1):
        print(x)
        final_sum += x
    print(final_sum)
sum(1000)
print("My program took", time.time() - start_time, "to run")
