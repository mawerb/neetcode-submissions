# [7,1,7,2,2,4]
# We calculate the max area of the position that we are at 
# by storing the minimum number we've seen so far and multiply it
# to the index - the last non-zero value we've been on
 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        last_min_value = []
        max_value = -1

        for i in range(len(heights)):
            curr_height = heights[i]
            last_index = i
            if (not last_min_value):
                last_min_value.append((i, curr_height))
                continue

            while (last_min_value and last_min_value[-1][1] > curr_height):
                width1, height = last_min_value.pop()
                max_value = max(max_value, (height * (i - width1)))
                last_index = width1
            if (last_min_value and last_min_value[-1][1] == curr_height):
                continue

            if (last_min_value):
                last_min_value.append((last_index, curr_height))
            else:
                last_min_value.append((0, curr_height))

        while last_min_value:
            width1, height = last_min_value.pop()
            max_value = max(max_value, (height * (len(heights) - width1)))

        return max_value
        