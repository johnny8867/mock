class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        left = -1 
        right = -1 

        if len(s) != len(goal):
            return False
        count = 0 
        contain = set()
        if s == goal:
            for char in s:
                if char in contain:
                    return True
                contain.add(char)
                
        count = 0 
        index = 0
        while index < len(s):
            if s[index] != goal[index]:
                count += 1
                if count == 3:
                    return False
                if left == -1:
                    left = index
                elif right == -1:
                    right = index
            index += 1
        return (s[left] == goal[right] and s[right] == goal[left]) and (left != right)
        #O(N), O(N)