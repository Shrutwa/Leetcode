class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while n > 0:
            x = n % 10
            p *= x
            s +=x
            n = n//10
            
        return p - s