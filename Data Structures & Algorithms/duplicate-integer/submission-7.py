class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for x in nums:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1
        
        for x in dict:
            if dict[x]!=1:
                return True
        else:
            return False
             