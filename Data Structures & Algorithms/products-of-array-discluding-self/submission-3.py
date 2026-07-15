class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_counts = nums.count(0)
        result = []
        product = 1
        for i in range(len(nums)):
            if nums[i]!=0:
                product*=nums[i]
        if zero_counts > 1:
            result = [0]*len(nums)
        elif zero_counts == 1:
            for i in range(len(nums)):
                if nums[i]==0:
                    result.append(product)
                else:
                    result.append(0)
        else:
            for i in range(len(nums)):
                result.append(product//nums[i])
         
        return result