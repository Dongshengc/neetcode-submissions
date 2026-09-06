class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        # first layer
        left = 0
        right = m - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                # row = mid 
                break

        if matrix[mid][0] > target:
            row = mid - 1
        else: 
            row = mid 
        # print(row)

        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                return True
        
        return False


        