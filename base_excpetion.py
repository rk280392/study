my_dict: dict = {'name': 'Bob', 'age': 33, 'language': 'Python'}
my_list: list = [1, 2, 3, 4, 5]

try:
    print(my_dict['name'])
    print(my_list[10])

except KeyError as error:
    print(f'Bad key: {error}')

except IndexError:
    print(my_list[-1])

except BaseException as error:
    print(f"something went wrong: {error}")
