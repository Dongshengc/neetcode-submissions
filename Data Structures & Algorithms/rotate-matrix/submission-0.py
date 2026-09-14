class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):

                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # print(matrix)

        for i in range(m):
            left, right = 0, n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
        
        
        