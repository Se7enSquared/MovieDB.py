class MovieCollection:
    movies = []

    def __init__(self):
        self.movies = []

    @classmethod
    def load_collection(cls, collection):
        cls.movies = collection
        return collection

    @classmethod
    def save_collection(cls, collection):
        with open('moviecollection.txt', 'wb') as f:
            pickle.dump(collection, f)
            print('*'*20 + '\nCollection saved.')

    def add_movie(self, movie):
        self.movies.append(movie)

    def movie_exists(self, title):

        if len(self.movies) > 0:            
            for movie in self.movies:
                if movie['title'] == title:
                    print('That movie is already in the database!\n')
                    return True
        return False

    def find_movie(self, criteria, value, operator=None):
        '''
        Handles searches through the movie list
        appends movies that are found to a list
        if movie is not found, displays message
        if found, returns list of found movies
        '''

        found_movies = []

        if not operator:
            found_movies.extend(movie for movie in self.movies if movie[criteria] == value)
        elif operator == 'greater':
            found_movies.extend(movie for movie in self.movies if movie[criteria] >= value)
            return found_movies
        else:
            found_movies.extend(movie for movie in self.movies if movie[criteria] <= value)
        if not found_movies:
            print('\nMovie not found\n')
        else:
            return found_movies

    def delete_movie(self, title):
        ''' removes a movie dictionary object from the movie 
        collection object '''
        for i in range(len(self.movies)):
            if self.movies[i]['title'] == title:
                del self.movies[i]
                print(title + ' was deleted from the database\n')
                break
            else:
                print(title + ' was not found in the database. Check the title'
                      ' name and try again.\n')

    def __str__(self):
        for movie in self.movies:
            if self.movies is None:
                print('The collection is empty')
            else:
                print('\nTitle: ' + movie['title'] + '\nGenre: ' +
                      movie['genre'] + '\nYear: ' + str(movie['year']) +
                      '\nDuration: ' + str(movie['duration_in_mins']) +
                      '\nSeen: ' + str(movie['seen']) + '\nYour Rating: '
                      + str(movie['rating']))

    def __repr__(self):
        return f'<{self.__class__.__name__} with {len(self.movies)} items>'
