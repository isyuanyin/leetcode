class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 and len(grid[0]) == 0:
            return 0

        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    if i == 0 or grid[i-1][j] == 0:
                        res += 1
                    if i == m-1 or grid[i+1][j] == 0:
                        res += 1
                    if j == 0 or grid[i][j-1] == 0:
                        res += 1
                    if j == n-1 or grid[i][j+1] == 0:
                        res += 1

        return res

