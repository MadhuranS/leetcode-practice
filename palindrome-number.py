class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False
        
        revX = 0
        while x > revX:
            revX = revX * 10 + x%10
            x = x//10
            
        return x == revX or x == revX//10
            