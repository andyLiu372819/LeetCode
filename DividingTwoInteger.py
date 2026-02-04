class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        Q = 0

        negative = (dividend < 0 or divisor < 0) and not (dividend < 0 and divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
            i = 0
            while dividend >= (divisor << (i + 1)):
                i += 1

            dividend = dividend - (divisor << i)
            Q += (1 << i)
            

        return Q if not negative else -Q


sol = Solution()
print(sol.divide(-1, -1))  # Output: 3

