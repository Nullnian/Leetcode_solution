# Question 9:
    # Longest Common Prefix
    # Write a function to find the longest common prefix string amongst an array of strings.
    # If there is no common prefix, return an empty string "".

# The leetcode solution
class Solution(object):
    def longestCommonPrefix(self, strs):
        if str == 0:
            return ""
        
        minStrs = min(strs) # ordered by ascii
        maxStrs = max(strs)
        for i in range (len(minStrs)):
            if minStrs[i] != maxStrs[i]:
                return minStrs[:i]
        return minStrs