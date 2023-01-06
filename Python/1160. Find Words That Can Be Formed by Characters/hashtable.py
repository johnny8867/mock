class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        table = {}
        for character in chars:
            table[character] = table.get(character, 0) + 1
        for item in words:
            table2 = table.copy()
            temp = 0
            for character in item:
                if character in table2 and table2[character] > 0:
                    table2[character] -= 1
                    temp += 1
                else:
                    temp = 0 
                    break
            result += temp
        
        return result