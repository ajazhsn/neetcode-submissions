class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        s = set(nums)
        for x in s:
            if x-1 not in s:
                length = 1
                while x+length in s:
                    length += 1
                best = max(length,best)

        return best