class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        unique = {}
        l = 0
        length = 0
        n = len(s)
        for right in range(n):
            if s[right] not in unique or unique[s[right]]<left:
                unique[s[right]] = right
                
            else:
                left = unique[s[right]] + 1
                unique[s[right]] = right
                
            l = right-left+1
            length = max(length,l)
        
        return length
            