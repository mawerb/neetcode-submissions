class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if (length <= 1):
            return nums

        mid = (length // 2)

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        sorted_list = []

        while (left or right):
            if (not left):
                sorted_list.append(right.pop(0))
            elif (not right):
                sorted_list.append(left.pop(0))
            elif (left[0] <= right[0]):
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        
        return sorted_list

