class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        contain = set(jewels)
        
        return sum(stone in contain for stone in stones)
    
    #O(length of jewels + length of stones), O(len of jewels)