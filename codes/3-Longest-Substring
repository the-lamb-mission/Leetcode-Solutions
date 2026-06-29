class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxN = 0
        frontPointer = 0
        for backPointer in range(0,len(s)):
            while len(s[frontPointer:backPointer+1]) != len(set(s[frontPointer:backPointer+1])):
                frontPointer += 1
            maxN = max(backPointer - frontPointer + 1, maxN)
        return maxN
