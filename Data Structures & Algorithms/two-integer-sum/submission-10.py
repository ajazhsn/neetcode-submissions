class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = i
        
        for i in range(len(nums)):
            need = target - nums[i]
            if need in freq and freq[need]!=i:
                return [i,freq[need]]
        