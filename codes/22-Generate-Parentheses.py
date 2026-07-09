from itertools import product

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def checkParenthesis(a):
            stack = []
            for char in a:
                try:
                    if char == ")":
                        if stack.pop() != "(":
                            return False
                    else:
                        stack.append(char)
                except IndexError:
                    return False

            return stack == []

        p = map(lambda x: "".join(x),list(product("()", repeat = n*2)))
        p = filter(lambda x: checkParenthesis(x), p)
        
        return list(p)
