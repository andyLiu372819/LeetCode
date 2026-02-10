#Word Searcher 
class Solution:
    def exist(self, board, word: str) -> bool:
        start = word[0]
        rows, cols = len(board), len(board[0])

        size = rows * cols
        if size < len(word):
            return False

        def search(i, j, curr, visited):
            
            visited[i][j] = True
            if curr == len(word) - 1:
                return True
            around = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for i in range(4):
                x_i, y_i = around[i]
                if 0 <= x_i < rows and 0 <= y_i < cols and not visited[x_i][y_i]:
                    if board[x_i][y_i] == word[curr + 1]:
                        visited[x_i][y_i] = True
                        if search(x_i, y_i, curr + 1, visited):
                            return True
                        visited[x_i][y_i] = False
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == start:
                    if search(i, j, 0, [[False] * cols for _ in range(rows)]):
                        return True
        return False
                
sol = Solution()
board = [["A", "A"], ["B", "C"]]
print(sol.exist(board, "AAB"))
print("a" == "A")
                    