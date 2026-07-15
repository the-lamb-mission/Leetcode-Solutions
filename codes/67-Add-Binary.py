class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = max(len(a), len(b))
        a, b = a.zfill(x), b.zfill(x)

        car = 0
        out = ""
        for i in range(x-1, -1, -1):
            print(i, a, b, x)
            val = int(a[i])+int(b[i]) + car
            out = str(val%2) + out
            car = val//2
        if car:
            out = "1" + out

        return out        
