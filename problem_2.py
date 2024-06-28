class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i]!='.':
                    if board[j][i] in s:
                        return False
                    else:
                        s.add(board[j][i])

        lines = [[] * 9 for _ in range(9)]
        for i in range(9):
            layer = board[i]
            for j in range(3):
                sub_layer = layer[3 * j: 3 * (j + 1)]
                lines[3 * (i // 3) + j].extend(sub_layer)
        for i in range(9):
            nums_line = set()
            for j in range(9):
                if lines[i][j] != '.':
                    if lines[i][j] in nums_line:
                        return False
                    else:
                        nums_line.add(lines[i][j])
                else:
                    continue
        return True

        



        