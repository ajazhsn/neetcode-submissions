from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for r in range(len(s2)-len(s1)+1):
            if Counter(s2[r:r+len(s1)]) == Counter(s1):
                return True
        return False
            

