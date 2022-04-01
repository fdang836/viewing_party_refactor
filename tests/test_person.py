import pytest
from viewing_party.person import *

def test_1():
    # Arrange
    name = "Olena"
    watched = ["A", "B", "C"]
    friends = ["D", "E", "F"]
    subscriptions = ["Netflix", "Hulu"]
    new_movie = "G"

    # Act
    person = Person(name, watched, friends, subscriptions)
    watched = person.add_watched(new_movie)
    num_watched = person.get_num_watched()

    # Assert
    assert person.name == "Olena"
    assert person.watched == ["A", "B", "C", "G"]
    assert len(person.watched) ==  4