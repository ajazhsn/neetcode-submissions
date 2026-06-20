class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        freq= {}

        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1

        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        result = [num for num, count in sorted_items[:k]]
        return result