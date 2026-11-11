class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = defaultdict(set)
        column_seen = defaultdict(set)
        box_seen = defaultdict(set)
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == '.':
                    continue
                box_key = (i//3, j//3)
                if value in row_seen[i] or value in column_seen[j] or value in box_seen[box_key]:
                    return False
                row_seen[i].add(value)
                column_seen[j].add(value)
                box_seen[box_key].add(value)
        return True