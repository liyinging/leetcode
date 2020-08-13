from typing import List
from collections import Counter


class Solution:
    def findPairsBruteForce(self, nums: List[int], k: int) -> int:
        """
        Brute Force
        Time Limit Exceeded
        """
        if not nums:
            return 0
        ans = 0
        nums.sort()
        rec = set()
        for i in range(len(nums)):
            if i < len(nums) - 1:
                for j in range(i + 1, len(nums)):
                    if nums[j] - nums[i] == k and (nums[i], nums[j]) not in rec:
                        rec.add((nums[i], nums[j]))
                        ans += 1
        return ans

    def findPairsTwoPointers(self, nums: List[int], k: int) -> int:
        left, right = 0, 1
        ans, n = 0, len(nums)
        while left < n and right < n:
            if left >= right or nums[right] - nums[left] < k:
                right += 1
            elif nums[right] - nums[left] > k:
                left += 1
            else:
                left += 1
                ans += 1
                while nums[left] == nums[left - 1] and left < n:
                    left += 1
        return ans

    def findPairsHashMap(self, nums: List[int], k: int) -> int:
        """
        Hashmap Approach
        Time Complexity: O(N)
        Space Complexity: O(M) where M is the number of unique numbers in nums
        """
        counter = Counter(nums)
        ans = 0
        for x in counter:
            if k > 0 and x + k in counter:
                ans += 1
            elif k == 0 and counter[x] > 1:
                ans += 1
        return ans
