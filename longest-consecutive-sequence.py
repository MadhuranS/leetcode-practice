class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()
        if not nums:
            return 0
        for num in nums:
            numset.add(num)
        
        longest = 1
        
        for num in numset:
            if not(num - 1 in numset):
                current = num
                currentlongest = 1
                
                while current + 1 in numset:
                    currentlongest += 1
                    current += 1
                longest = max(longest, currentlongest)

        return longest