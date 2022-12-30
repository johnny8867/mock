import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check(p, q):
            if (not p and not q):
                return True
            if (not p or not q) or q.val != p.val:
                return False
            return True

        queue = collections.deque([(p,q)])

        while queue:
            first, second = queue.popleft()
            
            if not check(first,second):
                return False

            if first:
                queue.append((first.left, second.left))
                queue.append((first.right, second.right))

        return True

    #O(N), O(N)