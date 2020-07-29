from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans = 0
        while len(arr) > 1:
            idx = arr.index(min(arr))
            ans += min(arr[idx - 1:idx] + arr[idx + 1:idx + 2]) * arr.pop(idx)
        return ans
