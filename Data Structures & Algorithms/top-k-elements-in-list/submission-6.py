from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return list(sorted(freq,key=lambda x:-freq[x]))[:k]