class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        
        goal = len(nums) - 1
        step = 1

        while True:

            if nums[goal-step] >= step:
                goal = goal - step
                step = 1
            else:
                step += 1 

            if not goal:
                return True
            
            if goal - step < 0:
                return False
        