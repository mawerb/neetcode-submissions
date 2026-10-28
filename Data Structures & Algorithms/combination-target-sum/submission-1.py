class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, total, arr):
            if total == target:
                res.append(arr.copy())
                return
            if i == len(nums):
                return

            curr = nums[i]

            if total + curr <= target:
                arr.append(curr)
                backtrack(i, total+curr, arr)
                arr.pop()

            backtrack(i+1, total, arr)

        backtrack(0, 0, [])

        return res