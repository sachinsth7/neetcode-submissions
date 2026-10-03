class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = defaultdict(list)
        column_seen = defaultdict(list)
        box_seen = defaultdict(list)
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == '.':
                    continue
                box_key = (i//3, j//3)
                if value in row_seen[i] or value in column_seen[j] or value in box_seen[box_key]:
                    return False
                row_seen[i].append(value)
                column_seen[j].append(value)
                box_seen[box_key].append(value)
        return True
