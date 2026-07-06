from collections import defaultdict
class Solution:
    def isValidSudoku(self,board:list[list[str]])->bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                if(board[r][c] in rows[r]
                   or board[r][c] in cols[c]
                   or board[r][c] in squares[(r // 3),(c // 3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3),(r // 3)].add(board[r][c])

        return True
    
solution= Solution()
board1=[["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
board2=[["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","1",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]              
print(solution.isValidSudoku(board1))
print(solution.isValidSudoku(board2))