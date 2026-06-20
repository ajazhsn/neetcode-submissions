class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = []
        for item in nums:
            if item not in new:
                new.append(item)
            else:
                return True
                break
        return False 
            