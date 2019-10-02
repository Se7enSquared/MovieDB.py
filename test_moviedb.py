import unittest
import unittest.mock
import moviedb as mv


class TestMoviedb(unittest.TestCase):

    movie_list = [
        {'title': 'Bambi', 'genre': 'kids', 'year': 1958, 
         'duration_in_mins': 91, 'seen': 'Yes', 'rating': 4.7},
        {'title': 'A River Runs Through It', 'genre': 'Drama', 'year': 1991, 
         'duration_in_mins': 102, 'seen': 'No', 'rating': None},
        {'title': 'It', 'genre': 'Horror', 'year': 1994, 
         'duration_in_mins': 325, 'seen': 'Yes', 'rating': 3.8},
        {'title': 'Englias', 'genre': 'Western', 'year': 1948, 
         'duration_in_mins': 82, 'seen': 'No', 'rating': None},
        {'title': 'These Hands', 'genre': 'Thriller', 'year': 2018, 
         'duration_in_mins': 75, 'seen': 'No', 'rating': None}
    ]

    def test_add(self):
        mv.add_movie().title = 'test'

if __name__ == "__main__":
    unittest.main()
