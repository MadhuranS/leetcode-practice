
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dict:
                return [dict[difference], i]
            else: 
                dict[nums[i]] = i

