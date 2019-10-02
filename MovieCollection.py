class MovieCollection:
    movies = []
    
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def movie_exists(self, title):

        if len(self.movies) > 0:            
            for movie in movies:
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
            for movie in self.movies:
                if movie[criteria] == value:
                    found_movies.append(movie)
        elif operator == 'greater':
            for movie in self.movies:
                if movie[criteria] >= value:
                    found_movies.append(movie)

            else:
                return found_movies
        else:
            for movie in self.movies:
                if movie[criteria] <= value:
                    found_movies.append(movie)

        if not found_movies:
            print('\nMovie not found\n')
        else:
            return found_movies

    def delete_movie(self, title):
        '''
        removes a movie dictionary object from the movie collection object
        '''
        for i in range(len(self.movies)):
            if self.movies[i]['title'] == title:
                del self.movies[i]
                print(title + ' was deleted from the database\n')
            else:
                print(title + ' was not found in the database. Check the title'
                      ' name and try again.\n')

    def __str__(self):
        for movie in self.movies:
            return '\nTitle: ' + self.movies['title'] + '\nGenre: ' + \
                    self.movies['genre'] + '\nYear: ' + self.movies['year'] + \
                    '\nDuration: ' + str(self.movies['duration_in_mins']) + \
                    '\nSeen: ' + str(self.movies['seen']) + '\nYour Rating: ' \
                    + str(self.movies['rating'])
