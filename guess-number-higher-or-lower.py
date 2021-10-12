# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

#Solution: Just use binary search to guess the correct number

class Solution:    
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            my_guess = low + (high - low)//2
            guessResult = guess(my_guess)
            if guessResult == 0:
                return my_guess
            elif guessResult == 1:
                low = my_guess + 1
            else:
                high = my_guess - 1