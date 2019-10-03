# todo: make menu into a class which can build a menu
# todo: add comments

import MovieCollection as mc
import Movie
import Menu





def create_movie(movie_collection):
    '''
    gets movie information from the user before passing it to
    the add_movie function of the MovieCollection class
    '''
    title = input('Title: ')
    if movie_collection.movie_exists(title):
        return
    genre = input('Genre: ')
    year = input('Year: ')
    duration_in_mins = input('Duration in Minutes: ')
    seen = input('Seen (y/n): optional').title()
    rating = input('Rating (optional 1.0 - 5.0): ')

    new_movie = Movie.Movie(movie_collection, title, genre, year, 
                            duration_in_mins, seen, rating)
    print('\n*************\nMovie Added:\n\n')
    print(new_movie)


def search_for_movie(movie_collection):
    '''
    searches for a movie in the database
    based on criteria given by the user.
    Certain criteria may include an operator
    (<= >=) and those are handled here and passed
    to the perform_special_search function
    '''
    criteria_dict = {1: 'title', 2: 'genre', 3: 'year',
                     4: 'duration_in_mins', 5: 'seen', 6: 'rating'}
    special_search = False

    criteria = ''
    value = ''

    while criteria not in range(1, 7):

        criteria_menu = Menu.Menu({'1': 'Title', '2': 'Genre', '3': 'Year', 
                                   '4': 'Duration', '5': 'Seen', '6': 
                                   'rating'})
        
        criteria = int(
            input('What do you want to search by: \n1. Title\n2. Genre\n'
                  '3. Year\n4. Duration\n5.Seen\n6.Rating\n'))

        if criteria == 1:
            operator = None
            value = input('Enter the exact title of the movie: ')
        elif criteria == 2:
            operator = None
            value = input('Enter the genre you want to search for: ')
        elif criteria == 3:
            value, operator, special_search = perform_special_search('year')
        elif criteria == 4:
            value, operator, special_search\
                 = perform_special_search('duration')
        elif criteria == 5:
            operator = None
            value = input('Seen (yes) or not (no): ')
        elif criteria ==  6:
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
            print('The following movies meet your criteria: ')
            for movie in found_movies:
                for key, value in movie.items():
                    print(key.title() + ': ' + value)
                print('')


def perform_special_search(type):
    '''
    Handles all searches which require an operator
    (>= <=). sets the value, operator, and special_search
    variables and returns them as a tuple
    '''

    search_type = ''
    while search_type not in range(1, 4):
        if type == 'year':
            search_type = int(input('Would you like to search for: \n'
                                    '1. Specific year\n2. Newer than\n'
                                    '3. Older than\n'))
        elif type == 'duration':
            search_type = int(input('Would you like to search for: \n'
                                    '1. Specific duration\n2. Longer than\n'
                                    '3. Shorter than\n'))
        elif type == 'rating':
            search_type = int(input('Would you like to search for: \n'
                                    '1. Specific rating\n2. Higher than\n'
                                    '3. Lower than\n'))


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
            value = input('Enter the latest year: '
                          '(returns years <= that year)')
        else:
            print('Invalid sub-criteria selected\n')
    return value, operator, special_search


def delete_movie(movie_collection):
    '''
    User interface to remove a movie from the database
    '''
    title = input('What movie do you want to delete? (Type the whole title'
                  'exactly as it is found in the database): ')
    
    movie_collection.delete_movie(title)


if __name__ == "__main__":
    
    # init new list of movies
    movie_collection = mc.MovieCollection()
    
    while True:

        main_menu = Menu.Menu({'1': 'Add movie', '2': 'Find Movie',
                               '3': 'Delete Movie', '4': 'View Collection\n\n'}, start_message='\n'
                              '******************************\n'
                              'Welcome to your movie Database\n')
        main_menu.show_menu()
        choice = int(main_menu.get_choice())

        if choice == 1:
            create_movie(movie_collection)

        elif choice == 2:
            search_for_movie(movie_collection)

        elif choice == 3:
            delete_movie(movie_collection)
        
        elif choice == 4:
            movie_collection.__str__()    
        else:
            print('Invalid input')

        continue_app = input('\n\nDo you want another operation? y/n: \n')

        if continue_app[0].lower() == 'y':
            continue_app
        else:
            break
