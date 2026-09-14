class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def helper(m, n):

            if m == 1:
                return 1
            
            if n == 1:
                return 1

            if (m, n) not in memo:
                memo[(m, n)] = helper(m-1, n) + helper(m, n-1)
            else:
                return memo[(m, n)]
            
            return memo[(m, n)]
        

        return helper(m, n)
        