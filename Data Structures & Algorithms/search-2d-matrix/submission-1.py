class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo,hi = 0,len(matrix)*len(matrix[0])-1

        while lo<=hi:
            mid = lo+(hi-lo)//2
            r = mid//len(matrix[0])
            c = mid%len(matrix[0])
        
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                lo = mid+1
            else:
                hi = mid-1
        
        return False