class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if nums[0] == target:
            return 0
        
        if nums[-1] == target:
            return len(nums) - 1

        left = 0
        right = len(nums) - 1

        while right - left > 1:

            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else: 
                return mid
        
        return -1 
        