class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi = 0,len(nums)-1
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if nums[mid]==target:
                return mid
            if nums[lo]<=nums[mid]:
                if target<nums[mid] and target>=nums[lo]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if target<=nums[hi] and target>nums[mid]:
                    lo = mid+1
                else:
                    hi = mid-1
        return -1
            