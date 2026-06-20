class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        result = []
        
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        

        items = list(d.items())

        n = len(items)

        n = len(items)

        for i in range(n):
            for j in range(0, n - i - 1):
                if items[j][1] < items[j + 1][1]:
                    items[j], items[j + 1] = items[j + 1], items[j]

        for i in range(k):
            result.append(items[i][0])

        return result

    
        