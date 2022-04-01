from lib2to3.pgen2.pgen import generate_grammar
import pytest
from viewing_party.movie import *

def test_1():
    # Arrange
    title = "Travelers"
    genre = "Drama"
    rating = 9
    host = "Netflix"
    new_rating = 8

    # Act
    movie = Movie(title, genre, rating, host)
    movie.update_rating(new_rating)

    # Assert
    assert movie.title == "Travelers"
    assert new_rating == movie.rating


    