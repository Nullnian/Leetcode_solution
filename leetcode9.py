# Question 9:
    # Palindrome Number
    # Given an integer x, return true if x is a palindrome, and false otherwise.

# The leetcode solution
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        xPali = x[::-1]
        return True if x==xPali else False
