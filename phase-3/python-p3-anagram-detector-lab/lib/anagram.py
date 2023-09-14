# your code goes here!
class Anagram:
    def __init__(self, original_word):
        self.original_word_sorted = sorted(original_word.lower())

    def match(self, words):
        # anagrams = []
        # for potential_anagram in words:
        #     if (self.is_anagram(potential_anagram)):
        #         anagrams.append(potential_anagram)
        # return anagrams
        return [word for word in words if self.is_anagram(word.lower())]

    def is_anagram(self, word):
        return sorted(word) == self.original_word_sorted
