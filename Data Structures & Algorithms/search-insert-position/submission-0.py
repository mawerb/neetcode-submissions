class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        while (end - start) >= 2:
            midpt = start + (end - start)//2

            if nums[midpt] == target:
                return midpt
            elif nums[midpt] > target:
                end = midpt
            else:
                start = midpt

        if nums[start] >= target:
            return start    
        return start + 1
