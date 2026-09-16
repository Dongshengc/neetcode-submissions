class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}

        def helper(cost):

            if len(cost) == 1:
                return min(0, cost[0])
            elif len(cost) == 2:
                return min(cost[0],cost[1])

            hashable_key = tuple(cost)
            if hashable_key not in memo:
                memo[hashable_key] = min(helper(cost[0:-1]) + cost[-1], helper(cost[0:-2]) + cost[-2])
            else:
                return memo[hashable_key]
            
            return memo[hashable_key]


        return helper(cost)
        