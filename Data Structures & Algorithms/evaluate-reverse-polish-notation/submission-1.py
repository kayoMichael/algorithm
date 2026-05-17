class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
                continue
            
            if len(token) > 1 and token[0] == "-":
                stack.append(int(token[1:]) * -1)
                continue

            val2 = stack.pop()
            val1 = stack.pop()
            if token == "+":
                stack.append(val1 + val2)

            if token == "-":
                stack.append(val1 - val2)

            if token == "*":
                stack.append(val1 * val2)

            if token == "/":
                stack.append(int(val1 / val2))


        return stack[0]

            