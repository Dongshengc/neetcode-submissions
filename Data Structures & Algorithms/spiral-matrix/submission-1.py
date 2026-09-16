class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m, n = len(matrix), len(matrix[0])
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        results = []

        while top <= bottom and left <= right:
            
            # print(top)
            for col in range(left, right+1):
                results.append(matrix[top][col])
            # print(results)
            top += 1

            # print(right)
            for row in range(top, bottom+1):
                results.append(matrix[row][right])
            # print(results)
            right -= 1

            # print(bottom)
            if top <= bottom:
                for col in range(right, left-1, -1):
                    results.append(matrix[bottom][col])
                # print(results)
                bottom -= 1

            if left <= right:
                # print(left)
                for row in range(bottom, top-1, -1):
                    results.append(matrix[row][left])
                # print(results)
                left += 1
        
        return results
  



