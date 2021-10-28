class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        arr = []
        dict = {}
        print(nums)
        for i in range(len(nums)):
            target = nums[i]
            if target > 0:
                break
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r] + target
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    key = f"{nums[l]},{nums[r]},{target}"
                    if not(key in dict):
                        arr.append([nums[l], nums[r], target])
                        dict[key] = True
                    l += 1
                    r -= 1
        
        return arr