class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hour(piles,k):
            return sum(((pile + k - 1) // k) for pile in piles)
        ans = 0
        lo,hi = 1,max(piles)
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if hour(piles,mid)<=h:
                ans = mid 
                hi = mid-1
            else:
                lo = mid+1
        return ans 