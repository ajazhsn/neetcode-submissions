class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        freq = {}
        req = []
        total_product = 1

        for num in nums:
            if num!=0:
                req.append(num)
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        
        for num in req:
            total_product*=num

        if 0 in freq:
            if freq[0]==1:
                for i in range(len(nums)):
                    if nums[i]==0:
                        nums[i]=total_product
                    else:
                        nums[i]=0
            if freq[0]>1:
                for i in range(len(nums)):
                    nums[i]=0
        else:
            for i in range(len(nums)):
                nums[i]=int(total_product/nums[i])


        return nums
        

