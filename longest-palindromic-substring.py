class Solution:

    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 1
        for i in range(len(s)):
            index1 = self.findPalindrome(s, i, i)
            index2 = self.findPalindrome(s, i, i+1)
            if index1[1] - index1[0] > index2[1] - index2[0]:
                length = index1[1] - index1[0]
                index = index1
            else :
                length = index2[1] - index2[0]
                index = index2
            
            if length > end - start:
                print("new start", length)
                start = index[0]
                end = index[1]
                print("start new", start)
                print("end new", end)
            
        return s[start:end]
        
    def findPalindrome(self, s: str, start: int, end: int) -> List:
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return [start + 1, end]