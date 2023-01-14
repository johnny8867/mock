class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        convert = []

        for val in nums:
            convert.append(str(val))

        def compare(n1, n2):
            if n1+n2 > n2+n1:
                return -1
            else:
                return 1
        convert = sorted(convert, key=cmp_to_key(compare))

        return str(int("".join(convert)))
        #O(nlogn), O(n)