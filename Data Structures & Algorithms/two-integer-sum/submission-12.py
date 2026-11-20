class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = i
        
        for i in range(len(nums)):
            if target-nums[i] in freq and freq[target-nums[i]]!=i:
                return [i,freq[target-nums[i]]]
        
        