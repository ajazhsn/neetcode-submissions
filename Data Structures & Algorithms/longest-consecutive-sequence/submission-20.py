class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        s = set(nums)
        visited = set()
        for i in range(len(nums)):
            if nums[i] not in visited and (nums[i]-1) not in s:
                a = nums[i]
                while a in s:
                    count+=1
                    visited.add(a)
                    a += 1
                max_count = max(max_count,count)
                count = 0
        return max_count 

