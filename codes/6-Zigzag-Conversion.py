class Solution:
    def convert(self, s: str, numRows: int) -> str:
        out = ""
        if numRows == 1:
            return s

        for i in range(0, len(s), max((numRows-1)*2,1)):
            out += s[i]

        for i in range(1, numRows-1):
            index = i
            gap = (numRows-1-i)*2
            antigap = (numRows-1)*2 - gap
            while index < len(s):
                out += s[index]
                index += gap
                if index >= len(s):
                    break
                out += s[index]
                index += antigap
        
        for i in range(numRows-1, len(s), max((numRows-1)*2,1)):
            out += s[i]
            
        return out
