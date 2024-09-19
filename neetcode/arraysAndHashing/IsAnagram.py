# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.

# https://neetcode.io/problems/is-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        
        sDict = {}
        tDict = {}

        for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]] += 1
            else:
                sDict[s[i]] = 1
            
            if t[i] in tDict:
                tDict[t[i]] += 1
            else:
                tDict[t[i]] = 1

        return sDict == tDict