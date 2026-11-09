class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0;
        r = len(matrix) * len(matrix[0])
        
        while l < r:
            m = l + (r - l) // 2

            i = int(m / len(matrix[0]))
            j = m % len(matrix[0])
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = m + 1
            elif matrix[i][j] > target:
                r = m
        
        return False