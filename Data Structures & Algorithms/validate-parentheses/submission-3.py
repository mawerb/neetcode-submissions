class Solution:
    def isValid(self, s: str) -> bool:
        parenR = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for c in s:
            if c in parenR and (not stack or stack.pop() != parenR[c]):
                return False
            elif c not in parenR:
                stack.append(c)

        if stack:
            return False
        return True

