from typing import List, Tuple

from utils.database_connection import DatabaseConnection

movies = Tuple[int, str, str, int]


def create_movie_table() -> None:
    with DatabaseConnection('my_project1.db') as connection:
        cursor = connection.cursor()

        # SQLite automatically makes `integer primary key` row auto-incrementing (see link in further reading)
        cursor.execute('CREATE TABLE IF NOT exists movies (id integer primary key, name text, genre  text, year integer, watched integer default 0)')


def get_all_movies() -> List[movies]:
    with DatabaseConnection('my_project1.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM movies')
        books = cursor.fetchall()
    return books


def add_movie(name: str, genre: str, year : int) -> None:
    with DatabaseConnection('my_project1.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO movies (name, genre, year) VALUES (?, ?, ?)', (name, genre, year))


def mark_movies_as_watched(name: str, year: int, genre: str) -> None:
    with DatabaseConnection('my_project1.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE movies SET watched=1 WHERE name=? and genre=? and year=?', (name,genre,year))


def delete_movies(name: str, genre: str, year: int) -> None:
    with DatabaseConnection('my_project1.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM movies WHERE name=? and year=?', (name,year))
def search_movies(name: str, genre: str, year: int) -> None:
    with DatabaseConnection('my_project1.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * from movies where name=? or genre=? or year=?', (name,genre,year))
