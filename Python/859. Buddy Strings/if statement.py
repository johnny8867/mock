class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        seen = set()
        if s == goal: #deal with same word
            for item in s:
                if item in seen:
                    return True
                seen.add(item)
            return False

        left = -1 
        right = -1 
        diff = 0
        for i in range(len(s)): #deal with not same word
            if s[i] != goal[i]:
                diff += 1
                if diff > 2:
                    return False

                if left == -1:
                    left = i
                
                elif left != -1 and right == -1:
                    right = i
        return s[left] == goal[right] and s[right] == goal[left]
        #O(n), O(n)