class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        result = 1
        count = 1
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return count
        for i in range(len(nums)-1):
            if (nums[i]+1)==nums[i+1]:
                count+=1
                result = max(result,count)
            else:
                count = 1
        return result
