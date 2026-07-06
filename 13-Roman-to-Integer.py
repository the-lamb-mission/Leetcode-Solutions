import re

class Solution:
    def romanToInt(self, s: str) -> int:
        valMap = [
            ["M", 1000],
            ["CM", 900],
            ["CD", 400],
            ["D", 500],
            ["C", 100],
            ["XC", 90],
            ["XL", 40],
            ["L", 50],
            ["X", 10],
            ["IX", 9],
            ["IV", 4],
            ["V", 5],
            ["I", 1],
        ]
        
        finalAns = 0

        for char, val in valMap:
            while re.match(char, s):
                finalAns += val 
                s = s[len(char):]
        
        return finalAns
