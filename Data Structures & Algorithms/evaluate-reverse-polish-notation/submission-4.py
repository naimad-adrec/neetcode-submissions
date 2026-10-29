class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                opperand_1 = stack.pop()
                opperand_2 = stack.pop()
                result = opperand_2 + opperand_1
            elif token == '-':
                opperand_1 = stack.pop()
                opperand_2 = stack.pop()
                result = opperand_2 - opperand_1
            elif token == '*':
                opperand_1 = stack.pop()
                opperand_2 = stack.pop()
                result = opperand_1 * opperand_2
            elif token == '/':
                opperand_1 = stack.pop()
                opperand_2 = stack.pop()
                result = int(float(opperand_2) / opperand_1)
            else:
                result = int(token)
            
            stack.append(result)

        return stack[0]
        