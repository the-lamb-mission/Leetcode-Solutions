class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()

        if s == "":
            return 0

        sign = 1
        total = "0"
        if s[0] == "+":
            s = s[1:]
        elif s[0] == "-":
            s = s[1:]
            sign = -1
        
        for i in range(len(s)):
            if s[i].isdigit():
                total += s[i]
            else:
                break
        return max(min(int(total)*sign, 2**31-1),-2**31)

        

