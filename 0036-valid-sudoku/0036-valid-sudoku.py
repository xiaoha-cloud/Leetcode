class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for row in range(9):
            check_set=set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in check_set:
                    return False
                check_set.add(board[row][i])


        # check column
        for col in range(9):
            check_set=set()
            for i in range(9):
                if board[i][col] == ".":
                    continue

                if board[i][col] in check_set:
                    return False
                check_set.add(board[i][col])


        # check 3 x 3 sub-boxes of the grid 
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) *3 + j
                    if board [row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True


        
        