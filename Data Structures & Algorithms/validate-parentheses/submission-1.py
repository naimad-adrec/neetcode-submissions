class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closed_to_open = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        for char in s:
            if stack and char in closed_to_open:
                if closed_to_open[char] == stack[-1]:
                    stack.pop()
                    continue
                
                return False
            
            stack.append(char)
        
        return not stack
        