##Solution: Use binary search, you either find the right answer or guess the answer to
##be low since no matter what the final guess will be low.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return low