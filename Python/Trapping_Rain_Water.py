from typing import List


class Solution:
    def trapDP(self, height: List[int]) -> int:
        """
        Dynamic Programming
        """
        max_from_left = [None] * len(height)
        max_from_right = [None] * len(height)
        max_from_left[0], max_from_right[-1] = height[0], max_from_right[-1]
        # Iterate from left to find all maximums
        for i in range(1, len(height)):
            max_from_left[i] = max(max_from_left[i - 1], height[i])
        # Iterate from right to find all maximums
        for i in range(len(height) - 2, -1, -1):
            max_from_right[i] = max(max_from_right[i + 1], height[i])
        ans = 0
        for i in range(len(height)):
            ans += min(max_from_left[i], max_from_right[i]) - height[i]
        return ans

    def trapStack(self, height: List[int]) -> int:
        """
        Using Stack
        """
        stack = []
        ans = 0
        i = 0
        while i < len(height):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                delta_height = min(height[stack[-1]], height[i]) - height[top]
                delta_dist = i - stack[-1] - 1
                ans += delta_dist * delta_height
            i += 1
            stack.append(i)
        return ans

    def trapTwoPointers(self, height: List[int]) -> int:
        """
        Two Pointers
        """
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans
