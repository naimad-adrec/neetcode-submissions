class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closed_to_open = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        for char in s:
            if char in closed_to_open:
                if stack and stack[-1] == closed_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack
        