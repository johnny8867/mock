import collections
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def helper(contains):
            res = {0:1}
            for item in contains:
                temp = collections.defaultdict(int)
                for char in item:
                    for total in res:
                        temp[total + char] += res[total]
                    
                res = temp
            return res
        
        lists = [nums1, nums2, nums3, nums4]
        
        mid = len(lists) // 2
        left, right = helper(lists[:mid//2]), helper(lists[mid//2:]) # increase run time, increase space
        
        return sum(left[s] * right[-s] for s in left)
    
    #O(n^k/2), O(n^k/2)