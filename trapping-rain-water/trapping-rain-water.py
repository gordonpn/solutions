class Solution:
    def trap(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1

        max_left = 0
        max_right = 0

        result = 0

        while left_pointer < right_pointer:
            if height[left_pointer] < height[right_pointer]:
                if height[left_pointer] > max_left:
                    max_left = height[left_pointer]
                else:
                    result += (max_left - height[left_pointer])
​
                left_pointer += 1

            else:
                if height[right_pointer] > max_right:
                    max_right = height[right_pointer]
                else:
                    result += (max_right - height[right_pointer])
​
                right_pointer -= 1


        return result
