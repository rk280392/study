my_string = 'radar'

original_str = my_string
reverse_str = my_string[::-1]

if original_str == reverse_str:
    print("palindrome")


def is_palidrome(str):
    return str==''.join(str[::-1])
print(is_palidrome('radar'))
