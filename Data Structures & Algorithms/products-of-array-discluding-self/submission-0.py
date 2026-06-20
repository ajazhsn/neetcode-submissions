class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1 
        dict = {}
        for num in nums:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1

        for num in nums:
            if num == 0:
                continue
            else:
                product = product*num

        if 0 in dict:
            if dict[0]>1:
                for i in range(len(nums)):
                    nums[i]=0
            if dict[0]==1:
                for i in range(len(nums)):
                    if nums[i] == 0:
                        nums[i] = product
                    else:
                        nums[i] = 0

        else:
            for i in range(len(nums)):
                nums[i] = product//nums[i]
        
        return nums      