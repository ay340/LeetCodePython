#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) in [0,1]:
            return s
        
        ind = [[i,i] for i in range(0,len(s))] + [[i,i+1] for i in range(0,len(s)-1) if s[i] == s[i+1]]
        
        for i in range(0, len(ind)):
            while ind[i][0] != 0 and ind[i][1] != len(s)-1 and s[ind[i][0]-1] == s[ind[i][1]+1]:
                ind[i][0] -= 1
                ind[i][1] += 1
        
        m = max(ind, key = lambda x: x[1]-x[0])
        return(s[m[0]:m[1]+1])
