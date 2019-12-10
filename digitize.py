# following code will convert an integer into a list of digits.

num = 123456

list_of_digits = list(map(int, str(num)))

print(list_of_digits)

list_of_digits = [int(x) for x in str(num)]

print(list_of_digits)
