from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find the locations of all rotten fruits
        # find the locations of all fresh fruits
        # empty spaces
        # conduct bfs from all rotten fruits by minutes

        rotten = [] # (row, col)
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        queue = deque()
        for fruit in rotten:
            queue.append(fruit)

        minute = 0
        while queue:
            next_min_queue = deque()
            while queue:
                fruit = queue.popleft()

                # check the positions NESW
                row, col = fruit
                if row - 1 >= 0:
                    if grid[row - 1][col] == 1:
                        next_min_queue.append((row - 1, col))
                        grid[row - 1][col] = 2
                        fresh -= 1
                if col + 1 < len(grid[0]):
                    if grid[row][col + 1] == 1:
                        next_min_queue.append((row, col + 1))
                        grid[row][col + 1] = 2
                        fresh -= 1
                if row + 1 < len(grid):
                    if grid[row + 1][col] == 1:
                        next_min_queue.append((row + 1, col))
                        grid[row + 1][col] = 2
                        fresh -= 1
                if col - 1 >= 0:
                    if grid[row][col - 1] == 1:
                        next_min_queue.append((row, col - 1))
                        grid[row][col - 1] = 2
                        fresh -= 1

            queue = next_min_queue

            if next_min_queue:
                minute += 1

        if fresh > 0:
            return -1
        else:
            return minute