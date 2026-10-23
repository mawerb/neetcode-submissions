class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","-","*","/"}
        ops = []
        vals = []

        for token in tokens:
            if token in operators:
                b = vals.pop()
                a = vals.pop()
                if token == "+":
                    vals.append(a + b)
                elif token == "-":
                    vals.append(a - b)
                elif token == "*":
                    vals.append(a * b)
                else:
                    # Truncate toward zero, as required for RPN division.
                    quotient = abs(a) // abs(b)
                    vals.append(-quotient if (a < 0) != (b < 0) else quotient)
            else:
                vals.append(int(token))


        return vals.pop()
            