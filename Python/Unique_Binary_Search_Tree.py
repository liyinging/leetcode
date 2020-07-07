class Solution:
    def numTrees(self, n: int) -> int:
        ans = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                ans[i] += ans[j - 1] * ans[i - j]
        return ans[n]
