class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        n = len(a)
        a = sorted(a)
        result = []
        for i in range(n-2):
            l = i+1
            r = n-1
            while l<r:
                if a[l]+a[r]==-a[i]:
                    new = [a[i],a[l],a[r]]
                    if new not in result:
                        result.append(new)
                    l+=1
                    r-=1
                elif a[l]+a[r]>-a[i]:
                    r-=1
                else:
                    l+=1
        return result 