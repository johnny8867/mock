import collections
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        queue = collections.deque()

        for i in range(len(dom)):
            if dominoes[i] != '.':
                queue.append((i, dominoes[i]))

        while queue:
            index, val = queue.popleft()

            if val == 'L':
                if index > 0 and dom[index-1] == '.':
                    dom[index-1] = 'L'
                    queue.append((index-1, 'L'))

            elif val == 'R':
                if index + 1 < len(dom) and dom[index+1] == '.':
                    if index + 2 < len(dom) and dom[index+2] == 'L':
                        queue.popleft()
                    else:
                        dom[index+1] = 'R'
                        queue.append((index+1, 'R'))

        return ''.join(dom)
        #O(N), O(N)