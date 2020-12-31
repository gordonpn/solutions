class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        size = len(height)
        maxes_left = [0] * size
        maxes_right = [0] * size
        
        maxes_left[0] = height[0]
        for i in range(1, size):
            maxes_left[i] = max(height[i], maxes_left[i - 1])
            
        height = height[::-1]
        
        maxes_right[0] = height[0]
        for i in range(1, size):
            maxes_right[i] = max(height[i], maxes_right[i - 1])
            
        height = height[::-1]
        maxes_right = maxes_right[::-1]
        result = 0
        
        for i in range(size):
            result += min(maxes_right[i], maxes_left[i]) - height[i]
            
        return result
