class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                box_key = (i //3 , j //3)
                if val in rows[i] or val in cols[j] or val in box[box_key]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                box[box_key].add(val)
        return True
            
