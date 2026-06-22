class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = []
        count = 0
        max_count = 0
        for i in range(len(s)):
            for j in range(len(result)):
                if s[i] == result[j]:          # fixed here
                    result = result[j+1:]
                    count = len(result)
                    break                       # also add break, else loop continues on stale j
            result.append(s[i])
            count += 1
            max_count = max(count, max_count)
        return max_count