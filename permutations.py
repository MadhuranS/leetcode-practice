class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first: int):
            if first == len(nums) - 1:
                output.append(nums[:])
            else:
                for i in range(first, len(nums)):
                    nums[first], nums[i] = nums[i], nums[first]
                    backtrack(first + 1)
                    nums[first], nums[i] = nums[i], nums[first]
            
        output = []
        backtrack(0)
        return output