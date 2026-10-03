class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        from collections import Counter
        k = len(p)
        if k > len(s):
            return False

        need = Counter(p)            # what a matching window must look like
        window = Counter(s[:k])      # first window, built once

        if window == need:
            return True 

        for i in range(k, len(s)):
            # entering letter
            window[s[i]] += 1

            # leaving letter
            left = s[i - k]
            window[left] -= 1
            if window[left] == 0:
                del window[left]     # keep the dict clean

            # check this window
            if window == need:
                return True

        return False