class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total // 2
        if len(A) > len(B):
            A, B = B, A #always make sure A is smaller 
        left = 0
        right = len(A) - 1
        
        while True:
            mid_A = (left +right) // 2 #mid point for A
            mid_B = half - mid_A - 2 #mid point for B
            A_left = A[mid_A] if mid_A >= 0 else -float('inf')
            A_right = A[mid_A+1] if (mid_A+1) < len(A) else float('inf')
            B_left = B[mid_B] if mid_B >= 0 else -float('inf')
            B_right = B[mid_B+1] if (mid_B+1) < len(B) else float('inf')

            if A_left <= B_right and A_right >= B_left:
                if total % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                else:
                    return min(A_right, B_right)
            elif A_left > B_right:
                right = mid_A - 1
            else:
                left = mid_A + 1

        #O(log(m+n)), O(1)