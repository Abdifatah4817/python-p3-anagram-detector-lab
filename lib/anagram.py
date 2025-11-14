class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        sorted_word = sorted(self.word)
        matches = []

        for w in word_list:
            lw = w.lower()
            if lw != self.word and sorted(lw) == sorted_word:
                matches.append(w)

        return matches
