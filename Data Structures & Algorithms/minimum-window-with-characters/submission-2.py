from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = Counter()
        required = len(need)       # distinct letters to satisfy
        formed = 0
        left = 0
        best_len = float('inf')
        best_start = 0

        for right in range(len(s)):
            c = s[right]
            window[c] += 1
            if c in need and window[c] == need[c]:
                formed += 1                      # c just became satisfied

            while formed == required:            # valid → record, shrink
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                d = s[left]
                if d in need and window[d] == need[d]:
                    formed -= 1                  # d is about to drop below need
                window[d] -= 1
                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]