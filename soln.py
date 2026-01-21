def threeSumClosest(nums: list[int], target: int) -> list[list[int]]:
    def fun(s, nums1, t, size):
        res1 = []
        for i in range(s + 1, size):
            if nums[i] == nums[i-1]:
                continue
            j, k = i + 1, size - 1
            while j < k:
                temp = nums1[i] + nums1[j] + nums1[k]

                if temp == t:
                    res1.append([nums1[i], nums1[j], nums1[k]])
                    j += 1
                    while nums1[j] == nums1[j - 1] and j < k:
                        j += 1
                elif temp < t:
                    j += 1
                else:
                    k -= 1
        return res1

    n = len(nums)
    if n < 4:
        return []
    res = []
    nums.sort()

    for i1 in range(0, n):
        if i1 > 0 and nums[i1] == nums[i1 - 1]:
            continue
        temp_res = fun(i1, nums, target - nums[i1], n)
        for j1 in temp_res:
            if nums[i1] + sum(j1) == target:
                res.append([nums[i1]] + j1)
    return res


#nums1 = [1, 0, -1, 0, -2, 2]
nums2 = [2, 2, 2, 2, 2]
#print(threeSumClosest(nums1, 0))
print(threeSumClosest(nums2, 8))