class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += 2 ** 32

        dic = {10:'a', 11: 'b', 12:'c', 13:'d', 14:'e', 15:"f"}
        result = ''

        while num >= 16:
            to_add = num % 16
            result = str(to_add if to_add < 10 else dic[to_add]) + result
            num //= 16

        if num >= 0:
            result = str(num if num < 10 else dic[num]) + result

        return result
        #(logn), O(1)