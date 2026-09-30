import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x,y in points:
            heapq.heappush(h,(x*x+y*y,x,y))
        
        result = []

        for _ in range(k):
            dist,x,y = heapq.heappop(h)
            result.append([x,y])
        
        return result


        
        