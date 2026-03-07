class MinHeap:
    def __init__(self):
        self.lis = []
    
    def hasContent(self):
        return self.lis

    def heapifyUp(self):
        index = len(self.lis) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.lis[index][0] < self.lis[parent][0]:
                self.lis[index], self.lis[parent] = self.lis[parent], self.lis[index]
            index = parent
        return
    
    def heapifyDown(self):
        index = 0
        while index < (len(self.lis)-1) // 2:
            leftChild, rightChild = 2*index + 1, 2*(index + 1)
            if self.lis[leftChild][0] < self.lis[rightChild][0]:
                minChild = leftChild
            else:
                minChild = rightChild
            self.lis[index], self.lis[minChild] = self.lis[minChild], self.lis[index]
            index = minChild
        return

    def addElement(self, s):
        self.lis.append(s)
        self.heapifyUp()
        return
    
    def peek(self):
        return self.lis[0]
    
    def pop(self):
        res = self.peek()
        self.lis[0], self.lis[-1] = self.lis[-1], self.lis[0]
        self.lis = self.lis[:-1]
        self.heapifyDown()
        return res[0], res[1], res[2]
    


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


    def trapRainWater(self, heightMap):

        def inBound(x, y, n, m):
            return 0 <= x < n and 0 <= y < m

        res = 0
        n, m = len(heightMap), len(heightMap[0])
        heap = MinHeap()
        visited = [[False for _ in range(m)] for _ in range(n)]

        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(len(heightMap)):
            if i == 0 or i == len(heightMap) - 1:
                for j in range(len(heightMap[0])):
                    heap.addElement((heightMap[i][j], i, j))
                    visited[i][j] = True
            else:
                heap.addElement((heightMap[i][0], i, 0))
                heap.addElement((heightMap[i][-1], i, m - 1))
                visited[i][0], visited[i][-1] = True, True
        
        while heap.hasContent():
            visiting, x, y = heap.pop()
            for i, j in direction:
                if inBound(x+i, y+j, n, m) and not visited[x+i][y+j]:
                    visited[x+i][y+j] = True
                    if visiting > heightMap[x+i][y+j]:
                        res += visiting - heightMap[x+i][y+j]
                    
                    heap.addElement((max(visiting, heightMap[x+i][y+j]), x+i, y+j))

        return res
    

sol = Solution()
#print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
#print(sol.trap([4,2,0,3,2,5]))

print(sol.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))
print(sol.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))