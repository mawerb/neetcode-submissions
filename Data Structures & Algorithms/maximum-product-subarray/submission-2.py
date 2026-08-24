class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        negatives = []
        largest = float('-inf')
        boundary = 0

        def evaluate_segment(start,end):
            if start > end:
                return float("-inf")

            lValid = False
            rValid = False

            if negatives[-1] > start:
                left = dp[negatives[-1]-1]
                lValid = True
            if negatives[0] < end:
                right = dp[end] // dp[negatives[0]]
                rValid = True

            if lValid and rValid:
                return max(left,right)
            elif lValid:
                return left
            elif rValid:
                return right
            else:
                return float('-inf')

        for i in range(len(nums)):
            if nums[i] == 0:
                dp[i] = 0
                if len(negatives) % 2 == 1:
                    largest = max(largest,evaluate_segment(boundary,i-1))
                boundary = i+1
                negatives = []

            if nums[i] > largest:
                largest = nums[i]

            if i == boundary:
                dp[i] = nums[i]
            elif nums[i] != 0:
                dp[i] = dp[i-1] * nums[i]
            if nums[i] < 0:
                negatives.append(i)

            if dp[i] > largest:
                largest = dp[i]

        if len(negatives) % 2 == 1:
            largest = max(largest,evaluate_segment(boundary,len(nums)-1))

        return largest