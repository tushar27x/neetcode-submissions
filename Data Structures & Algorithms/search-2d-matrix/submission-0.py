class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows: int = len(matrix)
        cols: int = len(matrix[0])

        l = 0
        h = rows * cols -1

        while l <= h:
            m = l + (h-l) // 2
            row = m // cols
            col = m % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m+1
            else:
                h = m-1
        
        return False