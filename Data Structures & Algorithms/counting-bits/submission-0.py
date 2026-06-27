class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        count = 0
        result.append(0)
        for i in range(1,n+1):
            while i!=0:
                i = i&(i-1)
                count += 1
            result.append(count)
            count = 0
        
        return result 