class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = []
        N = len(nums)

        for i in range(N):
            if i <= 1:
                dp.append(nums[i])
            elif i == 2:
                dp.append(dp[0] + nums[i])
            else:
                dp.append(0)


        for i in range(3, N):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])
            
        return max(dp[N - 1], dp[N-2])
