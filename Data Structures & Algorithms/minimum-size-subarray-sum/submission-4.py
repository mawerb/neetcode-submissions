class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            if(nums[0] >= target):
                return 1
            else:
                return 0

        l = 0
        r = 0
        min_len = float('inf')
        running_sum = 0


        while l <= r and r < len(nums):
            running_sum += nums[r]

            while running_sum >= target and l <= r:
                min_len = min(min_len, r - l + 1)
                running_sum -= nums[l]
                l += 1
            r += 1
        if min_len == float('inf'):
            return 0
        return min_len