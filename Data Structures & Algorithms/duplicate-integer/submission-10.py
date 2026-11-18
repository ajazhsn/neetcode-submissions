from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(Counter(nums))!=len(nums):
            return True
        else:
            return False