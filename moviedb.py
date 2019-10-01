# todo: make menu into a class which can build a menu
# todo: add comments


class Movie:
    # creates a movie object which is a dictionare and appends it to a list

    movies = []

    def __init__(self, title, genre, year, duration_in_mins, seen='No',
                 rating=None):

        movie = {}
        self.title = title
        self.genre = genre
        self.year = year
        self.duration_in_mins = duration_in_mins
        self.seen = seen
        self.rating = rating

        movie['title'] = self.title
        movie['genre'] = self.genre
        movie['year'] = self.year
        movie['duration_in_mins'] = self.duration_in_mins
        movie['seen'] = self.seen
        movie['rating'] = self.rating

        Movie.movies.append(movie)

    def view_movie(self):
        print(self.__str__)

    @staticmethod
    def find_movie(criteria, value, operator=None):

        found_movies = []
        if not operator:
            for movie in Movie.movies:
                if movie[criteria] == value:
                    found_movies.append(movie)
        elif operator == 'greater':
            for movie in Movie.movies:
                if movie[criteria] >= value:
                    found_movies.append(movie)

            else:
                return found_movies
        else:
            for movie in Movie.movies:
                if movie[criteria] <= value:
                    found_movies.append(movie)

        if len(found_movies) == 0:
            print('Movie not found')
        else:
            return found_movies

    @staticmethod
    def delete_movie(title):
        for i in range(len(Movie.movies)):
            if Movie.movies[i]['title'] == title:
                del Movie.movies[i]
                print(title + ' was deleted from the database')
            else:
                print(title + ' was not found in the database. Check the title \
                      name and try again.')

    def __str__(self):
        return 'Title: ' + self.title + '\nGenre: ' + self.genre + '\nYear: ' \
                + self.year + '\nDuration: ' + str(self.duration_in_mins) + \
                '\nSeen: ' + str(self.seen) + '\nYour Rating: ' + str(self.rating)


def menu_choice():
    while True:
        try:
            choice = int(input('What do you want to do? (1, 2, 3): '))
            if choice in [1, 2, 3]:
                break
            else:
                print('You must choose 1, 2, or 3')
                continue
        except:
            print('Input must be a number between 1 & 3')
    return choice


def add_movie():
    title = input('Title: ')
    if len(Movie.movies) > 0:
        for movie in Movie.movies:
            if movie['title'] == title:
                print('That movie is already in the database!')
                return
    genre = input('Genre: ')
    year = input('Year: ')
    duration_in_mins = input('Duration in Minutes: ')
    seen = input('Seen (y/n): ').title()
    rating = input('Rating (decimal value from 1.0 - 5.0 or leave blank): ')

    new_movie = Movie(title, genre, year, duration_in_mins, seen, rating)
    print('\n*************\nMovie Added:\n\n')
    print(new_movie)


def search_for_movie():
    criteria_dict = {1: 'title', 2: 'genre', 3: 'year',
                     4: 'duration_in_mins', 5: 'seen', 6: 'rating'}
    special_search = False

    criteria = ''
    value = ''

    while criteria not in range(1, 7):

        criteria = int(
            input('What do you want to search by: \n1. Title\n2. Genre\n3. Year\n4. Duration\n5.Seen\n6.Rating\n'))

        if criteria == 1:
            operator = None
            value = input('Enter the exact title of the movie: ')
        elif criteria == 2:
            operator = None
            value = input('Enter the genre you want to search for: ')
        elif criteria == 3:
            value, operator, special_search = perform_special_search('year')
        elif criteria == 4:
            value, operator, special_search = perform_special_search('duration')
        else:
            print('Invalid selection')

        if special_search:
            found_movies = Movie.find_movie(criteria_dict[criteria], value, 
                                            operator)
        else:
            found_movies = Movie.find_movie(criteria_dict[criteria], value)

        if len(found_movies) > 0:
            print('\n\n' + str(len(found_movies)) + ' movie(s) found!\n')
            print('The following movies meet your criteria: ')
        for movie in found_movies:
            for key, value in movie.items():
                print(key.title() + ': ' + value)
            print('')


def perform_special_search(type):
    search_type = ''
    while search_type not in range(1, 4):
        if type == 'year':
            search_type = int(input('Would you like to search for: \n1. Specific year\n2. Newer than\n3. Older than\n'))
        elif type == 'duration':
            search_type = int(input('Would you like to search for: \n1. Specific duration\n2. Longer than\n3. Shorter than\n'))

        if search_type == 1:
            operator = None
            value = input('Enter the ' + type + 'you\'d like to search for:')
        elif search_type == 2:
            special_search = True
            operator = 'greater'
            value = input('Enter the lowest ' + type + ' (returns' + type + '>= that ' + type +'):')
        elif search_type == 3:
            special_search = True
            operator = 'lesser'
            value = input('Enter the latest year: (returns years <= that year)')
        else:
            print('Invalid sub-criteria selected')
    return value, operator, special_search


def delete_movie():
    title = input('What movie do you want to delete? (Type the whole title exactly as it is found in the database): ')
    Movie.delete_movie(title)


def main_menu():
    print('Welcome to your movie Database')
    print('Choose an option:')
    print('1 - Add movie')
    print('2 - View existing movie')
    print('3 - Delete a movie from the database')


if __name__ == "__main__":

    while True:
        main_menu()

        choice = menu_choice()

        if choice == 1:
            add_movie()

        elif choice == 2:
            search_for_movie()

        elif choice == 3:
            delete_movie()        
        else:
            print('Invalid choice')

        continue_app = input('\n\nDo you want another operation? y/n: ')

        if continue_app[0].lower() == 'y':
            continue_app
        else:
            break
