class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []

        results = []
        subset = []

        def dfs(i):
            


            if i >= len(nums):
                results.append(subset.copy())
                return

            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        
        dfs(0)

        return results
        




        