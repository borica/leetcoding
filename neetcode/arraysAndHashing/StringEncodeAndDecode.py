# String Encode and Decode
# Solved 
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.

# https://neetcode.io/problems/string-encode-and-decode

## Solution below has a flaw, although it passes all neetcode cases, if a string has the | delimiter, output will fail. 
## There is a solution involving appending  along with the delimiter, the size of the encoded string, this way you dont have to worry about misinputing strings.

class Solution:
    separator = '|'

    def encode(self, strs: List[str]) -> str:
        output = ''
        
        for i in strs:
            output += i + self.separator

        return output



    def decode(self, s: str) -> List[str]:
        output = []
        aux = ''

        for i in range(len(s)):
            if s[i] == self.separator:
                output.append(aux)
                aux = ''
                continue

            aux += s[i]

        return output