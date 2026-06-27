class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF      # 32 bits of 1s
        MAX = 0x7FFFFFFF       # max positive 32-bit int
        
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
        
        # handle negative numbers (2's complement)
        return a if a <= MAX else ~(a ^ MASK)