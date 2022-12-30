class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = { 
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz' 
        }

        if not digits:
            return []
        
        result = []
        contain = []

        def back_track(index, contain):
            if len(contain) == len(digits):
                result.append(''.join(contain))
                return

            cur = table[digits[index]]

            for letter in cur:
                contain.append(letter)
                back_track(index+1, contain)
                contain.pop()

        back_track(0, contain)
        return result
        #O(N*4^N) N - len(digits), O(N) for space