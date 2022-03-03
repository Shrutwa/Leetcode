class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        s = 0
        p = 1
        while n > 0:
            x = n % 10
            digits.append(x)
            n = n//10
        # print(digits)
            
        for i in digits:
            s += i
            p *= i
            
        return p - s