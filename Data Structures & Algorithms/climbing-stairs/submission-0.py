class Solution:
    def climbStairs(self, n: int) -> int:
        seen = { 1 : 1, 2: 2 }

        for i in range(3, n+1):
            seen[i] = seen[i-2] + seen[i-1]

        return seen[n]