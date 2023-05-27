# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        matched_words = []
        sorted_word = sorted(self.word.lower())
        for word in words:
            if sorted(word.lower()) == sorted_word and word.lower() != self.word.lower():
                matched_words.append(word)
        return matched_words
