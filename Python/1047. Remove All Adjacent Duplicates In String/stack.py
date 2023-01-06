class Solution:
    def removeDuplicates(self, s: str) -> str:
        contain = []
        for item in s:
            if contain and contain[-1] == item:
                contain.pop()
            else:
                contain.append(item)

        return ''.join(contain)
        #O(n), O(n)