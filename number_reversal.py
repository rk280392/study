reverse = 0
remainder = 0
n = 1234

while n>0:
    remainder= n % 10
    n = n//10
    reverse = reverse*10+remainder
print(reverse)

