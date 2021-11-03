class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        self.reverse(0, len(nums) - 1, nums)
        self.reverse(0, k - 1, nums)
        self.reverse(k, len(nums) - 1, nums)
                
    def reverse(self, start: int, end: int, nums: List[int]) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1