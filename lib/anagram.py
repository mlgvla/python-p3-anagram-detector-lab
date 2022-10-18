class Anagram:

    def __init__(self, word):
        self.word = word
        self.sorted_word = "".join(sorted(word.lower()))

    def match(self, list):
        anagrams = []

        for w in list:
            sorted_w = "".join(sorted(w.lower()))
            if sorted_w == self.sorted_word:
                anagrams.append(w)
        
        return anagrams