class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for m in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[m] == 0:
                        triplet = sorted([nums[i], nums[j], nums[m]])
                        res.add(tuple(triplet))   # set removes duplicates

        # convert back to list of lists
        final = [list(t) for t in res]
        return final
