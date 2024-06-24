class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        n = len(isConnected)

        for i in range(n):
            if i in visited:
                continue
            stack = [i]
            while stack:
                cur = stack.pop()
                if cur not in visited:
                    visited.add(cur)
                    stack.extend(
                        [j for j in range(n) if isConnected[cur][j] == 1])
            count += 1

        return count
