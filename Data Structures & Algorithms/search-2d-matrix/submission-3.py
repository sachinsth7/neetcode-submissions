class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        m = len(matrix)
        n = len(matrix[0])
        right = m * n - 1
        while left <= right:
            mid = (left + right) // 2
            x = mid // n
            y = mid % n
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False