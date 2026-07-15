class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        d = dict(sorted(d.items(),key=lambda x:x[1]))

        result = []

        for item in d:
            result.append(item)

        return result[-k:]