class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        for i in range(len(nums1)):
            result.append(nums1[i])

        for i in range(len(nums2)):
            result.append(nums2[i])

        result.sort()

        mid = len(result)//2
        
        if len(result)%2==0:
            return (result[mid]+result[mid-1])/2
        else:
            return result[mid]