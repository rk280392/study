import random

num = 0

num = random.randint(1,10)
print(num)

user_input = int(input('guess a number : '))
while user_input != num:
    print('try again')
    user_input = int(input('guess a number between 1,10 : '))
if user_input == num:
    print('correct the number is {}'.format(num))
