from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        max_rows = len(grid)
        max_cols = len(grid[0])
        num_islands = 0

        def bfs(row, col):
            queue = [(row, col)]

            while queue:
                row, col = queue.pop(0)
                if (row, col) in visited:
                    continue
                visited.add((row, col))
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

                for r, c in directions:
                    this_row = row + r
                    this_col = col + c
                    if this_row >= max_rows or this_row < 0:
                        continue
                    if this_col >= max_cols or this_col < 0:
                        continue
                    if (
                        grid[this_row][this_col] == "1"
                        and (this_row, this_col) not in visited
                    ):
                        queue.append((this_row, this_col))

        for row in range(max_rows):
            for col in range(max_cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    num_islands += 1
                visited.add((row, col))

        return num_islands
