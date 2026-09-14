class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum = 0 
        max_sum = 0

        for i in range(len(nums)):

            sum += nums[i]

            if not i:
                max_sum = sum
            else:
                if max_sum < sum:
                    max_sum = sum 
            
            if sum < 0:
                sum = 0
        
        return max_sum




        