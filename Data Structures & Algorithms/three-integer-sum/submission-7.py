class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        n = len(a)
        a = sorted(a)
        result = []
        for i in range(n-2):
            if a[i]>0:break
            if i>0 and a[i]==a[i-1]:continue
            l = i+1
            r = n-1
            while l<r:
                if a[l]+a[r]==-a[i]:
                    result.append([a[i],a[l],a[r]])
                    l+=1
                    r-=1
                    while l<r and a[l]==a[l-1]:
                        l+=1
                elif a[l]+a[r]<-a[i]:
                    l+=1
                else:
                    r-=1
        return result 