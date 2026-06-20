class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        freq = {}
        result = []
        for i in range(len(arr)):
            if (target-arr[i]) in freq:
                result.append(freq[target-arr[i]])
                result.append(i)
            else:
                freq[arr[i]]=i

        return result
