class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_l = 0
        max_freq = 0
        freq = {}
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1
            max_freq = max(max_freq,freq[s[right]])
            # window_size = right-left+1
            while (right-left+1)-max_freq>k:
                freq[s[left]]-=1
                left+=1
            max_l = max(max_l,right-left+1)
        return max_l
            