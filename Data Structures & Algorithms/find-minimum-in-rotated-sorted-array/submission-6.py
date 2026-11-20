class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if nums[mid]>=nums[-1]:
                lo = mid+1
            else:
                if nums[mid]>nums[mid-1]:
                    hi = mid-1
                else:
                    return nums[mid]
        return nums[hi]