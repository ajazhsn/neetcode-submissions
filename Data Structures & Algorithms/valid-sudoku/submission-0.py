class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s1 = set()
        s2 = set()
        s3 = set()

        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        # Check columns
        for i in range(len(board[0])):
            seen = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        # Check 3x3 sub-boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])

        return True
        


