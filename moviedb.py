class Movie:

    movies = []

    def __init__(self, title, genre, year, duration_in_mins, seen=False, rating=None):
 
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
    def find_movie(criteria, value):

        found_movies = []

        for movie in Movie.movies:
            if movie[criteria] == value:
                found_movies.append(movie)

        if len(found_movies) == 0:
            print('Movie not found')
        else:        
            return found_movies
    
    def delete_movie(self):
        pass

    def __str__(self):
        return 'Title: ' + self.title + '\nGenre: ' + self.genre + '\nYear: ' + self.year +\
            '\nDuration: ' + str(self.duration_in_mins) + '\nSeen: ' + str(self.seen) + '\nYour Rating: ' + str(self.rating)


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
    seen = input('Seen (True or False): ').title()
    rating = input('Rating (decimal value from 1.0 - 5.0 or leave blank if haven\'t seen): ')

    new_movie = Movie(title, genre, year, duration_in_mins, seen, rating)
    print(new_movie)
    print('\n*************\nMovie Added:\n')
    print(new_movie)


def search_for_movie():
    criteria_dict = {1: 'title', 2: 'genre', 3: 'year', 4: 'duration_in_minutes', 5: 'seen', 6: 'rating'}
    criteria = int(input('What do you want to search by:\n1. Title\n2. Genre\n3. Year\n4. Duration\n5.Seen\n6.Rating'))
    if criteria == 1:
        title = input('Enter the exact title of the movie: ')
        found_movies = Movie.find_movie(criteria_dict[criteria], title)
    print('\n\n' + str(len(found_movies)) + ' movie(s) found!\n')
    if len(found_movies) > 0:
        print('The following movies meet your criteria: ')
    for movie in found_movies:
        for key, value in movie.items():
            print(key.title() + ': '+ value)


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
            
        else:
            delete_movie(title)
        
        continue_app = input('Do you want another operation? y/n')

        if continue_app[0].lower() == 'y':
            continue_app
        else:
            break