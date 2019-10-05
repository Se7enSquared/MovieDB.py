import MovieCollection as mc


class Movie:

    def __init__(self, movie_collection, title, genre, year, duration_in_mins, seen='No',
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
        movie['duration_in_mins'] = duration_in_mins
        movie['seen'] = self.seen
        movie['rating'] = self.rating

        mc.MovieCollection.add_movie(movie_collection, movie)
        
        print('Movie added: ')
        print(movie)

    def view_movie(self):
        print(self.__str__)

    def __str__(self):
        return 'Title: ' + self.title + '\nGenre: ' + self.genre + '\nYear: ' \
                + str(self.year) + '\nDuration: ' + str(self.duration_in_mins) + \
                '\nSeen: ' + self.seen + '\nYour Rating: ' + \
                str(self.rating)
    
    def __repr__(self):
        return f'<{self.class.__name__}: {self.title}>'
