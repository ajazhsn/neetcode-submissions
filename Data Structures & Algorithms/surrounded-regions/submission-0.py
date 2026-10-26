class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return 
        
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r,c):
            if (
                (r,c) in visited
                or r<0 or r>=rows or c<0 or c>=cols or board[r][c]=='X'
            ):
                return

            visited.add((r,c))

            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            for dr,dc in directions:
                dfs(r+dr,c+dc)

        for r in range(rows):
            dfs(r,0)
        
        for c in range(cols):
            dfs(0,c)

        for r in range(rows):
            dfs(r,cols-1)

        for c in range(cols):
            dfs(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and board[r][c]=='O':
                    board[r][c]='X'

        
        




        
            