class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
        print(s)
        start = end = 0
        while end < len(s):
            if s[end] == " ":
                self.reverse(s, start, end - 1)
                end += 2
                start = end - 1
            else:
                end += 1
        self.reverse(s, start, end - 1)
                
    
    def reverse(self, s: List[str], l: int, r: int):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1