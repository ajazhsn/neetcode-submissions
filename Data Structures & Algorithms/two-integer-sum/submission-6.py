class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        result = []
        for i in range(len(nums)):
            if target-nums[i] in d:
                result.append(d[target-nums[i]])
                result.append(i)
            else:
                d[nums[i]] = i
            
        return result