class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        current = nums[0]
        for  i in range(1, len(nums)):
            num = nums[i]
            current = max(current + num, num)
            sum = max(current, sum)
            
        return sum