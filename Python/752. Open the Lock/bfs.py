import collections
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0

        visited = set(deadends)

        queue = collections.deque()
        queue.append(('0000', 0))

        visited.add('0000')

        def next_comb(comb):
            result = []
            for i in range(4):
                val = str((int(comb[i])+1) % 10)
                result.append(comb[:i] + val + comb[i+1:])
                val = str((int(comb[i])-1) % 10)
                result.append(comb[:i] + val + comb[i+1:])
            return result

        while queue:
            cur_comb, steps = queue.popleft()
            if cur_comb == target:
                return steps
            for item in next_comb(cur_comb):
                if item not in visited:
                    visited.add(item)
                    queue.append((item, steps+1))
        return -1
        #O(N^2 * A^N +D) A = 0 - 9, N = number of dials, 10. D -> create set
        #O(A^N + D)