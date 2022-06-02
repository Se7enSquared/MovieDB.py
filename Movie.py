from MovieCollection import MovieCollection as mc


class Movie:

    def __init__(self, movie_collection, title, genre, year, duration_in_mins, seen='No',
                 rating=None):

        self.title = title
        self.genre = genre
        self.year = year
        self.duration_in_mins = duration_in_mins
        self.seen = seen
        self.rating = rating

        movie = {
            'title': self.title,
            'genre': self.genre,
            'year': self.year,
            'duration_in_mins': duration_in_mins,
            'seen': self.seen,
            'rating': self.rating,
        }

        mc.add_movie(movie_collection, movie)

        print('Movie added: ')
        print(movie)

    def view_movie(self):
        print(self.__str__)

    def __str__(self):
        return (
            (
                (
                    (
                        (
                            f'Title: {self.title}'
                            + '\nGenre: '
                            + self.genre
                            + '\nYear: '
                            + str(self.year)
                        )
                        + '\nDuration: '
                    )
                    + str(self.duration_in_mins)
                    + '\nSeen: '
                )
                + self.seen
            )
            + '\nYour Rating: '
        ) + str(self.rating)
                
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.title}>'
