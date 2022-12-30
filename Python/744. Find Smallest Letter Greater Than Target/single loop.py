class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for item in letters:
            if item > target:
                return item
            
        return letters[0]
    
    #O(n), O(1)