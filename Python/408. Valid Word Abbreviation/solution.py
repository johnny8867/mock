class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        left = 0
        right = 0


        while left < len(word) and right < len(abbr):
            if abbr[right].isdigit():
                if abbr[right] == '0':
                    return False
                else:
                    temp = 0
                    while right < len(abbr) and abbr[right].isdigit():
                        temp = temp * 10 + int(abbr[right])
                        right += 1
                    left += temp
            else:
                if word[left] != abbr[right]:
                    return False
                else:
                    left += 1
                    right += 1
        return left == len(word) and right == len(abbr)
        #O(n), O(1)
