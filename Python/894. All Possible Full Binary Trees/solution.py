# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0:[], 1:[TreeNode(0)]}

        def backtrack(n):
            if n in dp:
                return dp[n]
            res = []
            for l in range(n):
                r = n - 1 - l
                left = backtrack(l)
                right = backtrack(r)
                
                for l_t in left:
                    for r_t in right:
                        res.append(TreeNode(0, l_t, r_t))
            dp[n] = res
            return res
        backtrack(n)
        return dp[n]