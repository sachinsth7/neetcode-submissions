class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            left = 0
            right = len(m) - 1
            if target >= m[left] and target <= m[right]:
                while left <= right:
                    mid = (left+ right) // 2
                    if m[mid] == target:
                        return True
                    elif m[mid] > target:
                        right = mid - 1
                    else:
                        left = mid +1
            else:
                continue
        return False