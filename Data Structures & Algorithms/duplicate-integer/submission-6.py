class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        #flag = 1
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                #flag = 0
                return True 
                break 
        #if flag == 1:
        return False

            