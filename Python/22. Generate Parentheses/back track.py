class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        contain = []

        def back_track(open, closed):
            if open == closed == n:
                result.append(''.join(contain))
                return
            
            if open < n:
                contain.append('(')
                back_track(open+1, closed)
                contain.pop()
            
            if open > closed:
                contain.append(')')
                back_track(open, closed + 1)
                contain.pop()

        back_track(0,0)
        return result

        #O(2^2N), O(2^2N)