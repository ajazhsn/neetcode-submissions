class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows,cols = len(heights),len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r,c,visited,prev_height):
            if (
                (r,c) in visited
                or r<0 or r>=rows or c<0 or c>=cols
                or heights[r][c] < prev_height
            ):
                return

            visited.add((r,c))

            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            for dr,dc in directions:
                dfs(r+dr,c+dc,visited,heights[r][c])

        for c in range(cols):
            dfs(0,c,pacific_reachable,heights[0][c])
        
        for r in range(rows):
            dfs(r,0,pacific_reachable,heights[r][0])

        for c in range(cols):
            dfs(rows-1,c,atlantic_reachable,heights[rows-1][c])
        
        for r in range(rows):
            dfs(r,cols-1,atlantic_reachable,heights[r][cols-1])

        return list(pacific_reachable & atlantic_reachable)






