class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        contain_s = []
        contain_t = []

        for item in s:
            if contain_s and item == '#':
                contain_s.pop()
            elif item.isalpha():
                contain_s.append(item)

        for item in t:
            if contain_t and item == '#':
                contain_t.pop()
            elif item.isalpha():
                contain_t.append(item)

        return contain_s == contain_t
        #O(n), O(n)