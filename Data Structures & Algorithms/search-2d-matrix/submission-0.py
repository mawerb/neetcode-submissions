class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        b = len(matrix) - 1
        t = 0

        while t <= b:
            curr = (t + b) // 2

            if matrix[curr][0] <= target <= matrix[curr][-1]:
                toSearch = matrix[curr]
                break
            elif matrix[curr][0] < target:
                t = curr + 1
            else:
                b = curr - 1

        if t > b:
            return False

        l = 0
        r = len(matrix[curr]) - 1
        arr = matrix[curr]

        while l <= r:
            
            mid = (l+r) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

        