class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix = [0] * n
        postfix = [0] * n

        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])

        postfix[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            postfix[i] = max(postfix[i + 1], height[i])

        total_water = 0
        for i, curr_height in enumerate(height):
            max_left = prefix[i]
            max_right = postfix[i]
            max_water = max(0, min(max_left, max_right) - curr_height)
                
            total_water += max_water
        
        return total_water
        