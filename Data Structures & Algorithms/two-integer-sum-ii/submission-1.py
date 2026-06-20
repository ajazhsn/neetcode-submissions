class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # result = []
        # i = 0
        # k = len(numbers)-1
        # j = k

        # while i != k:
        #     while i != j:
        #         if numbers[i]!=numbers[j]:
        #             if numbers[i]+numbers[j]==target:
        #                 result.append(numbers[i])
        #                 result.append(numbers[j])
        #             j-=1
        #     i += 1
        #     j = k
        result = []
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[j]==target-numbers[i]:
                    result.append(i+1)
                    result.append(j+1)
        return result