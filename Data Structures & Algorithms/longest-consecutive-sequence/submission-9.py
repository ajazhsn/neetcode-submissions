class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        arr = list(set(arr))
        arr.sort()
        sum = 0
        largest = 0

        for i in range(len(arr)-1):

            if arr[i+1]==(arr[i]+1):
                sum += 1
                # <-- move the next two lines to here, one indent deeper
                if sum>largest:
                    largest = sum
            else:
                sum = 0 
        
        if len(arr)==0:
            return largest
        else:
            return largest+1