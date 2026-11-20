from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1,f2 = {},{}
        k = len(s1)
        if len(s1)>len(s2):
            return False

        for i in range(k):
            f2[s2[i]] = f2.get(s2[i],0)+1
            f1[s1[i]] = f1.get(s1[i],0)+1

        for r in range(k,len(s2)):
            if f1 == f2:
                return True
            f2[s2[r-k]]-=1
            if f2[s2[r-k]]==0:
                del f2[s2[r-k]]
            f2[s2[r]] = f2.get(s2[r],0)+1

        return f1 == f2
            

