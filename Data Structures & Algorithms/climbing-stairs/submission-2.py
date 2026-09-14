class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        def helper(n):

            if n == 0:
                return 1
            
            if n == 1:
                return 1

            if n == 2:
                return 2

            if n not in memo:
                memo[n] = helper(n - 2) + helper(n - 1)
            else:
                return memo[n]

            return memo[n]
            
        return helper(n)