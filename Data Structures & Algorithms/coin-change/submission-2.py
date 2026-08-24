class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [-1] * (amount+1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                remaining_amt = i-c

                if remaining_amt >= 0 and dp[i-c] != -1:
                    potential = dp[i-c] + 1
                    print(potential)
                    
                    if dp[i] == -1 or dp[i] > potential:
                        dp[i] = potential

        return dp[amount]