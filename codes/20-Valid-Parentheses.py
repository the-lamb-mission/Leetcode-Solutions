class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            try:
                match char:
                    case ")":
                        if stack.pop() != "(":
                            return False
                    case "}":
                        if stack.pop() != "{":
                            return False
                    case "]":
                        if stack.pop() != "[":
                            return False
                    case _:
                        stack.append(char)
            except IndexError:
                return False

        return stack == []
