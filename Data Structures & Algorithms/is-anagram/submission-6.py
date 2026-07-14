class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        if len(s)!=len(t):
            return False
        for ch in s:
            if ch not in d1:
                d1[ch]=1
            else:
                d1[ch]+=1
        
        for ch in t:
            if ch not in d2:
                d2[ch] = 1
            else:
                d2[ch] += 1

        for ch in d1:
            if ch not in d2:
                return False
            else:
                if d1[ch]!=d2[ch]:
                    return False
        else:
            return True