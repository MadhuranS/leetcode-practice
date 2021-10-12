# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

#Use binary search, every loop narrow the domain by removing elements that
#can definitely not be the answer

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        high = n 
        low = 1
        while low < high:
            mid = low + (high-low)//2
            version_check = isBadVersion(mid)
            if version_check:
                high = mid
            else:
                low = mid + 1

        return high