class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for ch in s:
            if ch in dict:
                dict[ch]+=1
            else:
                dict[ch]=1
            
        for ch in t:
            if ch in dict:
                dict[ch]-=1
            else:
                return False
            
        for ch in dict:
            if dict[ch]==0:
                continue
            else:
                return False
        else:
            return True