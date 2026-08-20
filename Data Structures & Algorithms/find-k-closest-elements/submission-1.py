class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        r = 0
        min_diff = float('inf')

        while r < len(arr):
            curr_diff = abs(arr[r] - x)
            if curr_diff > min_diff:
                r -= 1
                break
            min_diff = curr_diff
            r += 1
        
        if r == len(arr):
            r -= 1

        res = [arr[r]]
        l = r - 1
        r = r + 1
        while len(res) < k:
            if r >= len(arr):
                res.insert(0,arr[l])
                l -= 1
            elif l < 0:
                res.append(arr[r])
                r += 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                res.insert(0,arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
        return res