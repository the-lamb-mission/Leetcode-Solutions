class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in range(len(s)+1,0,-1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    longest = substring if len(substring) > len(longest) else longest
                    break
        return longest
        
