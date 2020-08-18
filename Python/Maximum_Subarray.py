from typing import List


class Solution:
    def maxSubArrayGreedy(self, nums: List[int]) -> int:
        if not nums:
            return None
        max_sum = curr_sum = float('-inf')
        for i in range(len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(curr_sum, max_sum)
        return max_sum

    def maxSubArrayDP(self, nums: List[int]) -> int:
        """
        Kadane's algorithm
        """
        if not nums:
            return None
        ans = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            ans = max(ans, nums[i])
        return ans

    # TODO: Devide and Conquer
