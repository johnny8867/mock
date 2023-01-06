class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        left = 0 
        right = len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if target < letters[mid]:
                right = right - 1
            else:
                left = left + 1

        return letters[left]
            
    
    #O(n), O(1)