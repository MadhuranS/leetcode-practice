class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            return self.intersect(nums2, nums1)
        dict = {}
        for num in nums1:
            dict[num] = dict.get(num, 0) + 1
        
        count = 0
        for num in nums2:
            if num in dict and dict[num] > 0:
                dict[num] = dict.get(num) - 1
                nums1[count] = num
                count += 1
                
        return nums1[0:count]