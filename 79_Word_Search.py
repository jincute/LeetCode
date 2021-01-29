class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)  # rows
        n = len(board[0])  # columns
        l = len(word)

        flag = [[0] * n for _ in range(m)]
        direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def dfs(i, j, k):
            if board[i][j] == word[k]:
                flag[i][j] == 1
                if k == l - 1:
                    return True
                else:
                    for d in direction:
                        ni = i + d[0]
                        nj = j + d[1]
                        if 0 <= ni < m and 0 <= nj < n and flag[ni][nj] == 0 and dfs(ni, nj, k + 1):
                            return True
                flag[i][j] = 0
                return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False