class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def trace(curr, curr_target, curr_can):
            if curr_target == 0:
                curr.sort()
                if curr not in res:
                    res.append(curr[:])
                return
            
            if curr_target < 0:
                return
            
            for i in range(len(curr_can) - 1, -1, -1):
                curr.append(curr_can[i])
                trace(curr, curr_target - curr_can[i], curr_can[:i + 1])
                curr.pop()
            
        
        candidates.sort()
        for i in range(len(candidates) - 1, -1, -1):
            print(candidates[:i + 1])
            trace([candidates[i]], target - candidates[i], candidates[:i + 1])
        return res
    

sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
print(sol.combinationSum([2, 3, 5], 8))