class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)-2):
            sub = s[i:]
            try:
                a = sub.index("a")
                b = sub.index("b")
                c = sub.index("c")
                total += len(s)-max(a,b,c) - i
            except ValueError:
                next
        return total
