class Solution:
    def trap(self, height) -> int:
        
        res = 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])

            if leftMax <= rightMax:
                res += leftMax - height[l]
                l += 1
            else:
                res += rightMax - height[r]
                r -= 1

        return res
    

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
#print(sol.trap([4,2,0,3,2,5]))