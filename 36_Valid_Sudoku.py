class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. 每行包含1-9不重复的数字
        # 2. 每列包含1-9不重复数字
        # 3. 3 x 3 九宫格包含1-9不重复数字 [0-2][3-5][6-8]

        '''
        solution 1

        used_i = [[0]*9 for _ in range(9)] # python _ 表示？
        used_j = [[0]*9 for _ in range(9)]
        used_k = [[0]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                piece = board[i][j]
                if piece == '.':
                    continue
                n = int(piece) - 1
                k = i // 3 * 3 + j // 3
                if used_i[i][n] or used_j[j][n] or used_k[k][n]:
                    return False
                used_i[i][n] = used_j[j][n] = used_k[k][n] = 1
        return True
        '''

        # solution 2 字典映射
        # 时间复杂度 O(1), 空间复杂度 O(1), 复杂度固定在 9*9 宫格内
        # 核心思想采用字典映射，存储每行，每列，每个9宫格元素出现的个数，总共有9行9列9块9宫格
        # 最后采用 set，集合，检索遍历的次数，一旦出现不等于1的值，return False, 其他情况 return True
        boxs = [{} for _ in range(9)]  # _ 表示无关紧要的变量，比如一些临时值
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxs_number = 0
        for i in range(9):
            if i % 3 == 0 and i != 0:
                boxs_number += 3
            # print(box_number)
            for j in range(9):
                if board[i][j] != '.':
                    # Python 字典 setdefault() 方法和 get()方法 类似
                    # 如果键不已经存在于字典中，将会添加键并将值设为默认值。
                    rows[i][board[i][j]] = rows[i].setdefault(board[i][j], 0) + 1
                    columns[j][board[i][j]] = columns[j].setdefault(board[i][j], 0) + 1
                    boxs[boxs_number + j // 3][board[i][j]] = boxs[boxs_number + j // 3].setdefault(board[i][j], 0) + 1
                    #         print(rows)
                    #         print(columns)
                    #         print(boxs)

                    #         print(set(list(boxs[0].values())))

        for i in range(9):
            b = set(list(boxs[i].values()))
            r = set(list(rows[i].values()))
            c = set(list(columns[i].values()))

            for i in b:
                if i != 1:
                    return False
            for i in r:
                if i != 1:
                    return False
            for i in c:
                if i != 1:
                    return False
        return True