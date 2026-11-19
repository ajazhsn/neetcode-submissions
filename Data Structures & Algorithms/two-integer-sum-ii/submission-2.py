class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(numbers)):
            freq[numbers[i]] = i+1
        for i in range(len(numbers)):
            if target-numbers[i] in freq:
                return [i+1,freq[target-numbers[i]]]

        