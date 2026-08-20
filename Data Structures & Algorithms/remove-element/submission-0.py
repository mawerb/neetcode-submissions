class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        moved = 0
        i = 0

        while moved < len(nums):
            if nums[i] == val:
                nums.pop(i)
                nums.append(val)
                count += 1
                i -= 1
            moved += 1
            i += 1

        return moved - count  