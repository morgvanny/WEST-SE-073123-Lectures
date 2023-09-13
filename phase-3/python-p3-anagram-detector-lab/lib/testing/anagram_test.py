from anagram import Anagram

class TestAnagram:
    '''Class Anagram in anagram.py'''

    def test_instantiates_with_word(self):
        '''instantiates with a single argument, a word.'''
        assert(Anagram("word"))

    def test_has_match_method(self):
        '''contains a method called "match".'''
        assert(Anagram.match)

    def test_does_not_match_returns_empty_list(self):
        '''returns an empty list if the input list contains no words that match the initialized word.'''
        assert(Anagram("word").match(["hello", "goodbye"]) == [])

    def test_match_one_returns_list_length_one(self):
        '''returns a list with one element when one element of the input list matches the initialized word.'''
        assert(Anagram("enlist").match(["listen", "poison", "hello"]) == ["listen"])

    def test_match_two_returns_list_length_two(self):
        '''returns a list with two elements when two elements of the input list match the initialized word.'''
        assert(Anagram("enlist").match(["listen", "silent", "hippopotamus"]) == ["listen", "silent"])