class ValidWordAbbr:

    def __init__(self, dictionary: List[str]): #O(n), O(n)
        self.contain = {}
        for item in dictionary:
            to_put = self.is_abbr(item)
            
            if to_put in self.contain:
                if self.contain[to_put] != item:
                    self.contain[to_put] = '*'
            else:
                self.contain[to_put] = item
        
        
        
    def is_abbr(self, word: str) -> str: #O(1), O(1)
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word)-2) + word[-1]
        

    def isUnique(self, word: str) -> bool: #O(n), 
        
        to_put = self.is_abbr(word)
        
        if to_put in self.contain:
            if self.contain[to_put] == word:
                return True
            else:
                return False
            
        return True
        
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)