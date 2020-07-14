#Given a string, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        greedyString = ""
        maxLength = 0
        if len(s) in [0,1]:
            return len(s)
        for i in range(0, len(s)-1):
            greedyString = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in greedyString:
                    greedyString += s[j]
                    if len(greedyString) > maxLength:
                        maxLength = len(greedyString)
                    continue
                elif len(greedyString) > maxLength:
                    maxLength = len(greedyString)
                break            
        return maxLength
        
