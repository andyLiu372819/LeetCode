class Solution:
    def divide(self, dividend: int, divisor: int) -> int:\
        # Try division by repeated subtraction
        def div_by_sub(N, D):
            if (N < 0):
                return -div_by_sub(-N, D)
            elif (D < 0):
                return -div_by_sub(N, -D)
            else:
                Q = 0
                while N >= D:
                    N -= D
                    Q += 1
                return Q
        return div_by_sub(dividend, divisor)


sol = Solution()
print(sol.divide(10, 3))  # Output: 3