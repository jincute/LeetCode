class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        # solutioni 1, passed. but not in-place

        row_matrix = len(matrix)
        new_matrix = [[0 for i in range(len(matrix[0]))] for _ in range(row_matrix)]

        for i in range(row_matrix):
            for j in range(len(matrix[i])):
                # print(row_matrix-1-j)
                # print(i)
                new_matrix[i][j] = matrix[row_matrix-1-j][i]

        for i in range(row_matrix):
            for j in range(len(matrix[i])):
                matrix[i][j] = new_matrix[i][j]
        return matrix
        '''

        # 一行代码
        # matrix[:]=map(list,zip(*matrix[::-1]))

        '''
        # solution 2, 两次。先进行转置，再进行每行的反转
        '''
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
        return matrix

