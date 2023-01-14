class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hold = collections.defaultdict(int)
        for char in text:
            hold[char] = hold.get(char, 0) + 1


        result = float('inf')

        for char in 'balon':
            if char == 'l' or char == 'o':
                result = min(result, hold[char]//2)
            else:
                result = min(result, hold[char])

        return result
        #O(N), O(N)