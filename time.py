import time

start_time = time.time()
print(start_time)

a,b = 1,2
c = a+b

end_time = time.time()
print(end_time)

time_taken_in_micro = (end_time - start_time)*(10**6)

print(time_taken_in_micro)
