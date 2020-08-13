from typing import List
from collections import Counter


class Solution:
    def majorityElementHashMap(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        """
        counter = Counter(nums)
        return max(counter, key=counter.get)

    def majorityElementSorting(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
