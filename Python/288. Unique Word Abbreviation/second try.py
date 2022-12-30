class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.contain = {}
        for word in dictionary:
            self.addword(word)
        #O(n)
    def isUnique(self, word: str) -> bool:
        key = ''
        if len(word) <= 2:
            key = word
        else:
            key = word[0] + str(len(word)-2) + word[-1]

        if key not in self.contain:
            return True
        else:
            if word in self.contain[key]:
                for value in self.contain[key]:
                    if word != value:
                        return False
                return True
        return False
        #O(1)?

    def addword(self, word):
        key = ''
        if len(word) <= 2:
            key = word
        else:
            key = word[0] + str(len(word)-2) + word[-1]
        self.contain[key] = self.contain.get(key, []) + [word]
        #O(1)? 
    


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)