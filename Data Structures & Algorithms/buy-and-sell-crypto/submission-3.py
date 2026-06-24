class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        minimum = arr[0]
        max_l = 0

        for i in range(len(arr)):
            if arr[i] >= 0 and arr[i] < minimum:
                minimum = arr[i]
            max_l = max(max_l,arr[i]-minimum)

        return max_l
            
        