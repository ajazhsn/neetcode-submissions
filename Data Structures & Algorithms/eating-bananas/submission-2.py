class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def times(piles,rate):
            count = 0
            for i in range(len(piles)):
                count += (piles[i]+rate-1)//rate
            return count
        pos = len(piles)
        lo = 1
        hi = max(piles)
        
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if times(piles,mid)<=h:
                pos = mid
                hi = mid-1
            else:
                lo = mid+1
        
        return pos
        