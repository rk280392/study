from utils import my_project_database

USER_CHOICE = """
Enter:
'a' to add a new movies
'l' to list all movies
'w' to mark a movie as watched
'd' to delete a movie
'q' to quit
Your choice: """


def menu():
    my_project_database.create_movie_table()
    user_input = input(USER_CHOICE)
    if user_input == 'q':
        print("Stopping the program. Thanks for using.")
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_movies()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            prompt_find_movies()
        elif user_input == 'd'
            prompt_delete_movies()
        elif user_input == 'w':
            prompt_watched_movie()
        else:
            print("Invalid Input, please try again : ")
        user_input = input(USER_CHOICE)

def prompt_add_movies():
    name = input("Please enter movie name : ")
    genre = input("Please enter director of the movie : ")
    year = input("Please enter year of the movie : ")
    
    my_project_database.add_movie(name,genre,year)
    

def show_movies():
    for movie in my_project_database.get_all_movies() :
        watched = 'YES' if movie[4] else 'NO'  # movie[3] will be a falsy value (0) if not read
        print(f'{movie[1]} by {movie[2]} — Watched: {watched}')

def find_movies():
    find_by = input("How do you want to search for a movie? Enter name, genre or year : ").lower()
    looking_for = input("Please enter the search value : ")
    watched = 'YES' if movie[3] else 'NO'
    if find_by == 'name':
        movie_name = looking_for
    elif find_by == 'genre':
        dir_name = looking_for
    elif find_by == 'year':
        movie_year = looking_for
    my_project_database.search_movies(movie_name,dir_name,movie_year)

def prompt_watched_movie():
    name = input('Enter the name of the movie you just finished watching: ')

    my_project_database.mark_as_watched(name)


def prompt_delete_movie():
    name = input('Enter the name of the movie you wish to delete: ')

    my_project_database.delete_movie(name)

menu()
