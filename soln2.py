def trap(height: list[int]) -> int:
    def find_next_larger(height, n, j):
        i = j + 1
        while i < n:
            if height[j] <= height[i]:
                return i
            i += 1
        return None

    def find_next_largest(height, n, i):
        j = i + 1


    def highest_pillar(height, n, i):
        k = i + 1
        res = 0
        while k < n:
            t = find_next_larger(height, n, k)
            if t:
                for p in range(k, t):
                    res += height[t] - height[p]
                k = t
            else:
                k += 1
        return res

    res = 0
    i, n = 0, len(height)
    while height[i] == 0:
        i += 1
    while i < n:
        j = find_next_larger(height, n, i)
        if j:
            for k in range(i, j):
                res += height[i] - height[k]
            i = j
        else:
            res += highest_pillar(height, n, i)
            i = n
    return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [0,7,1,4,6]
print(trap(height2))