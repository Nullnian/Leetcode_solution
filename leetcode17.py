# Question 17:
    # Letter Combinations of a Phone Number
    # Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
    # A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# The leetcode solution
class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        phoneMap = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        asw = []
        def recursion(i, possiWord):
            if i == len(digits):
                asw.append(possiWord)
                return
            
            for j in phoneMap[digits[i]]:
                recursion(i+1, possiWord+j)
        recursion(0, "")
        return asw
