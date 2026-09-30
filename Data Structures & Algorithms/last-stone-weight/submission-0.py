import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)

        while len(h)>1:
            a = -heapq.heappop(h)
            b = -heapq.heappop(h)
            if a == b:
                continue
            elif a<b or b<a:
                b = abs(b-a)
                heapq.heappush(h,-b)
        
        if len(h)==0:
            return 0 
        else: 
            return -h[0]


