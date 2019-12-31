my_dict: dict = {'name': 'Bob', 'age': 33, 'language': 'Python'}
my_list: list = [1, 2, 3, 4, 5]

try:
    print(my_dict['address'])
except KeyError as error:
    print('Bad key: ' + str(error))
    print(f'Bad key: {error}')
    print("Try using one of the following:")
    for key in my_dict.keys():
        print(f"\t{key}")

try:
    print(my_list[10])
except IndexError as error:
    print(error)
    print(my_list[-1])

