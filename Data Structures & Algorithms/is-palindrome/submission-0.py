class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for ch in s:
            if ch.isalnum():
                result += ch.lower()

        n = len(result)
        i = 0
        j = n-1
        for i in range(0,n//2):
            if result[i]==result[j]:
                i+=1
                j-=1
                continue
            else:
                return False
                break
        else:
            return True