class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows,cols = len(grid),len(grid[0])
        queue = deque()
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        minutes = 0
        
        while queue and fresh_count > 0:
            minutes += 1
            layer_size = len(queue)

            for _ in range(layer_size):
                r,c = queue.popleft()
                for dr,dc in directions:
                    nr , nc = r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh_count-=1
                        queue.append((nr,nc))
        
        return minutes if fresh_count == 0 else -1





        


