from MovieCollection import MovieCollection as mc
from Movie import Movie
from Menu import Menu
import pickle
from os import path


def create_movie(movie_collection):
    ''' gets movie information from the user before passing it to
    the add_movie function of the MovieCollection class '''

    title = input('Title:')
    if movie_collection.movie_exists(title):
        return
    genre = input('Genre:')

    # get year and validate input is a 4 digit number
    while True:
        year = input('Year:')
        if len(year) != 4:
            print('\nYear must be a 4 digit number')
        elif not year.isdigit():
            print('\nYear must be numeric')
        else:
            break
    try:
        year = int(year)
    except:
        print('\nMust be an integer')

    # get duration and verify input is numeric
    while True:
        duration_in_mins = input('Duration (mins):')
        try:
            duration_in_mins = int(duration_in_mins)
            break
        except:
            print('\nMust be an integer')

    # get seen and verify input is yes or no
    while True:
        seen = input('Seen (yes/no):').title()
        if seen in ['Yes', 'No']:
            break
        else:
            print('\nPlease type Yes or No')
    rating = ''
    while True:
        
        try:
            rating = input('Rating 1-5:')
            # rating is optional
            if rating == '':
                break
            rating = int(rating)
        except:
            print('Must be an integer')

        if rating in range(1, 6) or rating is None:
            break
        else:
            print('\nRating must be a number between 1 & 5')

    new_movie = Movie(movie_collection, title, genre, year, 
                      duration_in_mins, seen, rating)

    print('\n*************\nMovie Added:\n\n\n')
    print(new_movie)


def search_for_movie(movie_collection):
    ''' searches for a movie in the database
    based on criteria given by the user.
    Certain criteria may include an operator
    (<= >=) and those are handled here and passed
    to the perform_special_search function '''

    # finds the correct dictionary key in the movie collection based
    # on the number the user inputs
    criteria_dict = {1: 'title', 2: 'genre', 3: 'year',
                     4: 'duration_in_mins', 5: 'seen', 6: 'rating'}

    # a special_search is a search where an operator is needed (such as
    # finding all movies longer than 2 hours)
    special_search = False
    criteria = ''
    value = ''

    while criteria not in range(1, 7):

        # Construct a new menu object
        criteria_menu = Menu({'1':  'Title', '2':  'Genre', '3': 'Year', 
                              '4': 'Duration', '5': 'Seen', '6': 
                              'rating'}, start_message='What do you want '
                             'to search by: ')
        criteria_menu.show_menu()
        criteria = int(input())

        if criteria == 1:
            operator = None
            value = input('Enter the exact title of the movie:')
        elif criteria == 2:
            operator = None
            value = input('Enter the genre you want to search for:')
        elif criteria == 3:
            value, operator, special_search = perform_special_search('year')
        elif criteria == 4:
            value, operator, special_search\
                 = perform_special_search('duration')
        elif criteria == 5:
            operator = None
            value = input('Seen (yes) or not (no):')
        elif criteria == 6:
            value, operator, special_search = perform_special_search('rating')
        else:
            print('Invalid selection')

        if special_search:
            found_movies = movie_collection.find_movie(criteria_dict[criteria],
                                                       value, operator)
        else:
            found_movies = movie_collection.find_movie(criteria_dict[criteria],
                                                       value)

        if found_movies:
            print('\n\n' + str(len(found_movies)) + ' movie(s) found!\n')
            print('The following movies meet your criteria:')

            for movie in found_movies:
                for key, value in movie.items():
                    print(key.title() + ': ' + str(value))
                print('')


def perform_special_search(type):

    ''' Handles all searches which require an operator
    (>= <=). sets the value, operator, and special_search
    variables and returns them as a tuple '''

    search_type = ''
    while search_type not in range(1, 4):

        if type == 'year': 
            year_menu = Menu.Menu({'1': 'Specific year', '2': 'Newer than',
                                  '3': 'Older than'}, start_message='\nWould '
                                  'you like to search for:\n')
            year_menu.show_menu()
            search_type = int(input())

        elif type == 'duration': 
            duration_menu = Menu.Menu({'1': 'Specific duration', '2': 'Longer '
                                       'than', '3': 'Shorter than'},
                                      start_message='\nWould you like to '
                                      'search for:\n')
            duration_menu.show_menu()
            search_type = int(input())

        elif type == 'rating': 
            rating_menu = Menu.Menu({'1': 'Specific rating', '2': 'Higher '
                                     'than', '3': 'Lower than'},
                                    start_message='\nWould you like to '
                                    'search for:\n')
            rating_menu.show_menu()
            search_type = int(input())

        if search_type == 1:
            operator = None
            value = input('Enter the ' + type + 'you\'d like to search for:')

        elif search_type == 2:
            special_search = True
            operator = 'greater'
            value = input('Enter the lowest ' + type + ' (returns' + type +
                          '>= that ' + type + '):')

        elif search_type == 3:
            special_search = True
            operator = 'lesser'
            value = input('Enter the latest year:'
                          '(returns years <= that year)')

        else:
            print('Invalid sub-criteria selected\n')
    return value, operator, special_search


def delete_movie(movie_collection):

    ''' User interface to remove a movie from the database '''

    title = input('What movie do you want to delete? (Type the whole title'
                  'exactly as it is found in the database):')

    movie_collection.delete_movie(title)


if __name__ == "__main__":

    # init new list of movies
    if path.isfile('./moviecollection.txt'):
        load = input('Do you wish to load the existing collection? y/n')

        if load[0].lower() == 'y':
            movie_collection = mc.load_collection(pickle.load(
                open('moviecollection.txt', 'rb')))
        else:
            movie_collection = mc()
    else:
        movie_collection = mc()

    while True:

        main_menu = Menu({'1': 'Add movie', '2': 'Find Movie',
                          '3': 'Delete Movie', '4': 'View Collection',
                          '5': 'Save collection', '6': 'Load Collection',
                          '7': 'Quit application\n\n'}, 
                         start_message='\n' + '*' * 30 + '\n'
                         'Welcome to your movie Database\n' + '*'*30)

        main_menu.show_menu()
        choice = int(main_menu.get_choice())

        if choice == 1:
            create_movie(movie_collection)

        elif choice == 2:
            search_for_movie(movie_collection)

        elif choice == 3:
            delete_movie(movie_collection)

        elif choice == 4:
            print('\n' + '*'*20)
            print('Your Collection')
            movie_collection.__str__()    
        elif choice == 5:
            f = open('moviecollection.txt', 'wb')
            pickle.dump(movie_collection, f)
            f.close()
        elif choice == 6:
            f = open('moviecollection.txt', 'rb')
            movie_collection = mc.load_collection(pickle.load(f))
            f.close()
        elif choice == 7:
            print('\n' + '*'*20 + '\nClosing application')
            break

        else:
            print('Invalid input')

        continue_app = input('\n\nDo you want another operation? y/n:\n')

        if continue_app[0].lower() == 'y': 
            continue_app
        else:
            break
